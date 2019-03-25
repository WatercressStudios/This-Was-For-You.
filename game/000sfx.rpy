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


python early:

    def parse_sfx(lex):
        # Default values
        clip = None
        subtitle = None

        # Based on what the user passed in, overwrite  the default values
        clip = lex.simple_expression().strip('"').strip("'")
        if not lex.eol():
            subtitle = lex.rest().strip('"').strip("'")

        # Wrap up the params and return it to renpy
        return clip, subtitle


    def execute_sfx(o):
        clip, subtitle = o
        renpy.play(clip, "sound")
        if subtitle != None:
            renpy.hide_screen("sfx_screen")
            renpy.show_screen("sfx_screen", subtitle)
            renpy.restart_interaction()


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
