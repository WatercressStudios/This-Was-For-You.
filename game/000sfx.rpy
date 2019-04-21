#
# SFX thing
#

transform sfx_inout:
    on show:
        pos (460, 750) alpha 0
        parallel:
            linear 0.3 alpha 1
            pause 1.3
            linear 0.2 alpha 0
        parallel:
            easein 1.2 xpos 360

screen sfx_screen(what):
    fixed at sfx_inout:
        text what:
            font "BebasNeue-Regular.otf"
            color "#ffffff"
            size 50
        timer 2 action Hide("sfx_screen")


python early:

    from threading import Timer

    def parse_sfx(lex):
        # Default values
        clip = None
        subtitle = None

        # Based on what the user passed in, overwrite  the default values
        clip = lex.simple_expression().strip('"').strip("'")
        if clip.startswith('[') and clip.endswith(']'):
            clip = eval(clip)
        if not lex.eol():
            subtitle = lex.rest().strip('"').strip("'")

        # Wrap up the params and return it to renpy
        return clip, subtitle


    class show_sfx_txt:
        def __init__(self, txt):
            self.txt = txt

        def __call__(self):
            renpy.hide_screen("sfx_screen")
            renpy.show_screen("sfx_screen", self.txt)
            renpy.restart_interaction()

    def execute_sfx(o):
        clip, subtitle = o
        renpy.play(clip, "sound")
        if subtitle != None:
            if (type(clip) != unicode and '<silence ' and clip[0]):
                duration = float(clip[0][9:-1])
                #ui.timer(duration, show_sfx_txt(subtitle))
                Timer(duration, show_sfx_txt(subtitle), ()).start()
            else:
                show_sfx_txt(subtitle)()


    def lint_sfx(o):
        clip, subtitle = o
        try:
            renpy.play(clip, "sound")
        except:
            renpy.error("SFX not defined: %s" % clip)

        if substitle != None:
            tte = renpy.check_text_tags(subtitle)
            if tte:
                renpy.error(tte)

    renpy.register_statement("sfx", parse=parse_sfx, execute=execute_sfx, lint=lint_sfx)
