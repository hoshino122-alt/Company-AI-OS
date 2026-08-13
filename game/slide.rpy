init python:

    import os
    import wave
    import contextlib

    def get_voice_length(filename):

        try:

            # Ren'Pyのゲームディレクトリからの実ファイルパス
            path = renpy.loader.transfn(filename)

            if not os.path.exists(path):
                return 0.0

            # WAVの場合
            if filename.lower().endswith(".wav"):

                with contextlib.closing(wave.open(path, "rb")) as wf:

                    frames = wf.getnframes()
                    rate = wf.getframerate()

                    if rate == 0:
                        return 0.0

                    return frames / float(rate)

        except Exception:

            pass

        return 0.0


label slide(
    img,
    msg,
    voice_file="",
    voice_duration=3.0,
    t1="",
    t2="",
    t3="",
    t4=""
):

    scene black

    show expression img

    if voice_file != "":

        play sound voice_file

        $ renpy.pause(voice_duration, hard=True)

        stop sound

    else:

        $ renpy.pause(3.0, hard=True)

    return