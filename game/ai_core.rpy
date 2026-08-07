default core_status = "OFFLINE"
default core_power = 0
default core_message = "Waiting..."
default boot_step = 0

init python:

    def core_start():

        store.boot_step = 0
        store.core_status = "BOOTING"
        store.core_message = "SYSTEM BOOT"


    def core_initialize():

        store.boot_step = 1
        store.core_status = "INITIALIZING"
        store.core_message = "AI CORE INITIALIZING..."


    def core_online():

        store.boot_step = 2
        store.core_status = "ONLINE"
        store.core_power = 100
        store.core_message = "AI CORE ONLINE"