default core_status = "OFFLINE"
default core_power = 0
default core_message = "Waiting..."
default boot_step = 0
default core_log = "AI Core Boot"
default core_log_time = "12:00:10"
default core_log_seconds = 10
default core_log_history = []
default queue_boot = "WAITING"
default queue_memory = "WAITING"
default queue_initialize = "WAITING"
default queue_ai_engine = "WAITING"
default ai_engine_timer = 0.0
default queue_task = "WAITING"
default task_timer = 0
default current_task = ""
default current_task_id = 1
default task_result = ""
default task_queue = []
default current_task_index = 0


init python:

    def core_start():

        store.boot_step = 0
        store.core_status = "BOOTING"
        store.core_message = "SYSTEM BOOT"
        store.queue_boot = "RUNNING"


    def core_initialize():

        store.boot_step = 1
        store.core_status = "INITIALIZING"
        store.core_message = "AI CORE INITIALIZING..."
        store.queue_memory = "RUNNING"
        store.queue_initialize = "RUNNING"

    def core_online():

        store.boot_step = 2
        store.core_status = "ONLINE"
        store.core_power = 100
        store.core_message = "AI CORE ONLINE"

        store.queue_boot = "DONE"
        store.queue_memory = "DONE"
        store.queue_initialize = "DONE"
        store.queue_ai_engine = "RUNNING"
        store.ai_engine_timer = 0.0
        store.queue_task = "WAITING"

        initialize_task_queue()

    def core_monitor_update():

        # COREがONLINEのときだけ監視値を更新
        if store.core_status == "ONLINE":

            store.gpu_usage += 2

            if store.gpu_usage > 80:
                store.gpu_usage = 70

            store.vram_usage += 0.1

            if store.vram_usage > 14.8:
                store.vram_usage = 14.0

            store.core_log = "GPU %d%%  VRAM %.1f GB  TOKENS %d/s  MEMORY %d  LOAD %s" % (
            store.gpu_usage,
            store.vram_usage,
            store.tokens_speed,
            store.memory_nodes,
            core_load_state()
            )

            store.core_log_seconds += 5

            hours = store.core_log_seconds // 3600
            minutes = (store.core_log_seconds % 3600) // 60
            seconds = store.core_log_seconds % 60

            store.core_log_time = "%02d:%02d:%02d" % (
                hours,
                minutes,
                seconds
            )

            store.core_log_history.append(
                "%s  %s" % (
                    store.core_log_time,
                    store.core_log
                )
            )

            if len(store.core_log_history) > 4:
                store.core_log_history.pop(0)


            store.tokens_speed += 1

            if store.tokens_speed > 50:
                store.tokens_speed = 40


            store.memory_nodes += 10  

    def add_core_log(message):

        store.core_log = message

        store.core_log_history.append(
            "%s  %s" % (
                store.core_log_time,
                message
            )
        )

        if len(store.core_log_history) > 8:
            store.core_log_history.pop(0)

    def ai_engine_complete():

        if store.core_status == "ONLINE":

            if store.queue_ai_engine == "RUNNING":

                store.queue_ai_engine = "DONE"

                store.queue_task = "RUNNING"

                add_core_log("AI Engine Complete")
 
    def task_start():

        if store.core_status == "ONLINE":

            if store.queue_task == "RUNNING":

                load_current_task()

                add_core_log(
                    "TASK %03d RECEIVED: %s" % (
                        store.current_task_id,
                        store.current_task
                    )
                )

    def load_current_task():

        if store.task_queue:

            task = store.task_queue[store.current_task_index]

            store.current_task_id = task["id"]

            store.current_task = task["name"]                  

    def core_load_state():

        if store.gpu_usage >= 75:
            return "HIGH"

        elif store.gpu_usage >= 60:
            return "ACTIVE"

        else:
            return "STABLE"

    def task_processing():

        if store.core_status == "ONLINE":

            if store.queue_task == "RUNNING":

                add_core_log(
                    "TASK %03d PROCESSING: %s" % (
                        store.current_task_id,
                        store.current_task
                    )
                )


    def task_complete():

        if store.core_status == "ONLINE":

            store.task_timer = 0

            if store.queue_task == "RUNNING":

                if store.current_task_id == 1:

                    store.task_result = "System status analysis complete"

                elif store.current_task_id == 2:

                    store.task_result = "Memory status check complete"

                elif store.current_task_id == 3:

                    store.task_result = "AI Engine initialization complete"

                store.queue_task = "DONE"

                add_core_log(
                    "TASK %03d COMPLETE: %s" % (
                        store.current_task_id,
                        store.task_result
                    )
                )

                if store.current_task_index < len(store.task_queue) - 1:

                    store.current_task_index += 1

                    load_current_task()

                    store.queue_task = "RUNNING"

                    add_core_log(
                        "NEXT TASK READY: %03d %s" % (
                            store.current_task_id,
                            store.current_task
                        )
                    )

                else:

                    add_core_log(
                        "TASK QUEUE COMPLETE"
                    )

    def initialize_task_queue():

        store.task_queue = [
            {
                "id": 1,
                "name": "Analyze system status"
            },
            {
                "id": 2,
                "name": "Check memory status"
            },
            {
                "id": 3,
                "name": "Initialize AI Engine"
            }
        ]

        store.current_task_index = 0


    def task_sequence_update():

        if store.core_status != "ONLINE":
            return

        # AI Engineが起動中なら、まず完了させる
        if store.queue_ai_engine == "RUNNING":

            store.ai_engine_timer += 1.0

            if store.ai_engine_timer >= 3.0:

                store.queue_ai_engine = "DONE"
                store.queue_task = "RUNNING"

                store.ai_engine_timer = 0.0

                add_core_log("AI Engine Complete")

                load_current_task()

                add_core_log(
                    "TASK %03d RECEIVED: %s" % (
                        store.current_task_id,
                        store.current_task
                    )
                )

            return


        # Task処理
        if store.queue_task == "RUNNING":

            store.task_timer += 1

            # TASK 001を2秒処理
            if store.task_timer == 1:

                add_core_log(
                    "TASK %03d PROCESSING: %s" % (
                        store.current_task_id,
                        store.current_task
                    )
                )

            if store.task_timer >= 2:

                task_complete()

                store.task_timer = 0

        
screen day38_right_video():

    add Movie(
        play="videos/day38_right.webm",
        loop=True
    ):
        xpos 1500
        ypos 100
        xsize 420
        ysize 800

screen day38_subtitle(message):

    text message:
        xpos 620
        ypos 850
        xsize 700
        text_align 0.5
        size 30
        color "#ffffff"       