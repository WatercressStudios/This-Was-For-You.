#
# Part 3 of UI tutorial, Animation and Trigger Events.
# At the top of the "start" label, "jump" into the label below to test.
#

label part3_label:
    call screen part3_screen_buttonactions

label part3_label_continue:
    "Click to continue."

transform test_fade_showhide:
    on show:
        alpha 0
        linear 0.5 alpha 1
    on hide:
        alpha 1
        linear 0.5 alpha 0

transform test_slideright_showhide:
    on show:
        alpha 0 xalign 0.7
        linear 0.20 alpha 1 xalign 0.95
        linear 0.05 xalign 0.9
    on hide:
        alpha 1 xalign 0.9
        linear 0.1 xalign 0.95
        linear 0.15 alpha 0 xalign 0.7

transform test_zoom_idlehover:
    on idle:
        zoom 1.1
        linear 0.1 zoom 1.12
        linear 0.15 zoom 1
    on hover:
        zoom 1
        linear 0.2 zoom 1.12
        linear 0.05 zoom 1.1

screen part3_screen_buttonactions():
    frame:
        at test_fade_showhide
        xalign 0.2 yalign 0.5
        padding (50, 50)
        vbox:
            spacing 5
            text "Button Action Test"
            textbutton "Click to show another screen.":
                at test_zoom_idlehover
                action Show('part3_screen_anotherscreen')
            textbutton "Click to hide another screen.":
                at test_zoom_idlehover
                action Hide('part3_screen_anotherscreen')
            hbox:
                spacing 3
                text "Hide everything:"
                textbutton "Click to hide all screens.":
                    at test_zoom_idlehover
                    action [
                        Hide('part3_screen_buttonactions'),
                        Hide('part3_screen_anotherscreen'),
                        Jump('part3_label_continue')
                    ]
            text "Text at the bottom"

screen part3_screen_anotherscreen():
    frame:
        at test_slideright_showhide
        yalign 0.5
        padding (200, 200)
        text "Another screen!"
