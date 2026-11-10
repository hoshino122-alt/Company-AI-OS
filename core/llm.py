from ollama import chat


MODEL = "gemma4:12b"
#MODEL = "gemma4:e4b"

def ask_llm(messages):

    print("===== ASK LLM =====")

    response = chat(
        model=MODEL,
        messages=messages,
        think=False,
        options={
            "num_ctx": 8192,
            "num_gpu": 0,
        },
    )

    print("===== RESPONSE TYPE =====")
    print(type(response))
    print("=========================")

    print("===== RESPONSE REPR =====")
    print(repr(response))
    print("=========================")

    print("===== RESPONSE DICT =====")

    try:
        print(response.model_dump())
    except Exception as e:
        print("model_dump error:", e)

    print("=========================")

    print("===== MESSAGE REPR =====")

    try:
        print(repr(response.message))
    except Exception as e:
        print("message error:", e)

    print("=========================")

    print("===== CONTENT REPR =====")

    try:
        print(repr(response.message.content))
    except Exception as e:
        print("content error:", e)

    print("=========================")

    return response.message.content

