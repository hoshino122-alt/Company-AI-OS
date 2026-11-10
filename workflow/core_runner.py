"""Adapter for calling the existing Company AI OS CORE from Workflow.

The CORE function is injected rather than imported at module load time.
This keeps unit tests independent from Ollama, memory files, and Tool side effects.
"""

import json

from employees.definitions import EMPLOYEES, EMPLOYEE_ROLES
from workflow.answer_validator import validate_answer



class CoreTaskRunner:
    """Call an injected CORE process(question) function for each Workflow Task."""

    def __init__(
        self,
        process_fn,
        include_previous_result=True,
        validate_answers=False,
        required_keywords=None,
        max_answer_length=None,
        forbidden_phrases=None,
        max_bullet_items=None,
        require_bullet_format=None,
        reject_duplicate_bullet_items=None,
    ):
        if not callable(process_fn):
            raise TypeError("process_fn must be callable")

        self.process_fn = process_fn
        self.include_previous_result = include_previous_result
        # Validation feedback is isolated by Task ID to prevent cross-task leakage.
        self._validation_feedback = {}
        self.validate_answers = validate_answers
        self.required_keywords = required_keywords or {}
        self.max_answer_length = max_answer_length
        self.forbidden_phrases = forbidden_phrases or {}
        self.max_bullet_items = max_bullet_items or {}
        self.require_bullet_format = require_bullet_format or {}
        self.reject_duplicate_bullet_items = (
            reject_duplicate_bullet_items or {}
        )

    def __call__(self, task, previous_result):
        input_data = task.get("input_data") or {}
        question = input_data.get("question")

        if not isinstance(question, str) or not question.strip():
            raise ValueError(
                f"Task '{task.get('name', task.get('task_id'))}' "
                "requires input_data['question'] as a non-empty string."
            )

        employee_id = input_data.get("employee_id")

        if employee_id is not None:
            if not isinstance(employee_id, str) or not employee_id.strip():
                raise ValueError("employee_id must be a non-empty string.")

            if employee_id not in EMPLOYEES:
                raise ValueError(
                    f"Unknown employee_id: {employee_id!r}. "
                    f"Registered employees: {', '.join(EMPLOYEES)}"
                )

            employee = EMPLOYEES[employee_id]

            if not employee.get("enabled", False):
                raise ValueError(
                    f"Employee '{employee_id}' is disabled."
                )

        role_instruction = EMPLOYEE_ROLES.get(employee_id)
        task_instruction = input_data.get("instructions", "")
        prompt = question.strip()
        task_key = task.get("task_id") or task.get("id")

        if task_key is None:
            task_key = task.get("name")

        if task_key is None:
            task_key = f"{employee_id!r}:{question.strip()}"

        if role_instruction:
            prompt = (
                f"【担当AI社員：{employee_id}】\n"
                f"{role_instruction}\n\n"
                f"【今回の依頼】\n{prompt}"
            )

        if task_instruction:
            prompt = (
            f"{prompt}\n\n"
            "【Task固有の追加指示】\n"
            f"{task_instruction}"
        )

        if self.include_previous_result and previous_result is not None:
            prompt = (
                f"{prompt}\n\n"
                "【前のTaskの実行結果】\n"
                f"{json.dumps(previous_result, ensure_ascii=False, default=str)}\n\n"
                "前のTaskの結果を必要に応じて利用して回答してください。"
            )

        feedback = self._validation_feedback.get(task_key)
        if feedback:
            prompt = (
                f"{prompt}\n\n"
                "【前回の回答検証エラー：修正必須】\n"
                f"{feedback}\n"
                "上記のエラーをすべて解消するように回答を作り直してください。"
                "元の依頼、担当AI社員の役割、すべての回答制約は引き続き守ってください。"
                "必須キーワードは指定された文字列どおりに含めてください。"
            )

        answer = self.process_fn(prompt)

        if self.validate_answers:
            validation = validate_answer(
                answer,
                required_keywords=self.required_keywords.get(
                    employee_id, []
                ),
                max_length=self.max_answer_length,
                forbidden_phrases=self.forbidden_phrases.get(
                    employee_id, []
                ),
                max_bullet_items=self.max_bullet_items.get(
                    employee_id
                ),

                require_bullet_format=self.require_bullet_format.get(
                    employee_id, False
                ),
                reject_duplicate_bullet_items=(
                    self.reject_duplicate_bullet_items.get(
                        employee_id, False
                    )
                ),
            )


            if not validation["valid"]:
                feedback = " / ".join(validation["errors"])
                self._validation_feedback[task_key] = feedback
                raise ValueError(
                    "回答検証に失敗しました: " + feedback
                )

        self._validation_feedback.pop(task_key, None)
        return {"answer": answer}

