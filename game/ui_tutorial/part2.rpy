#
# Part 2 of UI tutorial, Screen Hierarchy and Button Actions.
# At the top of the "start" label, "jump" into the label below to test.
#

label part2_label:
    show screen part2_screen
    "Click to continue."
    hide screen part2_screen
    call screen part2_screen_buttonactions

label part2_label_continue:
    "Click to continue."

screen part2_screen():
    frame:
        xalign 0.5 yalign 0.5
        padding (50, 50)
        vbox:
            spacing 5
            text "Text at the top"
            textbutton "First button.":
                action Null
            textbutton "Second button.":
                action Null
            hbox:
                spacing 3
                text "Button label:"
                textbutton "Third button.":
                    action Null
            text "Text at the bottom"

screen part2_screen_buttonactions():
    frame:
        xalign 0.2 yalign 0.5
        padding (50, 50)
        vbox:
            spacing 5
            text "Button Action Test"
            textbutton "Click to show another screen.":
                action Show('part2_screen_anotherscreen')
            textbutton "Click to hide another screen.":
                action Hide('part2_screen_anotherscreen')
            hbox:
                spacing 3
                text "Hide everything:"
                textbutton "Click to hide all screens.":
                    action [
                        Hide('part2_screen_buttonactions'),
                        Hide('part2_screen_anotherscreen'),
                        Jump('part2_label_continue')
                    ]
            text "Text at the bottom"

screen part2_screen_anotherscreen():
    frame:
        xalign 0.9 yalign 0.5
        padding (200, 200)
        text "Another screen!"
