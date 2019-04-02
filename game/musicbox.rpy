#
# Generate music box screen based on parameters below
#

init python:
    musicbox_content = [
        ( "Music/Main Menu.ogg", "Menu Theme", "Paul Robins"),
        ( "Music/RW_Intro.ogg", "Memories of You", "Paul Robins"),
        ( "Music/Hub.ogg", "HU8 W0RLD", "Kieren 'Kierious' Eller"),
        ( "Music/Uninstall_Button.ogg", "Uninstall Button", "Speedy"),
        ( "Music/RW_S1.ogg","The World Keeps Turning", "Paul Robins"),
        ( "Music/Awoo_Mug.ogg", "You Were so Strong", "Speedy"),
        ( "Music/Cat.ogg", "Apologies", "Kieren 'Kierious' Eller"),
        ( "Music/8_Track.ogg", "Our Song", "Raymond Demers"),
        ( "Music/RW_S2.ogg", "Sustenance", "Paul Robins"),
        ( "Music/RW_S3.ogg", "Only The Good Die Young", "Paul Robins"),
        ( "Music/RW_S4.ogg", "Friendships", "Paul Robins"),
        ( "Music/Plane_Ticket.ogg", "What Could Have Been", "Speedy"),
    ]

    musicbox_currently_playing = None

screen musicbox():
    frame at fade_inout:
        background "megan_ui/gui-musicbox-background.png"
        xsize 920
        ysize 1000
        pos (500, 40)
        padding (0,0,0,0)
        frame:
            pos (40, 120)
            background None
            padding (0,0,0,0)
            xsize 790
            ysize 770
            vpgrid xoffset -10:
                cols 1
                mousewheel True
                draggable True
                scrollbars "vertical"
                side_xalign 0.5
                yinitial 0.0
                yspacing 20

                for i in range(len(musicbox_content)):
                    $ clip, title, artist = musicbox_content[i]
                    frame:
                        background None
                        xsize 750
                        ysize 135
                        padding (0,0,0,0)
                        right_margin 20
                        xalign 0
                        imagebutton:
                            idle Frame("megan_ui/save_slot_frame.png", Borders(30,30,30,30))
                            hover Frame("megan_ui/save_slot_frame_hover.png", Borders(30,30,30,30))
                            if i == musicbox_currently_playing:
                                action [ SetVariable("musicbox_currently_playing", None), Play("music", "music/Main Menu.ogg") ]
                            else:
                                action [ SetVariable("musicbox_currently_playing", i), Play("music", clip) ]

                        frame:
                            background None
                            xsize 750
                            ysize 135
                            padding (30,15,30,15)
                            right_margin 20
                            xalign 0

                            text title pos (0, 0):
                                font "BebasNeue-Regular.otf"
                                size 50
                                color "#36428A"
                                outlines []
                            text "by " + artist pos (0, 50):
                                font "BebasNeue-Regular.otf"
                                size 50
                                color "#36428A"
                                outlines []
                            fixed pos (600,23):
                                if i == musicbox_currently_playing:
                                    add "megan_ui/gui-musicbox-pause.png"
                                else:
                                    add "megan_ui/gui-musicbox-play.png"

        fixed pos (40, 40):
            text "Music Box":
                font "BebasNeue-Regular.otf"
                size 60
                color "#36428A"
                outlines []

        fixed pos (650, 910):
            imagebutton offset (-40, -5):
                idle "megan_ui/gui-back-idle.png"
                hover "megan_ui/gui-back-select.png"
                if in_main_menu:
                    action [ Play("sound", uisound()), Hide("custom_title_extras"), Show("custom_title_right2center") ]
                else:
                    action [ Play("sound", uisound()), Return() ]
            text "Back":
                font "BebasNeue-Regular.otf"
                size 60
                color "#36428A"
                outlines []
