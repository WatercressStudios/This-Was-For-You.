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

    button xpos 1030 ypos 0:
        add "rewind_buttons"
        action Null
    button xpos 1140 ypos 0:
        add "autoplay_buttons"
        action Null
    button xpos 1250 ypos 0:
        add "skip_buttons"
        action Null
    button xpos 1360 ypos 0:
        add "history_buttons"
        action Null

    fixed xpos 110 ypos -1010:
        add "megan_ui/gui-email-list-background.png"
    fixed xpos 110 ypos 0:
        add "megan_ui/gui-email.png"
    mousearea:
        area (110, 0, 520, 90)
        hovered [Show("in_game_email_content"), Show("in_game_email_button")]
    mousearea:
        area (110, 0, 520, 790)
        unhovered [Hide("in_game_email_content"), Hide("in_game_email"), Hide("in_game_email_button")]

    fixed xpos 1470 ypos -420:
        add "megan_ui/gui-menu-background.png"
    fixed xpos 1470 ypos 0:
        add "megan_ui/gui-menu-closed.png"
    mousearea:
        area (1470, 0, 340, 90)
        hovered [Show("in_game_menu_content"), Show("in_game_menu_button")]
    mousearea:
        area (1470, 0, 340, 470)
        unhovered [Hide("in_game_menu_content"), Hide("in_game_menu_button")]

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
            action Null
        imagebutton ypos 220:
            idle "megan_ui/gui-gamemenu-load.png"
            action Null
        imagebutton ypos 310:
            idle "megan_ui/gui-gamemenu-settings.png"
            action Null
        imagebutton ypos 400:
            idle "megan_ui/gui-gamemenu-mainmenu.png"
            action Null

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
        action [Hide("in_game_entervr"), Show("in_game_entervr_showing")]
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
        action [Hide("in_game_exitvr"), Show("in_game_exitvr_showing")]
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
