#Ceiling

image ceilingfan:
    "bgs/ceiling/ceilingfan.png"
    rotate 0
    xalign 0.5 yalign 0.5
    linear 6 rotate 360
    repeat

image ceilingfanstatic = "bgs/ceiling/ceilingfan.png"

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
    #"bgs/bedroom/bedroom open dark.png"

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

layeredimage bg bedroombg:

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

        attribute darkblue:
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

## VR Woodtrail1 ######################################################################

## The Foreground stays still as the abstract landscape flickers abstractly.
## Wolf wanted abstract, we gonna get abstract up in this VN.

image woodtrailstarsdraz1:                             ##DRAZ WAS HERE######################################################################
    "vfx/bg_woodtrail_base.png"

image woodtrailbgdraz1:                                ## Thanks to Draz, Anagram is now able to code a bunch a stuff~! Draz is the best Space Future Aunt ever~!
    "vfx/bg_woodtrail_base2.png"
    alpha 1.0
    linear 5.0 alpha 0.1
    linear 5.0 alpha 0.1
    linear 5.0 alpha 1.0
    linear 10.0 alpha 1.0
    linear 10.0 alpha 0.1
    linear 15.0 alpha 0.1
    linear 15.0 alpha 1.0
    linear 15.0 alpha 1.0
    repeat

image woodtrailforegrounddraz1:
    "vfx/bg_woodtrail_foreground.png"
    alpha 1.0
    linear 2.0 alpha 1.0
    linear 2.0 alpha 0.8
    linear 2.0 alpha 1.0
    linear 3.0 alpha 0.7
    linear 3.0 alpha 1.0
    repeat

image crtwoods1:
    "crtvfx"
    alpha 0.1

layeredimage woodtrail1:
    always:
        "woodtrailstarsdraz1"

    always:
        "woodtrailbgdraz1"

    always:
        "woodtrailforegrounddraz1"

    always:
        "vfxfireflies"

    always:
        "crtwoods1"



## VR Woodtrail2 ######################################################################

## Same as the last one, now possible thanks to Draz' code.
## MC delves deepers, seeing a glow in the distance.

image woodtrailstarsdraz2:                             ##Feel free to thank Draz again, I stole the code and used it to make another BG. Enjoy~!
    "vfx/bg_woodtrail2_base.png"

image woodtrailbgdraz2:
    "vfx/bg_woodtrail2_base2.png"
    alpha 1.0
    linear 2.0 alpha 0.0
    linear 2.0 alpha 0.0
    linear 3.0 alpha 1.0
    linear 3.0 alpha 1.0
    linear 4.0 alpha 0.0
    linear 4.0 alpha 0.0
    linear 7.0 alpha 1.0
    linear 7.0 alpha 1.0
    repeat

image woodtrailforegrounddraz2:
    "vfx/bg_woodtrail2_foreground.png"
    alpha 1.0
    linear 2.0 alpha 0.9
    linear 2.0 alpha 0.7
    linear 2.0 alpha 0.9
    linear 3.0 alpha 0.6
    linear 3.0 alpha 0.9
    repeat

image crtwoods2:
    "crtvfx"
    xalign 0.5 yalign 0.5 alpha 0.3

layeredimage woodtrail2:
    always:
        "woodtrailstarsdraz2"

    always:
        "woodtrailbgdraz2"

    always:
        "woodtrailforegrounddraz2"

    always:
        "vfxfireflies"

    always:
        "crtwoods2"

## VR Campfire ######################################################################

## MC finds a campfire.

image campfire2:
    "vfx/kerosene_base2.png"

image campfire1:
    "vfx/kerosene_base1.png"
    alpha 1.0
    linear 1.5 alpha 0.5
    linear 0.5 alpha 1.0
    linear 0.5 alpha 0.5
    linear 1.5 alpha 1.0
    linear 1.5 alpha 0.5
    linear 0.5 alpha 1.0
    linear 0.5 alpha 0.0
    linear 0.5 alpha 0.2
    linear 1.0 alpha 1.0
    linear 0.5 alpha 0.0
    linear 1.0 alpha 0.0
    linear 1.0 alpha 1.0
    linear 0.5 alpha 1.0
    repeat

image keroseneforeground:
    "vfx/kerosene_foreground.png"
    alpha 1.0


image campfire:
    "firevfx"
    xpos 692 ypos 108 zoom 0.75 alpha 1.0
    block:
        linear 1.0 ypos 86 alpha 0.9
        linear 1.0 ypos 108 alpha 1.0
        linear 1.0 ypos 86 alpha 0.9
        linear 1.0 ypos 108 alpha 1.0
        linear 1.0 ypos 86 alpha 0.7
        linear 1.0 ypos 108 alpha 1.0
        repeat

layeredimage kerosene:
    always:
        "campfire2"

    always:
        "campfire1"

    always:
        "keroseneforeground"

    always:
        "campfire"

    always:
        "vfxfireflies"

image sunsettitlescreen:
    "sunset"
    zoom 1.0
    linear 120.0 zoom 1.02
    linear 120.0 zoom 1.0
    repeat

image sun:
    "vfx/sun.png"
    xalign 0.5 yalign 0.5 alpha 1.0
    linear 1.0 alpha 0.3
    linear 1.0 alpha 1.0
    repeat

layeredimage sunsettitle:
    always:
        "sunsettitlescreen"
    always:
        "sun"
