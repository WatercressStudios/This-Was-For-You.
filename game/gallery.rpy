#
# Generate gallery screen based on parameters below
#

init python:
    gallery_content = [
        ( "bg bedroombg", "Bedroom", "Alison Huang"),
        ( "bg ceiling ceiling static", "Ceiling", "Alison Huang"),
        ( "bg hub hub", "Hub", "Alison Huang"),
        ( "thumbnails/kerosene.png", "Kerosene", "AnagramDaine"),
        ( "thumbnails/catfield.png", "Catfield", "AnagramDaine"),
        ( "thumbnails/woodtrail1.png", "Woodtrail", "AnagramDaine"),
        ( "thumbnails/woodtrail2.png", "Woodtrail 2", "AnagramDaine"),
        ( "thumbnails/sunset.png", "Sunset", "AnagramDaine"),
        ( "thumbnails/cheforward.png", "Cheshire Sprite - Forward", "AnagramDaine"),
        ( "thumbnails/cheside.png", "Cheshire Sprite - Side", "AnagramDaine"),
        ( "cheshire", "Cheshire CG", "Alison Huang"),
        ( "items uninstallbutton", "Uninstall Button", "Alison Huang"),
        ( "items awoomug", "Awoo Mug", "Alison Huang"),
        ( "items catplushie", "Cat Plushie", "Alison Huang"),
        ( "items 8track", "8 Track", "Alison Huang"),
        ( "items planeticket", "Plane Ticket", "Alison Huang"),
    ]

image black = Solid("#000")

transform gallery_thumbnail:
    xzoom 0.2
    yzoom 0.2

screen gallery_item(item):
    fixed at fade_inout:
        add "bg black"
    fixed align(0.5,0.5):
        xfit True
        yfit True
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
                        background None
                        xsize 414
                        ysize 246
                        padding (0,15,30,15)

                        frame:
                            background At("bg black", gallery_thumbnail)
                            xsize 384
                            ysize 216
                            padding (0,0,0,0)
                            fixed align(0.5,0.5):
                                xfit True
                                yfit True
                                add At(pic, gallery_thumbnail)
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
