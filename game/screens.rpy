transform boot_fade:

    alpha 0.0

    linear 1.0 alpha 1.0


transform boot_fade2:

    alpha 0.0

    linear 1.5 alpha 1.0

screen company_ai_os():

    default pulse = 0

    add Solid("#000000")

    use top_bar
    use left_panel
    use right_panel
    use bottom_log

    text "SYSTEM BOOT":
        xpos 760
        ypos 700
        size 28
        color "#66ffff"
        at boot_fade

    text "AI CORE INITIALIZING...":
        xpos 760
        ypos 750
        size 28
        color "#00ffff"
        at boot_fade2

    text "[core_message]":

        xpos 760
        ypos 800

        size 28
        color "#00ff88"

        at boot_fade2

#    text "BOOT STEP: [boot_step]":

#        xpos 760
#        ypos 850

#        size 22
#        color "#66ffff"

    text "BOOT PROGRESS":

        xpos 760
        ypos 860

        size 22
        color "#66ffff"


    bar:

        value boot_step

        range 2

        xpos 760
        ypos 920

        xsize 400
        ysize 20

    use center_panel

screen top_bar():

    frame:

        background "#001820CC"

        xpos 0
        ypos 0

        xfill True
        ysize 80


        text "Company AI OS":

            font "fonts/NotoSansJP-Regular.ttf"

            xpos 40
            ypos 20

            size 36

            color "#00ffff"


        text "DAY38":

            xpos 1700
            ypos 25

            size 28

            color "#66ffff"

screen center_panel():

    fixed:

        xpos 610
        ypos 150

        xsize 700
        ysize 700

        use ai_core_widget


screen left_panel():

    frame:

        background "#001820CC"

        xpos 30
        ypos 120

        xsize 280
        ysize 500


        has vbox

        spacing 15


        text "SYSTEM STATUS":

            size 28

            color "#00ffee"


        text "AI Core      ONLINE":

            size 22

            color "#00ff99"


        text "Memory       READY":

            size 22

            color "#66ffff"


        text "Command      READY":

            size 22

            color "#66ffff" 


screen right_panel():

    frame:

        background "#001820CC"

        xpos 1600
        ypos 120

        xsize 300
        ysize 500


        has vbox

        spacing 15


        text "COMMAND":

            size 28

            color "#00ffee"


        text "STATUS ONLINE":

            size 22

            color "#00ff99"


        text "QUEUE":

            size 24

            color "#66ffff"


        text "001 Boot":

            size 20


        text "002 Memory":

            size 20


        text "003 Initialize":

            size 20


        text "GPU [gpu_usage]%":

            size 20

            color "#00ffee"


        text "VRAM [vram_usage] GB":

            size 20

            color "#00ffee"


        text "TOKENS [tokens_speed]":

            size 20

            color "#00ffee"


        text "MEMORY [memory_nodes]":

            size 20

            color "#00ffee"

transform ring_rotate:

    rotate 0

    linear 8.0 rotate 360

    repeat


screen ai_core_widget():

    fixed:

        # 外側リング

        text "◌":

            xalign 0.5
            yalign 0.5

            size 320

            color "#00ccff55"

            at ring_rotate


        # 中央コア

        text "●":

            xalign 0.5
            yalign 0.5

            size 180

            color "#00ffff"

            at core_pulse


        # ラベル

        text "AI CORE":

            xalign 0.5

            ypos 500

            size 30

            color "#00ffee"


transform core_pulse:

    linear 1.0 zoom 1.15

    linear 1.0 zoom 1.0

    repeat



screen bottom_log():

    frame:

        background "#001820CC"

        xpos 30
        ypos 900

        xsize 1860
        ysize 130


        has vbox

        spacing 5


        text "SYSTEM LOG":

            size 26

            color "#00ffee"


        text "12:00:01  AI Core Boot":

            size 20


        text "12:00:03  Memory Ready":

            size 20


        text "12:00:05  Command Queue Ready":

            size 20


screen boot_overlay():

    frame:

        background "#000000AA"

        xalign 0.5
        yalign 0.5

        xsize 900
        ysize 250


        vbox:

            spacing 20


            text "COMPANY AI OS":

                xalign 0.5

                size 50

                color "#00ffff"


            text "CORE INITIALIZING...":

                xalign 0.5

                size 32

                color "#66ffff"                        