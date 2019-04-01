################################################################################
## Initialization
################################################################################

init offset = -1


############### NANO 2019 CODE ##############
image vr_buttons:
    "megan_ui/gui-vr-closed.png"
    on idle:
        "megan_ui/gui-vr-open.png" with Dissolve(1.0, alpha=True)
        pause 0.8
        "megan_ui/gui-vr-closed.png" with Dissolve(1.0, alpha=True)
        pause 0.8
        repeat
    on hover:
        "megan_ui/gui-vr-open.png" with Dissolve(0.3, alpha=True)
image realworld_buttons:
    "megan_ui/gui-realworld-closed.png"
    on idle:
        "megan_ui/gui-realworld-open.png" with Dissolve(1.0, alpha=True)
        pause 0.8
        "megan_ui/gui-realworld-closed.png" with Dissolve(1.0, alpha=True)
        pause 0.8
        repeat
    on hover:
        "megan_ui/gui-realworld-open.png" with Dissolve(0.3, alpha=True)

image rewind_buttons:
    "megan_ui/gui-rewind-closed.png"
    on idle:
        "megan_ui/gui-rewind-closed.png" with Dissolve(0.3, alpha=True)
    on hover:
        "megan_ui/gui-rewind-open.png" with Dissolve(0.3, alpha=True)
image autoplay_buttons:
    "megan_ui/gui-autoplay-closed.png"
    on idle:
        "megan_ui/gui-autoplay-closed.png" with Dissolve(0.3, alpha=True)
    on hover:
        "megan_ui/gui-autoplay-open.png" with Dissolve(0.3, alpha=True)
image skip_buttons:
    "megan_ui/gui-skip-closed.png"
    on idle:
        "megan_ui/gui-skip-closed.png" with Dissolve(0.3, alpha=True)
    on hover:
        "megan_ui/gui-skip-open.png" with Dissolve(0.3, alpha=True)
image history_buttons:
    "megan_ui/gui-history-closed.png"
    on idle:
        "megan_ui/gui-history-closed.png" with Dissolve(0.3, alpha=True)
    on hover:
        "megan_ui/gui-history-open.png" with Dissolve(0.3, alpha=True)


init python:
    import random
    def uisound():
        clips = [
            "sfx/button_click.ogg",
        ]
        return random.choice(clips)

    def uisoundin():
        clips = [
            "sfx/Swipe_1.ogg",
        ]
        return random.choice(clips)

    def uisoundout():
        clips = [
            "sfx/Swipe_2.ogg",
        ]
        return random.choice(clips)

screen in_game_menu():
    zorder 1

    button xpos 990 ypos 0:
        add "rewind_buttons"
        action [ Play("sound", uisound()), Rollback() ]
    button xpos 1100 ypos 0:
        add "autoplay_buttons"
        action [ Play("sound", uisound()), Preference("auto-forward", "toggle") ]
    button xpos 1210 ypos 0:
        add "skip_buttons"
        action Skip() alternate Skip(fast=True, confirm=True)
    button xpos 1320 ypos 0:
        add "history_buttons"
        action [ Play("sound", uisound()), ShowMenu('history') ]

    fixed xpos 110 ypos -1010:
        add "megan_ui/gui-email-list-background.png"
    fixed xpos 110 ypos 0:
        add "megan_ui/gui-email.png"
    mousearea:
        area (110, 0, 520, 90)
        hovered [
            Play("sound", uisoundin()),
            Show("in_game_email_content"),
            Show("in_game_email_button"),
            Hide("notify")
        ]
    mousearea:
        area (110, 0, 520, 790)
        unhovered [
            Play("sound", uisoundout()),
            Hide("in_game_email_content"),
            Hide("in_game_email"),
            Hide("in_game_email_button")
        ]

    fixed xpos 1470 ypos -420:
        add "megan_ui/gui-menu-background.png"
    fixed xpos 1470 ypos 0:
        add "megan_ui/gui-menu-closed.png"
    mousearea:
        area (1470, 0, 340, 90)
        hovered [
            Play("sound", uisoundin()),
            Show("in_game_menu_content"),
            Show("in_game_menu_button")
        ]
    mousearea:
        area (1470, 0, 340, 470)
        unhovered [
            Play("sound", uisoundout()),
            Hide("in_game_menu_content"),
            Hide("in_game_menu_button")
        ]

init python:
    maxlen = 18
    def shorten_email_text(intext):
        if len(intext) > maxlen + 1:
            return intext[:maxlen - 1] + '...'
        else:
            return intext
screen in_game_email_content():
    fixed xpos 110 ypos 0 at in_game_email_bg_showhide:
        add "megan_ui/gui-email-list-background.png"

        frame xpos 15 ypos 330:
            background None
            padding (0, 0, 20, 0)
            xsize 500
            ysize 730
            vpgrid:
                cols 1
                spacing 0
                mousewheel True
                draggable True
                scrollbars "vertical"
                side_xalign 0.5
                yinitial 1.0
                for ekey in visible_emails:
                    if ekey in read_emails:
                        $ email_color = "#39488D"
                    else:
                        $ email_color = "#06155a"
                    window:
                        ysize 130
                        $ email = all_emails[ekey]
                        add "megan_ui/gui-email-list-unclicked.png" ypos 20
                        imagebutton:
                            idle "megan_ui/gui-email-list-idle.png"
                            hover "megan_ui/gui-email-list-select.png"
                            action [ Play("sound", uisound()), Show("in_game_email", ekey=ekey) ]
                        fixed ypos 20:
                            text "FROM: ":
                                offset (41, 8)
                                font "BebasNeue-Regular.otf"
                                size 36
                                color email_color
                                outlines []
                            text shorten_email_text(email['from']):
                                offset (120, 14)
                                size 28
                                color email_color
                                outlines []
                            text "SUBJECT: ":
                                offset (10, 42)
                                font "BebasNeue-Regular.otf"
                                size 36
                                color email_color
                                outlines []
                            text shorten_email_text(email['title']):
                                offset (120, 49)
                                size 28
                                color email_color
                                outlines []

screen in_game_email_button():
    zorder 2
    fixed xpos 110 ypos 0 at in_game_email_button_showhide:
        add "megan_ui/gui-email-list-clicked.png"

transform in_game_email_button_showhide:
    on show:
        alpha 1 zoom 1 xpos 110
        linear 0.05 zoom 1.1 xpos 84
        linear 0.15 zoom 1 xpos 110
    on hide:
        alpha 1
        pause 0.2
        linear 0.1 alpha 0

transform in_game_email_bg_showhide:
    on show:
        alpha 1 ypos -1010
        pause 0.0
        linear .25 ypos -200
        linear .05 ypos -220
    on hide:
        ypos -220
        linear .1 ypos -200
        linear .2 ypos -1010
        alpha 0

screen in_game_email(ekey):
    if ekey not in read_emails:
        $ read_emails.append(ekey)

    zorder -1
    fixed xpos 650 ypos 130 at in_game_email_showhide:
        add "megan_ui/gui-email-body-background.png"
        $ email = all_emails[ekey]
        fixed pos (20, 40):
            text "FROM: ":
                offset (41, 8)
                font "BebasNeue-Regular.otf"
                size 36
                color "#39488D"
                outlines []
            text email['from']:
                offset (120, 14)
                size 28
                color "#39488D"
                outlines []
            text "SUBJECT: ":
                offset (10, 42)
                font "BebasNeue-Regular.otf"
                size 36
                color "#39488D"
                outlines []
            text email['title']:
                offset (120, 49)
                size 28
                color "#39488D"
                outlines []
        frame pos (20, 150):
            background None
            xsize 1000
            ysize 450
            padding (20, 20, 20, 20)
            text email['body']:
                size 28
                color "#39488D"
                outlines []
                first_indent 0

transform in_game_email_showhide:
    on show:
        alpha 0 xpos 110 ypos 130
        pause 0.0
        linear .25 alpha 1 xpos 670
        linear .05 xpos 650
    on hide:
        alpha 1 xpos 650 ypos 130
        linear .1 xpos 670
        linear .2 alpha 0 xpos 110

screen in_game_menu_content():
    fixed xpos 1470 ypos 0 at in_game_menu_bg_showhide:
        add "megan_ui/gui-menu-background.png"
        fixed ypos 130:
            imagebutton:
                idle "megan_ui/gui-gamemenu-save.png"
                hover "megan_ui/gui-gamemenu-select.png"
                action [ Play("sound", uisound()), ShowMenu("save") ]
            add "megan_ui/gui-gamemenu-save.png"
        fixed ypos 220:
            imagebutton:
                idle "megan_ui/gui-gamemenu-load.png"
                hover "megan_ui/gui-gamemenu-select.png"
                action [ Play("sound", uisound()), ShowMenu("load") ]
            add "megan_ui/gui-gamemenu-load.png"
        fixed ypos 310:
            imagebutton:
                idle "megan_ui/gui-gamemenu-settings.png"
                hover "megan_ui/gui-gamemenu-select.png"
                action [ Play("sound", uisound()), ShowMenu("custom_title_main_settings") ]
            add "megan_ui/gui-gamemenu-settings.png"
        fixed ypos 400:
            imagebutton:
                idle "megan_ui/gui-gamemenu-mainmenu.png"
                hover "megan_ui/gui-extrasmenu-mainmenu-select.png"
                action [ Play("sound", uisound()), MainMenu() ]
            add "megan_ui/gui-gamemenu-mainmenu.png"

screen in_game_menu_button():
    zorder 2
    fixed xpos 1470 ypos 0 at in_game_menu_button_showhide:
        add "megan_ui/gui-menu-clicked.png"

transform in_game_menu_button_showhide:
    on show:
        alpha 1 zoom 1 xpos 1470
        linear 0.05 zoom 1.1 xpos 1453
        linear 0.15 zoom 1 xpos 1470
    on hide:
        alpha 1
        pause 0.2
        linear 0.1 alpha 0

transform in_game_menu_bg_showhide:
    on show:
        alpha 1 ypos -420
        pause 0.0
        linear .25 ypos -20
        linear .05 ypos -40
    on hide:
        ypos -40
        linear .1 ypos -20
        linear .2 ypos -420
        alpha 0

screen in_game_entervr():
    zorder 10
    button xpos 1790:
        add "vr_buttons"
        action [
            Play("sound", "sfx/VR-On.ogg"),
            Hide("in_game_entervr"),
            Show("in_game_entervr_showing")
        ]
        at in_game_entervrbutton_showhide

screen in_game_entervr_showing():
    zorder 10
    fixed xpos 1790:
        add "megan_ui/gui-vr-closed.png"
        at in_game_entervr_showhide

        timer 1.5 action Return
        timer 1.5 action Hide("in_game_entervr_showing")

screen in_game_exitvr():
    zorder 10
    button xpos -1930:
        add "realworld_buttons"
        action [
            Play("sound", "sfx/VR-Off.ogg"),
            Hide("in_game_exitvr"),
            Show("in_game_exitvr_showing")
        ]
        at in_game_exitvrbutton_showhide

screen in_game_exitvr_showing():
    zorder 10
    fixed xpos -1930:
        add "megan_ui/gui-realworld-closed.png"
        at in_game_exitvr_showhide

        timer 1.5 action Return
        timer 1.5 action Hide("in_game_exitvr_showing")

transform in_game_entervrbutton_showhide:
    on show:
        alpha 1 xpos 1920
        linear 0.5 xpos 1790

transform in_game_exitvrbutton_showhide:
    on show:
        alpha 1 xpos -2050
        linear 0.5 xpos -1930

transform in_game_entervr_showhide:
    on show:
        alpha 1 xpos 1790
        linear 0.25 xpos 1830
        ease 1.0 xpos -130
    on hide:
        alpha 1
        linear 1.0 alpha 0

transform in_game_exitvr_showhide:
    on show:
        alpha 1 xpos -1930
        linear 0.25 xpos -1970
        ease 1.0 xpos 0
    on hide:
        alpha 1
        linear 1.0 alpha 0

transform pulse:
    zoom 1
    linear 0.05 zoom 1.1
    linear 0.25 zoom 1.0

transform fade_inout(duration=0.5):
    on show:
        alpha 0
        linear duration alpha 1
    on hide:
        linear duration alpha 0

init python:
    import time

    mc_name = ""

    def ChangedNameInput(name):
        global mc_name

        mc_name = name.strip()
        if (mc_name != ""):
            if renpy.get_screen("thumbprint_active") == None:
                renpy.show_screen("thumbprint_active")
                renpy.restart_interaction()
        else:
            if renpy.get_screen("thumbprint_active") != None:
                renpy.hide_screen("thumbprint_active")
                renpy.restart_interaction()

    def ClickedLogin():
        global mc_name

        if mc_name != "":
            renpy.play("sfx/Scanner.ogg", "sound")
            renpy.hide_screen("startgame_login")
            renpy.show_screen("thumbprint_scanning")
            renpy.show_screen("thumbprint_line")
            ui.timer(2.0, LoginToLoading)

    def LoginToLoading():
        renpy.play("sfx/Chime - DX EP.ogg", "sound")
        renpy.hide_screen("thumbprint_scanning")
        renpy.hide_screen("thumbprint_line")
        if relogin:
            renpy.jump("rw4_continue")
        else:
            renpy.jump("start2")

image authenticate_loading_bg:
    "megan_ui/authenticate-loadscreen1.jpg" with Dissolve(1.0)
    1.0
    "megan_ui/authenticate-loadscreen2.jpg" with Dissolve(1.0)
    1.0
    repeat

image thumbprint_glowing:
    "megan_ui/thumbprint-glow.png" with Dissolve(1.0)
    1.0
    "megan_ui/thumbprint-default.png" with Dissolve(1.0)
    1.0
    repeat

image authenticate_glowing:
    "megan_ui/authenticate-glow.png" with Dissolve(1.0)
    1.0
    "megan_ui/authenticate-default.png" with Dissolve(1.0)
    1.0
    repeat

image line_glowing:
    "megan_ui/line-scan.png" with Dissolve(0.4)
    0.4
    "megan_ui/line-default.png" with Dissolve(0.4)
    0.4
    repeat

transform line_scanning:
    pos (760, 740)
    linear 1.0 pos (760, 520)
    linear 1.0 pos (760, 740)
    repeat

screen startgame_login():
    tag login
    fixed at fade_inout:
        add "megan_ui/authenticate-background.jpg"

        fixed pos (540, 200):
            add "megan_ui/authenticate-voice-mail-subs-background.png"
            imagebutton:
                idle "megan_ui/authenticate-voice-mail-subs-off.png"
                hover "megan_ui/authenticate-voice-mail-subs-on.png"
                selected_idle "megan_ui/authenticate-voice-mail-subs-on.png"
                selected_hover "megan_ui/authenticate-voice-mail-subs-on.png"
                action [ Play("sound", uisound()), ToggleVariable("persistent.subtitle") ]

        fixed pos (540, 400):
            add "megan_ui/authenticate-name-background.png"
            if relogin:
                text mc_name pos (172, 242):
                    font "Arial Bold.ttf"
                    color "#ceebf5"
                    size 40
            else:
                input pos (172, 242):
                    default ""
                    length 12
                    font "Arial Bold.ttf"
                    color "#ceebf5"
                    size 40
                    changed ChangedNameInput

        fixed pos (760, 740):
            add "megan_ui/thumbprint-default.png"

screen startgame_logging_in():
    tag login
    fixed at fade_inout:
        add "authenticate_loading_bg"

layeredimage thumbprint_authenticate:
    group thumbprint:
        attribute glowing default:
            "thumbprint_glowing"
        attribute onhover:
            "megan_ui/thumbprint-glow.png"

    group authenticate:
        attribute glowing default:
            "authenticate_glowing"
        attribute onhover:
            "megan_ui/authenticate-glow.png"

screen thumbprint_active():
    tag thumbprint
    if relogin:
        add "megan_ui/authenticate-background.jpg"
    imagebutton pos (760, 740) at fade_inout:
        idle "thumbprint_authenticate"
        hover "thumbprint_authenticate onhover"
        action Function(ClickedLogin)
    key "K_RETURN" action Function(ClickedLogin)

screen thumbprint_scanning():
    tag thumbprint
    if relogin:
        add "megan_ui/authenticate-background.jpg"
    fixed pos (760, 740) at fade_inout:
        add "megan_ui/thumbprint-scan.png"

screen thumbprint_line():
    fixed at line_scanning:
        add "line_glowing"




label main_menu:
    $ in_main_menu = True
    play music "music/Main Menu.ogg" fadein 3.0 fadeout 3.0
    call screen custom_title_center with fade

screen custom_mainmenu_buttons_center():
    fixed:
        add "megan_ui/gui-mainmenu-background.png"

        imagebutton pos (20, 30): # Play
            idle "megan_ui/gui-gamemenu-idle.png"
            hover "megan_ui/gui-gamemenu-select.png"
            action [ Play("sound", uisound()), Start() ]

        imagebutton pos (20, 120): # Load
            idle "megan_ui/gui-gamemenu-idle.png"
            hover "megan_ui/gui-gamemenu-select.png"
            action [ Play("sound", uisound()), Show("custom_title_center2left"), Show("load") ]

        imagebutton pos (20, 210): # Settings
            idle "megan_ui/gui-gamemenu-idle.png"
            hover "megan_ui/gui-gamemenu-select.png"
            action [ Play("sound", uisound()), Show("custom_title_center2left"), Show("custom_title_main_settings") ]

        imagebutton pos (20, 300): # Extras
            idle "megan_ui/gui-gamemenu-idle.png"
            hover "megan_ui/gui-gamemenu-select.png"
            action [ Play("sound", uisound()), Show("custom_title_center2right") ]

        imagebutton pos (20, 390): # Quit
            idle "megan_ui/gui-gamemenu-idle.png"
            hover "megan_ui/gui-gamemenu-mainmenu-select.png"
            action [ Play("sound", uisound()), Quit() ]

        add "megan_ui/gui-mainmenu-text.png"

screen custom_mainmenu_buttons_left():
    fixed:
        add "megan_ui/gui-mainmenu-background.png"

        imagebutton pos (20, 30): # Play
            idle "megan_ui/gui-gamemenu-idle.png"
            hover "megan_ui/gui-gamemenu-select.png"
            action [ Play("sound", uisound()), Start() ]

        imagebutton pos (20, 120): # Load
            idle "megan_ui/gui-gamemenu-idle.png"
            hover "megan_ui/gui-gamemenu-select.png"
            action [ Play("sound", uisound()), Show("load") ]

        imagebutton pos (20, 210): # Settings
            idle "megan_ui/gui-gamemenu-idle.png"
            hover "megan_ui/gui-gamemenu-select.png"
            action [ Play("sound", uisound()), Show("custom_title_main_settings")]

        imagebutton pos (20, 300): # Extras
            idle "megan_ui/gui-gamemenu-idle.png"
            hover "megan_ui/gui-gamemenu-select.png"
            action [ Play("sound", uisound()), Show("custom_title_left2right"), Hide("custom_title_main") ]

        imagebutton pos (20, 390): # Quit
            idle "megan_ui/gui-gamemenu-idle.png"
            hover "megan_ui/gui-gamemenu-mainmenu-select.png"
            action [ Play("sound", uisound()), Quit() ]

        add "megan_ui/gui-mainmenu-text.png"

screen custom_mainmenu_buttons_right():
    fixed:
        add "megan_ui/gui-extrasmenu-background.png"

        imagebutton pos (20, 30): # Gallery
            idle "megan_ui/gui-gamemenu-idle.png"
            hover "megan_ui/gui-gamemenu-select.png"
            action [ Play("sound", uisound()), Show("custom_title_extras_gallery"), Show("custom_title_extras_hide") ]

        imagebutton pos (20, 120): # Music box
            idle "megan_ui/gui-gamemenu-idle.png"
            hover "megan_ui/gui-gamemenu-select.png"
            action [ Play("sound", uisound()), Show("custom_title_extras_musicbox") ]

        imagebutton pos (20, 210): # Credits
            idle "megan_ui/gui-gamemenu-idle.png"
            hover "megan_ui/gui-gamemenu-select.png"
            action [ Play("sound", uisound()), Show("credits") ]

        imagebutton pos (20, 300): # Back
            idle "megan_ui/gui-gamemenu-idle.png"
            hover "megan_ui/gui-extrasmenu-mainmenu-select.png"
            action [ Play("sound", uisound()), Show("custom_title_right2center"), Hide("custom_title_extras") ]

        add "megan_ui/gui-extrasmenu-text.png"

screen custom_title_center():
    tag custom_title
    fixed:
        add "sunsettitle"

    fixed pos (420, 50):
        add "gui/this was for you Logo.png"

    fixed pos (770, 510):
        fixed at main_menu_center:
            use custom_mainmenu_buttons_center

screen custom_title_center2left():
    tag custom_title
    fixed:
        add "sunsettitle"

    fixed pos (420, 50):
        add "gui/this was for you Logo.png"

    fixed pos (770, 510):
        fixed at main_menu_center2left:
            use custom_mainmenu_buttons_left

screen custom_title_center2right():
    tag custom_title
    fixed:
        add "sunsettitle"

    fixed pos (420, 50):
        add "gui/this was for you Logo.png"

    fixed pos (770, 600):
        fixed at main_menu_center2right:
            use custom_mainmenu_buttons_right

screen custom_title_right2center():
    tag custom_title
    fixed:
        add "sunsettitle"

    fixed pos (420, 50):
        add "gui/this was for you Logo.png"

    fixed pos (770, 510):
        fixed at main_menu_right2center:
            use custom_mainmenu_buttons_center

screen custom_title_left2center():
    tag custom_title
    fixed:
        add "sunsettitle"

    fixed pos (420, 50):
        add "gui/this was for you Logo.png"

    fixed pos (770, 510):
        fixed at main_menu_left2center:
            use custom_mainmenu_buttons_center

screen custom_title_left2right():
    tag custom_title
    fixed:
        add "sunsettitle"

    fixed pos (420, 50):
        add "gui/this was for you Logo.png"

    fixed pos (770, 600):
        fixed at main_menu_left2right:
            use custom_mainmenu_buttons_right

screen custom_title_extras_hide():
    tag custom_title
    fixed:
        add "sunsettitle"

    fixed pos (420, 50):
        add "gui/this was for you Logo.png"

transform main_menu_center:
    easein 0.2 alpha 1 xpos 0

transform main_menu_center2left:
    easein 0.2 alpha 1 xpos -710

transform main_menu_center2right:
    easein 0.2 alpha 1 xpos 710

transform main_menu_right2center:
    xpos 710
    easein 0.2 alpha 1 xpos 0

transform main_menu_left2center:
    xpos -710
    easein 0.2 alpha 1 xpos 0

transform main_menu_left2right:
    xpos -710
    easein 0.2 alpha 1 xpos 710

screen save():
    tag custom_title_main
    use custom_title_main_saveload("Save")

screen load():
    tag custom_title_main
    use custom_title_main_saveload("Load")

screen custom_title_main_saveload(title):
    frame align (0.5, 0.5) at fade_inout(0.2):
        background "megan_ui/gui-settings-background.png"
        xsize 920
        ysize 1000
        fixed pos (30, 10):
            text title:
                font "BebasNeue-Regular.otf"
                size 60
                color "#36428A"
                outlines []
                #outlines [ (absolute(6), "#CEEBF5", absolute(0), absolute(0)) ]
        frame ypos 90:
            background None
            padding (0, 0, 0, 0)
            xsize 850
            ysize 800
            vpgrid xoffset -30:
                cols 1
                spacing 10
                mousewheel True
                draggable True
                scrollbars "vertical"
                side_xalign 0.5
                for slot in range(1, 10):
                    frame:
                        background None
                        padding (30,0,20,0)
                        xsize 790
                        ysize 140
                        imagebutton:
                            idle Frame("megan_ui/save_slot_frame.png", Borders(30, 30, 30, 30))
                            hover Frame("megan_ui/save_slot_frame_hover.png", Borders(30, 30, 30, 30))
                            action [ Play("sound", uisound()), FileAction(slot) ]
                        frame:
                            background None
                            xsize 790
                            ysize 140
                            padding (20, 10, 20, 10)
                            right_margin 10
                            add FileScreenshot(slot) xalign 1.0 zoom 0.55 crop (90, 0, 220, 220)
                            text "[slot]. " + FileSaveName(slot):
                                font "BebasNeue-Regular.otf"
                                size 50
                                color "#36428A"
                                outlines []
                            text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")) ypos 60:
                                font "BebasNeue-Regular.otf"
                                size 50
                                color "#36428A"
                                outlines []
        fixed pos (650, 910):
            imagebutton offset (-40, -5):
                idle "megan_ui/gui-back-idle.png"
                hover "megan_ui/gui-back-select.png"
                if in_main_menu:
                    action [ Play("sound", uisound()), Show("custom_title_left2center"), Hide("custom_title_main") ]
                else:
                    action [ Play("sound", uisound()), Return() ]
            text "Back":
                font "BebasNeue-Regular.otf"
                size 60
                color "#36428A"
                outlines []

screen custom_title_main_settings():
    tag custom_title_main

    frame align (0.5, 0.5) at fade_inout(0.2):
        background "megan_ui/gui-settings-background.png"
        xsize 920
        ysize 1000

        fixed pos (30, 10):
            text "Settings":
                font "BebasNeue-Regular.otf"
                size 60
                color "#36428A"
                outlines []

            if config.has_music or config.has_sound or config.has_voice:
                null height gui.pref_spacing

                textbutton _("Mute All"):
                    action Preference("all mute", "toggle")
                    style "mute_all_button"
                    xalign 0.3

            if config.has_music or config.has_sound or config.has_voice:
                null height gui.pref_spacing

                textbutton _("Subtitles"):
                    action ToggleVariable("persistent.subtitle")
                    style "mute_all_button"
                    xalign 0.65

        hbox:
            ypos 120
            xpos 30
            box_wrap True
            style_prefix "slider"

            vbox:
                spacing -5

                text "Text Speed":
                    font "BebasNeue-Regular.otf"
                    size 40
                    color "#36428A"
                    outlines []

                bar value Preference("text speed"):
                    xalign 1.5 yoffset -65

                text "Autoplay Speed":
                    font "BebasNeue-Regular.otf"
                    size 40
                    color "#36428A"
                    outlines []

                bar value Preference("auto-forward time"):
                    xalign 1.5 yoffset -65

                if config.has_music:

                    text "Music Volume":
                        font "BebasNeue-Regular.otf"
                        size 40
                        color "#36428A"
                        outlines []

                    bar value Preference("music volume"):
                        xalign 1.5 yoffset -65

                if config.has_sound:
                    text "Sound Volume":
                        font "BebasNeue-Regular.otf"
                        size 40
                        color "#36428A"
                        outlines []

                    bar value Preference("sound volume"):
                        xalign 1.5 yoffset -65

                    if config.sample_sound:
                        textbutton _("Test") action Play("sound", config.sample_sound)


                if config.has_voice:
                    text "Voice Volume":
                        font "BebasNeue-Regular.otf"
                        size 40
                        color "#36428A"
                        outlines []

                    bar value Preference("voice volume"):
                        xalign 1.5 yoffset -65

                    if config.sample_voice:
                        textbutton _("Test") action Play("voice", config.sample_voice)

        hbox:
            ypos 640
            xpos 30
            box_wrap True

            vbox:
                style_prefix "check"
                text "Skip":
                    font "BebasNeue-Regular.otf"
                    size 50
                    color "#36428A"
                    outlines []
                textbutton _("Unseen Text") action [ Play("sound", uisound()), Preference("skip", "toggle") ]
                textbutton _("After Choices") action [ Play("sound", uisound()), Preference("after choices", "toggle") ]
                textbutton _("Transitions") action [ Play("sound", uisound()), InvertSelected(Preference("transitions", "toggle")) ]

            if renpy.variant("pc"):

                vbox:
                    style_prefix "check"
                    text "Display":
                        font "BebasNeue-Regular.otf"
                        size 50
                        color "#36428A"
                        outlines []
                    textbutton _("Window") action [ Play("sound", uisound()), Preference("display", "window") ]

                    textbutton _("Fullscreen") action [ Play("sound", uisound()), Preference("display", "fullscreen") ]

        fixed pos (650, 910):
            imagebutton offset (-40, -5):
                idle "megan_ui/gui-back-idle.png"
                hover "megan_ui/gui-back-select.png"
                if in_main_menu:
                    action [ Play("sound", uisound()), Show("custom_title_left2center"), Hide("custom_title_main") ]
                else:
                    action [ Play("sound", uisound()), Return() ]
            text "Back":
                font "BebasNeue-Regular.otf"
                size 60
                color "#36428A"
                outlines []

screen custom_title_extras_gallery():
    tag custom_title_extras
    use gallery

screen custom_title_extras_musicbox():
    tag custom_title_extras
    fixed:
        text "Music box Screen"

screen history():
    tag custom_title_main

    ## Avoid predicting this screen, as it can be very large.
    predict False

    add "megan_ui/gui-skipping-background.png"
    frame:
        background None
        padding (200, 120, 200, 140)
        vpgrid:
            cols 1
            mousewheel True
            draggable True
            scrollbars "vertical"
            side_xalign 0.5
            yinitial 1.0
            for h in _history_list:
                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)

                fixed:
                    yfit True
                    label what:
                        xfill True
                        ysize 120
                        text_text_align 0.5
                        text_xalign 0.5
                        text_font "Arial Bold.ttf"
                        if h.who and "color" in h.what_args:
                            text_color h.what_args["color"]
                        substitute False

            if not _history_list:
                label _("The dialogue history is empty.")
    fixed pos (1560, 960):
        imagebutton offset (-20, 0):
            idle "megan_ui/gui-back-idle.png"
            hover "megan_ui/gui-back-select.png"
            action [ Play("sound", uisound()), Return() ]
        add "megan_ui/gui-history-back.png"

transform chapter_inout:
    on show:
        alpha 0
        linear 1.5 alpha 1
    on hide:
        linear 1.5 alpha 0

screen chapter_announce():
    frame align (0.5, 0.4) at chapter_inout:
        background None
        padding (100,100,100,100)
        text save_name:
            align (0.5, 0.5)
            text_align 0.5
            font "BebasNeue-Regular.otf"
            size 100
    timer 2 action Hide("chapter_announce")
