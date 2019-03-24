#Ceiling

image ceilingfan:
    "bgs/ceiling/ceilingfan.png"
    rotate 0
    xalign 0.5 yalign 0.5
    linear 6 rotate 360
    repeat

#Bedroom

image citylights:
    "bgs/bedroom_layeredimage/citylights.png"
    alpha 0.5
    linear 5 alpha 0.75
    linear 5 alpha 0.5
    linear 5 alpha 0.25
    linear 5 alpha 0.5
    repeat

image lightning:
    alpha 0
    linear 0.2 alpha 1
    "bgs/bedroom_layeredimage/skyline_lightning.png"
    linear 0.2 alpha 0.5
    alpha 1
    "bgs/bedroom_layeredimage/skyline_lightningmore.png"
    0.2
    "bgs/bedroom_layeredimage/skyline_lightning.png"
    linear 0.2 alpha 0

image rain:
    parallel:
        "bgs/bedroom_layeredimage/rain_1.png"
        0.1
        "bgs/bedroom_layeredimage/rain_2.png"
        0.1
        "bgs/bedroom_layeredimage/rain_3.png"
        0.1
        "bgs/bedroom_layeredimage/rain_4.png"
        0.1
        repeat
    parallel:
        alpha 0.2
        linear 2 alpha 0.25
        linear 2 alpha 0.2
        linear 2 alpha 0.15
        linear 2 alpha 0.2
        repeat

image blue:
    alpha 0
    linear 0.2 alpha 1
    "bgs/bedroom_layeredimage/wall_lightning.png"
    linear 0.2 alpha 0.5
    alpha 1
    "bgs/bedroom_layeredimage/wall_lightning.png"
    0.2
    "bgs/bedroom_layeredimage/wall_lightning.png"
    linear 0.2 alpha 0

image darkblue:
    alpha 0
    linear 0.2 alpha 1
    "bgs/bedroom_layeredimage/wall_dark_lightning.png"
    linear 0.2 alpha 0.5
    alpha 1
    "bgs/bedroom_layeredimage/wall_dark_lightning.png"
    0.2
    "bgs/bedroom_layeredimage/wall_dark_lightning.png"
    linear 0.2 alpha 0

image flash:
    alpha 0
    linear 0.2 alpha 1
    "bgs/bedroom_layeredimage/curtains_open_lightning.png"
    linear 0.2 alpha 0.5
    alpha 1
    "bgs/bedroom_layeredimage/curtains_open_lightningmore.png"
    0.2
    "bgs/bedroom_layeredimage/curtains_open_lightning.png"
    linear 0.2 alpha 0

image darkflash:
    alpha 0
    linear 0.2 alpha 1
    "bgs/bedroom_layeredimage/curtains_open_dark_lightning.png"
    linear 0.2 alpha 0.5
    alpha 1
    "bgs/bedroom_layeredimage/curtains_open_dark_lightningmore.png"
    0.2
    "bgs/bedroom_layeredimage/curtains_open_dark_lightning.png"
    linear 0.2 alpha 0

image brightlightning:
    alpha 0
    linear 0.2 alpha 1
    "bgs/bedroom_layeredimage/foreground_lightning.png"
    linear 0.2 alpha 0.5
    alpha 1
    "bgs/bedroom_layeredimage/foreground_lightningmore.png"
    0.2
    "bgs/bedroom_layeredimage/foreground_lightning.png"
    linear 0.2 alpha 0

image darklightning:
    alpha 0
    linear 0.2 alpha 1
    "bgs/bedroom_layeredimage/foreground_dark_lightning.png"
    linear 0.2 alpha 0.5
    alpha 1
    "bgs/bedroom_layeredimage/foreground_dark_lightningmore.png"
    0.2
    "bgs/bedroom_layeredimage/foreground_dark_lightning.png"
    linear 0.2 alpha 0

layeredimage bedroombg:

    group skyline:
        attribute normal default:
            "bgs/bedroom_layeredimage/skyline.png"

        #This is for the blackout when it's dark but there's no lightning
        attribute darker:
            "bgs/bedroom_layeredimage/skyline_dark.png"

    group citylights:
        attribute citylights default:
            "citylights"

    group rain:
        attribute rain:
            "rain"

    group lightning:
        attribute lightning:
            "lightning"

    group wall:
        attribute lit default:
            "bgs/bedroom_layeredimage/wall.png"

        attribute dim:
            "bgs/bedroom_layeredimage/wall_dark.png"

    group curtains:
        attribute closed default:
            "bgs/bedroom_layeredimage/curtains_closed.png"

        attribute nocurtains:
            "bgs/bedroom_layeredimage/curtains_nocurtains.png"

        attribute open:
            "bgs/bedroom_layeredimage/curtains_open.png"

        attribute opendark:
            "bgs/bedroom_layeredimage/curtains_open_dark.png"

    group foreground:
        attribute bright default:
            "bgs/bedroom_layeredimage/foreground.png"

        attribute dark:
            "bgs/bedroom_layeredimage/foreground_dark.png"

layeredimage bedroomstorm:

    group wall:

        attribute blue default:
            "blue"

        attribute darkdark:
            "darkblue"

    group curtains:
        attribute flash default:
            "flash"

        attribute darkflash:
            "darkflash"

        attribute nocurtains:
            "bgs/bedroom_layeredimage/curtains_nocurtains.png"

    group foreground:
        attribute brightlightning default:
            "brightlightning"

        attribute darklightning:
            "darklightning"
