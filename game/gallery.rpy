#
# Generate gallery screen based on parameters below
#

init python:
    gallery_content = [
        ( "thumbnails/bedroom.png", "bg bedroombg", "Bedroom", "Alison Huang"),
        ( "thumbnails/ceiling.png", "bg ceiling ceiling static", "Ceiling", "Alison Huang"),
        ( "thumbnails/hub.png", "bg hub hub", "Hub", "Alison Huang"),
        ( "thumbnails/kerosene.png", "kerosene", "Kerosene", "AnagramDaine"),
        ( "thumbnails/catfield.png", "catfieldbg", "Catfield", "AnagramDaine"),
        ( "thumbnails/woodtrail1.png", "woodtrail1", "Woodtrail", "AnagramDaine"),
        ( "thumbnails/woodtrail2.png", "woodtrail2", "Woodtrail 2", "AnagramDaine"),
        ( "thumbnails/sunset.png", "sunsettitle", "Sunset", "AnagramDaine"),
        ( "thumbnails/cheforward.png", "che f", "Cheshire Sprite - Forward", "AnagramDaine"),
        ( "thumbnails/cheside.png", "che s", "Cheshire Sprite - Side", "AnagramDaine"),
        ( "thumbnails/cheshire.png", "cheshire", "Cheshire CG", "Alison Huang"),
        ( "thumbnails/uninstallbutton.png", "items uninstallbutton", "Uninstall Button", "Alison Huang"),
        ( "thumbnails/awoomug.png", "items awoomug", "Awoo Mug", "Alison Huang"),
        ( "thumbnails/catplushie.png", "items catplushie", "Cat Plushie", "Alison Huang"),
        ( "thumbnails/8track.png", "items 8track", "8 Track", "Alison Huang"),
        ( "thumbnails/planeticket.png", "items planeticket", "Plane Ticket", "Alison Huang"),
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

                for thumbnail, pic, title, artist in gallery_content:
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
                                add At(thumbnail)
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
