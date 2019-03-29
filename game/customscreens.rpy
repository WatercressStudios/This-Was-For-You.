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


screen in_game_menu():
    zorder 1

    button xpos 990 ypos 0:
        add "rewind_buttons"
        action Rollback()
    button xpos 1100 ypos 0:
        add "autoplay_buttons"
        action Preference("auto-forward", "toggle")
    button xpos 1210 ypos 0:
        add "skip_buttons"
        action Skip() alternate Skip(fast=True, confirm=True)
    button xpos 1320 ypos 0:
        add "history_buttons"
        action ShowMenu('history')

    fixed xpos 110 ypos -1010:
        add "megan_ui/gui-email-list-background.png"
    fixed xpos 110 ypos 0:
        add "megan_ui/gui-email.png"
    mousearea:
        area (110, 0, 520, 90)
        hovered [
            Show("in_game_email_content"),
            Show("in_game_email_button"),
            Hide("notify")
        ]
    mousearea:
        area (110, 0, 520, 790)
        unhovered [
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
            Show("in_game_menu_content"),
            Show("in_game_menu_button")
        ]
    mousearea:
        area (1470, 0, 340, 470)
        unhovered [
            Hide("in_game_menu_content"),
            Hide("in_game_menu_button")
        ]

screen in_game_email_content():
    fixed xpos 110 ypos 0 at in_game_email_bg_showhide:
        add "megan_ui/gui-email-list-background.png"
        fixed xpos 480 ypos 330:
            add "megan_ui/gui-email-list-scroll-background.png"
        button xpos 20 ypos 330:
            add "megan_ui/gui-email-list-unclicked.png"
            text "Click here to show email"
            action Show("in_game_email")
        button xpos 20 ypos 460:
            add "megan_ui/gui-email-list-unclicked.png"
            text "Click here to hide email"
            action Hide("in_game_email")
        # imagebutton ypos 220:
        #     idle "megan_ui/gui-gamemenu-load.png"
        #     action Null
        # imagebutton ypos 310:
        #     idle "megan_ui/gui-gamemenu-settings.png"
        #     action Null
        # imagebutton ypos 400:
        #     idle "megan_ui/gui-gamemenu-mainmenu.png"
        #     action Null

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

screen in_game_email():
    zorder -1
    fixed xpos 650 ypos 130 at in_game_email_showhide:
        add "megan_ui/gui-email-body-background.png"

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
        imagebutton ypos 130:
            idle "megan_ui/gui-gamemenu-save.png"
            action ShowMenu("save")
        imagebutton ypos 220:
            idle "megan_ui/gui-gamemenu-load.png"
            action ShowMenu("load")
        imagebutton ypos 310:
            idle "megan_ui/gui-gamemenu-settings.png"
            action Null
        imagebutton ypos 400:
            idle "megan_ui/gui-gamemenu-mainmenu.png"
            action MainMenu()

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
    button xpos 1810:
        add "vr_buttons"
        action [
            Hide("in_game_entervr"),
            Show("in_game_entervr_showing")
        ]
        at in_game_entervrbutton_showhide

screen in_game_entervr_showing():
    zorder 10
    fixed xpos 1810:
        add "megan_ui/gui-vr-closed.png"
        at in_game_entervr_showhide

screen in_game_exitvr():
    zorder 10
    button xpos -1920:
        add "realworld_buttons"
        action [
            Hide("in_game_exitvr"),
            Show("in_game_exitvr_showing")
        ]
        at in_game_exitvrbutton_showhide

screen in_game_exitvr_showing():
    zorder 10
    fixed xpos -1920:
        add "megan_ui/gui-realworld-closed.png"
        at in_game_exitvr_showhide

transform in_game_entervrbutton_showhide:
    on show:
        alpha 1 xpos 1920
        linear 0.5 xpos 1810

transform in_game_exitvrbutton_showhide:
    on show:
        alpha 1 xpos -2050
        linear 0.5 xpos -1920

transform in_game_entervr_showhide:
    on show:
        alpha 1 xpos 1810
        linear 0.25 xpos 1850
        ease 1.0 xpos -130
    on hide:
        alpha 1
        linear 1.0 alpha 0

transform in_game_exitvr_showhide:
    on show:
        alpha 1 xpos -1920
        linear 0.25 xpos -1960
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
            renpy.hide_screen("startgame_login")
            renpy.show_screen("thumbprint_scanning")
            renpy.show_screen("thumbprint_line")
            ui.timer(2.0, LoginToLoading)

    def LoginToLoading():
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
                hover "megan_ui/authenticate-voice-mail-subs-off.png"
                selected_idle "megan_ui/authenticate-voice-mail-subs-on.png"
                selected_hover "megan_ui/authenticate-voice-mail-subs-on.png"
                action ToggleVariable("persistent.subtitle")

        fixed pos (540, 400):
            add "megan_ui/authenticate-name-background.png"
            if relogin:
                text mc_name pos (172, 240):
                    font "BebasNeue-Regular.otf"
                    color "#ceebf5"
                    size 50
            else:
                input pos (172, 240):
                    default ""
                    length 12
                    font "BebasNeue-Regular.otf"
                    color "#ceebf5"
                    size 50
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
    call screen custom_title_center with fade

screen custom_mainmenu_buttons_center():
    fixed:
        add "megan_ui/gui-mainmenu-background.png"

        imagebutton pos (20, 30): # Play
            idle "megan_ui/gui-gamemenu-idle.png"
            hover "megan_ui/gui-gamemenu-select.png"
            action Start()

        imagebutton pos (20, 120): # Load
            idle "megan_ui/gui-gamemenu-idle.png"
            hover "megan_ui/gui-gamemenu-select.png"
            action [ Show("custom_title_center2left"), Show("load") ]

        imagebutton pos (20, 210): # Settings
            idle "megan_ui/gui-gamemenu-idle.png"
            hover "megan_ui/gui-gamemenu-select.png"
            action [ Show("custom_title_center2left"), Show("custom_title_main_settings") ]

        imagebutton pos (20, 300): # Extras
            idle "megan_ui/gui-gamemenu-idle.png"
            hover "megan_ui/gui-gamemenu-select.png"
            action [ Show("custom_title_center2right") ]

        imagebutton pos (20, 390): # Quit
            idle "megan_ui/gui-gamemenu-idle.png"
            hover "megan_ui/gui-gamemenu-mainmenu-select.png"
            action Quit()

        add "megan_ui/gui-mainmenu-text.png"

screen custom_mainmenu_buttons_left():
    fixed:
        add "megan_ui/gui-mainmenu-background.png"

        imagebutton pos (20, 30): # Play
            idle "megan_ui/gui-gamemenu-idle.png"
            hover "megan_ui/gui-gamemenu-select.png"
            action Start()

        imagebutton pos (20, 120): # Load
            idle "megan_ui/gui-gamemenu-idle.png"
            hover "megan_ui/gui-gamemenu-select.png"
            action Show("load")

        imagebutton pos (20, 210): # Settings
            idle "megan_ui/gui-gamemenu-idle.png"
            hover "megan_ui/gui-gamemenu-select.png"
            action Show("custom_title_main_settings")

        imagebutton pos (20, 300): # Extras
            idle "megan_ui/gui-gamemenu-idle.png"
            hover "megan_ui/gui-gamemenu-select.png"
            action [ Show("custom_title_left2right"), Hide("custom_title_main") ]

        imagebutton pos (20, 390): # Quit
            idle "megan_ui/gui-gamemenu-idle.png"
            hover "megan_ui/gui-gamemenu-mainmenu-select.png"
            action Quit()

        add "megan_ui/gui-mainmenu-text.png"

screen custom_mainmenu_buttons_right():
    fixed:
        add "megan_ui/gui-extrasmenu-background.png"

        imagebutton pos (20, 30): # Gallery
            idle "megan_ui/gui-gamemenu-idle.png"
            hover "megan_ui/gui-gamemenu-select.png"
            action Show("custom_title_extras_gallery")

        imagebutton pos (20, 120): # Music box
            idle "megan_ui/gui-gamemenu-idle.png"
            hover "megan_ui/gui-gamemenu-select.png"
            action Show("custom_title_extras_musicbox")

        imagebutton pos (20, 210): # Credits
            idle "megan_ui/gui-gamemenu-idle.png"
            hover "megan_ui/gui-gamemenu-select.png"
            action Show("custom_title_extras_credits")

        imagebutton pos (20, 300): # Back
            idle "megan_ui/gui-gamemenu-idle.png"
            hover "megan_ui/gui-extrasmenu-mainmenu-select.png"
            action [ Show("custom_title_right2center"), Hide("custom_title_extras") ]

        add "megan_ui/gui-extrasmenu-text.png"

screen custom_title_center():
    tag custom_title
    fixed:
        add "sunsettitle"

    fixed pos (770, 510):
        fixed at main_menu_center:
            use custom_mainmenu_buttons_center

screen custom_title_center2left():
    tag custom_title
    fixed:
        add "sunsettitle"

    fixed pos (770, 510):
        fixed at main_menu_center2left:
            use custom_mainmenu_buttons_left

screen custom_title_center2right():
    tag custom_title
    fixed:
        add "sunsettitle"

    fixed pos (770, 600):
        fixed at main_menu_center2right:
            use custom_mainmenu_buttons_right

screen custom_title_right2center():
    tag custom_title
    fixed:
        add "sunsettitle"

    fixed pos (770, 510):
        fixed at main_menu_right2center:
            use custom_mainmenu_buttons_center

screen custom_title_left2center():
    tag custom_title
    fixed:
        add "sunsettitle"

    fixed pos (770, 510):
        fixed at main_menu_left2center:
            use custom_mainmenu_buttons_center

screen custom_title_left2right():
    tag custom_title
    fixed:
        add "sunsettitle"

    fixed pos (770, 600):
        fixed at main_menu_left2right:
            use custom_mainmenu_buttons_right

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
        background "megan_ui/gui-save-background.png"
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
            xsize 920
            ysize 800
            vpgrid xoffset -50:
                cols 1
                spacing 10
                mousewheel True
                draggable True
                scrollbars "vertical"
                side_xalign 0.5
                for slot in range(1, 10):
                    frame:
                        background None
                        padding (10,0,10,0)
                        xsize 790
                        ysize 140
                        imagebutton:
                            idle Frame("megan_ui/save_slot_frame.png", Borders(30, 30, 30, 30))
                            hover Frame("megan_ui/save_slot_frame_hover.png", Borders(30, 30, 30, 30))
                            action FileAction(slot)
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
            imagebutton offset (-185, -5):
                idle "megan_ui/gui-gamemenu-idle.png"
                hover "megan_ui/gui-gamemenu-mainmenu-select.png"
                if in_main_menu:
                    action [ Show("custom_title_left2center"), Hide("custom_title_main") ]
                else:
                    action Return()
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

        hbox:
            ypos 90
            xpos 60
            box_wrap True

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"

            if renpy.variant("pc"):

                vbox:
                    style_prefix "check"
                    label _("Display")
                    textbutton _("Window") action Preference("display", "window")
                    textbutton _("Fullscreen") action Preference("display", "fullscreen")

            vbox:
                style_prefix "check"
                label _("Skip")
                textbutton _("Unseen Text") action Preference("skip", "toggle")
                textbutton _("After Choices") action Preference("after choices", "toggle")
                textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))
