image day38_01 = "images/day38/day38_01.png"
image day38_02 = "images/day38/day38_02.png"
image day38_03 = "images/day38/day38_03.png"
image day38_04 = "images/day38/day38_04.png"
image day38_05 = "images/day38/day38_05.png"
image day38_06 = "images/day38/day38_06.png"
image day38_07 = "images/day38/day38_07.png"


# ============================================
# DAY38
# Company AI OS
# AI CORE Boot Sequence
# ============================================


label day38:

    scene black

    play music "audio/Future.mp3" fadein 2.0 volume 0.3


    # ============================================
    # DAY38_01
    # ============================================

    show expression Image("images/day38/day38_01.png") with fade

    voice "voice/day38/day38_01.ogg"

    pause 9.0


    # ============================================
    # DAY38_02
    # ============================================

    show expression Image("images/day38/day38_02.png") with fade

    voice "voice/day38/day38_02.ogg"

    pause 10.0


    # ============================================
    # DAY38_03
    # ============================================

    show expression Image("images/day38/day38_03.png") with fade

    voice "voice/day38/day38_03.ogg"

    pause 10.0


    # ============================================
    # DAY38_04
    # ============================================

    show expression Image("images/day38/day38_04.png") with fade

    voice "voice/day38/day38_04.ogg"

    pause 9.0


    # ============================================
    # DAY38_05
    # ============================================

    show expression Image("images/day38/day38_05.png") with fade

    voice "voice/day38/day38_05.ogg"

    pause 8.0


    # ============================================
    # DAY38_06
    # ============================================

    #show expression Image("images/day38/day38_06.png") with fade

    #voice "voice/day38/day38_06.ogg"

    #pause 5.0


    # ============================================
    # DAY38_07
    # 実際のAI CORE画面
    # ============================================

    scene black

    show screen company_ai_os

    pause 0.5


    # SYSTEM BOOT

    $ core_start()

    pause 2.0


    # AI CORE INITIALIZING...

    $ core_initialize()

    pause 2.0


    # AI CORE ONLINE

    $ core_online()

    pause 5.0


    hide screen company_ai_os

    scene black

    pause 1.0


    # ============================================
    # DAY38_08
    # ============================================

    show expression Image("images/day38/day38_08.png") with fade

    voice "voice/day38/day38_08.ogg"

    pause 7.0


    # ============================================
    # END
    # ============================================

    stop music fadeout 3.0

    scene black with fade

    pause 2.0

    return