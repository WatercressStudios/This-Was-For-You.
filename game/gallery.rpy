#
# Generate credits screen based on parameters below
#

init python:
    gallery_content = [
        ( "bg bedroombg", "Lonely bedroom", "Draz"),
        ( "bg bedroombg", "Title of image", "Artist"),
        ( "bg bedroombg", "Title of image", "Artist"),
        ( "bg bedroombg", "Title of image", "Artist"),
        ( "bg bedroombg", "Title of image", "Artist"),
        ( "bg bedroombg", "Title of image", "Artist"),
        ( "bg bedroombg", "Title of image", "Artist"),
        ( "bg bedroombg", "Title of image", "Artist"),
        ( "bg bedroombg", "Title of image", "Artist"),
        ( "bg bedroombg", "Title of image", "Artist"),
        ( "bg bedroombg", "Title of image", "Artist"),
        ( "bg bedroombg", "Title of image", "Artist"),
        ( "bg bedroombg", "Title of image", "Artist"),
        ( "bg bedroombg", "Title of image", "Artist"),
        ( "bg bedroombg", "Title of image", "Artist"),
        ( "bg bedroombg", "Title of image", "Artist"),
    ]

transform gallery_thumbnail:
    xzoom 0.2
    yzoom 0.2

screen gallery_item(item):
    fixed at fade_inout:
        add item
    key "dismiss" action Hide("gallery_item")

screen gallery():
    frame at fade_inout:
        background "megan_ui/gui-gallery-background.png"
        xsize 1840
        ysize 1000
        align (0.5, 0.5)
        padding (0,0,0,0)
        frame:
            pos (30, 110)
            background None
            padding (0,0,0,0)
            xsize 1700
            ysize 800
            vpgrid:
                cols 4
                mousewheel True
                draggable True
                scrollbars "vertical"
                side_xalign 0.5
                yinitial 0.0
                xspacing 0
                yspacing 0

                for pic, title, artist in gallery_content:
                    frame:
                        background At(pic, gallery_thumbnail)
                        xsize 414
                        ysize 270
                        padding (15,15,15,15)
                        label title pos (0, 110)
                        label "by " + artist pos (0, 150)
                        button action Show("gallery_item", item=pic)
        fixed pos (1565,918):
            imagebutton offset (-40, -5):
                idle "megan_ui/gui-back-idle.png"
                hover "megan_ui/gui-back-select.png"
                if in_main_menu:
                    action [ Play("sound", uisound()), Hide("custom_title_extras"), Show("custom_title_center2right") ]
                else:
                    action [ Play("sound", uisound()), Return() ]
            # text "Back":
            #     font "BebasNeue-Regular.otf"
            #     size 60
            #     color "#36428A"
            #     outlines []
