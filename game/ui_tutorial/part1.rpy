#
# Part 1 of UI tutorial, Hello World.
# At the top of the "start" label, "jump" into the label below to test.
#

label part1_label:
    show screen part1_helloworld
    "Click to continue."
    show screen part1_helloworld_with_frame
    "Click to continue."
    show screen part1_helloworld_with_frame_nobg
    "Click to continue."
    show screen part1_helloworld_with_frame_custombg
    "Click to continue."
    hide screen part1_helloworld
    hide screen part1_helloworld_with_frame
    hide screen part1_helloworld_with_frame_nobg
    hide screen part1_helloworld_with_frame_custombg
    "Click to continue."

screen part1_helloworld():
    fixed:
        xpos 0.5 ypos 0.5
        text "Hello world."

screen part1_helloworld_with_frame():
    frame:
        xalign 0.8 yalign 0.5
        padding (200, 200)
        text "Hello world."

screen part1_helloworld_with_frame_nobg():
    frame:
        xalign 0.4 yalign 0.5
        padding (200, 200)
        background None
        text "Hello world."

screen part1_helloworld_with_frame_custombg():
    frame:
        xalign 0.2 yalign 0.5
        padding (200, 200)
        background Frame("ui_tutorial/customframe.png", 40, 40, 40, 40)
        text "Hello world."
