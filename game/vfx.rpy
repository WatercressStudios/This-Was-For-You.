## This file contains strange VFX made by the enigmatic AnagramDaine that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncommentn't
## dem. Lines beginning with a single '#' mark are something something, and I don't code,
## so good luck.

## SPLASH SCREEN ######################################################################

## A BG version of the Watercress is shown to the player changes as a VR headset
##  lowers over their view, changing it to motifs to the character Cheshire

## Splash Screen
label splashscreen:
    scene black
    with Pause(1)
    
    if persistent.ending  == "Complete":                ## For Completionists.
        show watercresssplash 4 with dissolve
        with Pause(2)

        scene watercress with dissolve
        with Pause(1)

        return
    else:
        show watercresssplash 1 with dissolve           ## By Default
        with Pause(0.1)
        call vreffect
        with Pause(1.5)
        show watercresssplash 2 with Dissolve(0.2)
        show watercresssplash 3 with Dissolve(1.0)
        show watercresssplash 4 with Dissolve(0.3)
        with Pause(2)
        scene white with Dissolve(0.5)
        with Pause(1)
        return

## Images used in Splash Screen
image black              = "#000"
image white              = "#FFF"
image watercresssplash 1 = "vfx/watercresssplash1.png"
image watercresssplash 2 = "vfx/watercresssplash2.png"
image watercresssplash 3 = "vfx/watercresssplash3.png"
image watercresssplash 4 = "vfx/watercresssplash4.png"
        
## VR Headset Frames of Animation used in Splash Screen    
init:
    image vrhelmet = Animation("vfx/vrheadset01.png",0.01,
                                "vfx/vrheadset02.png",0.01,
                                "vfx/vrheadset03.png",0.01,
                                "vfx/vrheadset04.png",0.01,
                                "vfx/vrheadset05.png",0.01,
                                "vfx/vrheadset06.png",0.01,
                                "vfx/vrheadset07.png",0.01,
                                "vfx/vrheadset08.png",0.01,
                                "vfx/vrheadset09.png",0.01,
                                "vfx/vrheadset10.png",0.01,)
## VR Headset Lowering Visual
label vreffect:
    show vrhelmet:
        xalign 0.5 yalign 1.3 alpha 1.0 zoom 0.8
        linear 0.25 xalign 0.5 yalign 1.0 alpha 1.0 zoom 0.8
        linear 0.25 xalign 0.5 yalign 0.09 alpha 1.0 zoom 0.8
        linear 1.0 xalign 0.5 yalign 0.09 alpha 1.0 zoom 0.99
        linear 1.0 xalign 0.5 yalign 0.09 alpha 0.5 zoom 1.02
        linear 1.0 xalign 0.5 yalign 0.09 alpha 0.1 zoom 1.02
        
