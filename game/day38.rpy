image day38_01 = "images/day38/day38_01.png"
image day38_02 = "images/day38/day38_02.png"
image day38_03 = "images/day38/day38_03.png"
image day38_04 = "images/day38/day38_04.png"
image day38_05 = "images/day38/day38_05.png"
image day38_06 = "images/day38/day38_06.png"
image day38_07 = "images/day38/day38_07.png"
image day38_08 = "images/day38/day38_08.png"
image day38_09 = "images/day38/day38_09.png"
image day38_10 = "images/day38/day38_10.png"
image day38_11 = "images/day38/day38_11.png"
image day38_12 = "images/day38/day38_12.png"
image day38_13 = "images/day38/day38_13.png"
image day38_14 = "images/day38/day38_14.png"
image day38_15 = "images/day38/day38_15.png"



# ============================================
# DAY38
# Company AI OS
# AI CORE Boot Sequence
# ============================================


label day38:

    scene black
    
    play music "audio/Future.mp3" fadein 2.0 volume 0.3

    # ==================================================
    # DAY38_01
    # 実際に動いているAI CORE
    # ==================================================

    $ renpy.movie_cutscene("videos/day38_core_renpy.webm")

    call slide(
        img="day38_01",
        msg="これが、現在のAI COREです。\n"
            "AI COREが起動し、Taskを受け取り、\n"
            "処理を実行しています。",
        voice_file="voice/day38/day38_01.ogg",
        voice_duration=7.34,
        t1="AI CORE",
        t2="ONLINE",
        t3="TASK PROCESSING",
        t4="DAY38"
    )

    # ==================================================
    # DAY38_02
    # AI CORE開発開始
    # ==================================================

    call slide(
        img="day38_02",
        msg="しかし、最初からこうだったわけではありません。\n"
            "ここから、AI COREの開発を振り返ります。",
        voice_file="voice/day38/day38_02.ogg",
        voice_duration=8.06,
        t1="DAY38",
        t2="AI CORE",
        t3="DEVELOPMENT",
        t4=""
    )


    # ==================================================
    # DAY38_03
    # 起動状態
    # ==================================================

    call slide(
        img="day38_03",
        msg="これまでのAI COREは、画面を表示することはできました。\n"
            "しかし、内部状態を持っていませんでした。",
        voice_file="voice/day38/day38_03.ogg",
        voice_duration=8.66,
        t1="AI CORE",
        t2="STATE",
        t3="BEFORE",
        t4=""
    )


    # ==================================================
    # DAY38_04
    # boot_step
    # ==================================================

    call slide(
        img="day38_04",
        msg="そこで、起動状態を管理するため、\n"
            "boot_stepと状態管理機能を追加しました。",
        voice_file="voice/day38/day38_04.ogg",
        voice_duration=6.83,
        t1="BOOT STEP",
        t2="STATE",
        t3="AI CORE",
        t4=""
    )


    # ==================================================
    # DAY38_05
    # 起動シーケンス
    # ==================================================

    call slide(
        img="day38_05",
        msg="AI COREの起動処理を3段階に分割しました。\n"
            "SYSTEM BOOT、INITIALIZING、ONLINE。",
        voice_file="voice/day38/day38_05.ogg",
        voice_duration=7.89,
        t1="SYSTEM BOOT",
        t2="INITIALIZING",
        t3="ONLINE",
        t4="BOOT SEQUENCE"
    )


    # ==================================================
    # DAY38_06
    # Ren'Py実装
    # ==================================================

    call slide(
        img="day38_06",
        msg="Ren'Py上で状態を切り替え、\n"
            "AI COREが順番に起動する演出を実装しました。",
        voice_file="voice/day38/day38_06.ogg",
        voice_duration=6.29,
        t1="REN'PY",
        t2="STATE CONTROL",
        t3="AI CORE",
        t4="ONLINE"
    )

    
    # ==================================================
    # DAY38_07
    # Task Queue
    # ==================================================

    scene black

    show screen day38_right_video

    show screen day38_subtitle(
        "次に、AI COREが実行するTaskを管理するため、\n"
        "Task Queueを実装しました。"
    )

    play sound "voice/day38/day38_07.ogg"

    $ renpy.pause(7.27, hard=True)

    stop sound

    hide screen day38_subtitle
    hide screen day38_right_video



    # ==================================================
    # DAY38_08
    # Task登録
    # ==================================================

    call slide(
        img="day38_08",
        msg="TaskをQueueに登録し、\n"
            "順番に処理できるようにしました。",
        voice_file="voice/day38/day38_08.ogg",
        voice_duration=4.81,
        t1="TASK 001",
        t2="TASK 002",
        t3="TASK 003",
        t4="QUEUE"
    )


    # ==================================================
    # DAY38_09
    # Task状態
    # ==================================================

    scene black

    show screen day38_right_video

    show screen day38_subtitle(
        "Taskには、受信、処理、完了という状態を持たせました。\n"
        "Taskの状態が順番に変化していきます。"
    )

    play sound "voice/day38/day38_09.ogg"

    $ renpy.pause(7.0, hard=True)

    stop sound

    hide screen day38_subtitle
    hide screen day38_right_video


    # ==================================================
    # DAY38_10
    # Task 001
    # ==================================================

    scene black

    show screen day38_right_video

    show screen day38_subtitle(
        "Task 001。\n"
        "システム状態の解析を実行します。"
    )

    play sound "voice/day38/day38_10.ogg"

    $ renpy.pause(4.97, hard=True)

    stop sound

    hide screen day38_subtitle
    hide screen day38_right_video


    # ==================================================
    # DAY38_11
    # Task 002
    # ==================================================

    scene black

    show screen day38_right_video

    show screen day38_subtitle(
        "Task 002。\n"
        "メモリ状態の確認を実行します。"
    )

    play sound "voice/day38/day38_11.ogg"

    $ renpy.pause(4.50, hard=True)

    stop sound

    hide screen day38_subtitle
    hide screen day38_right_video


    # ==================================================
    # DAY38_12
    # Task 003
    # ==================================================

    scene black

    show screen day38_right_video

    show screen day38_subtitle(
        "Task 003。\n"
        "AI Engineの初期化を実行します。"
    )

    play sound "voice/day38/day38_12.ogg"

    $ renpy.pause(4.88, hard=True)

    stop sound

    hide screen day38_subtitle
    hide screen day38_right_video


    # ==================================================
    # DAY38_13
    # システムモニター
    # ==================================================

    scene black

    show screen day38_right_video

    show screen day38_subtitle(
        "Taskの処理中は、GPU、VRAM、Memoryなどの\n"
        "システム状態も同時に監視します。"
    )

    play sound "voice/day38/day38_13.ogg"

    $ renpy.pause(7.59, hard=True)

    stop sound

    hide screen day38_subtitle
    hide screen day38_right_video


    # ==================================================
    # DAY38_14
    # AI CORE完成
    # ==================================================

    scene black

    show screen day38_right_video

    show screen day38_subtitle(
        "これでAI COREは、画面を表示するだけではなく、\n"
        "状態を持ち、Taskを順番に処理できるようになりました。"
    )

    play sound "voice/day38/day38_14.ogg"

    $ renpy.pause(8.64, hard=True)

    stop sound

    hide screen day38_subtitle
    hide screen day38_right_video


    # ==================================================
    # DAY38_15
    # 次回予告
    # ==================================================

    call slide(
        img="day38_15",
        msg="DAY38では、AI COREとTask処理の基盤を構築しました。\n"
            "次回は、この基盤をAIエージェント機能へ発展させます。",
        voice_file="voice/day38/day38_15.ogg",
        voice_duration=10.08,
        t1="NEXT",
        t2="AI AGENT",
        t3="TASK ENGINE",
        t4="DAY39"
)


    return
   
