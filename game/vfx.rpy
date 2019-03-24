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
        call vreffect from _call_vreffect
        with Pause(1.5)
        show watercresssplash 2 with Dissolve(0.2)
        show watercresssplash 3 with Dissolve(1.0)
        show watercresssplash 4 with Dissolve(0.3)
        with Pause(2)
        scene white with Dissolve(0.5)
        with Pause(1)
        return
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
       

## VR POWER OUTAGE ######################################################################

## A Visual Effect made for the wonderful Sagi; the VR headset experiences a
## a poweroutage, leaving the MC in the dark, playing the animation just once.

image vrpoweroutageeffect:
    "vfx/vrpowerout_01.png"
    0.02
    "vfx/vrpowerout_02.png"                           ## A simple animation~!
    0.02
    "vfx/vrpowerout_03.png"
    0.02
    "vfx/vrpowerout_04.png"
    0.02
    "vfx/vrpowerout_05.png"
    0.02
    "vfx/vrpowerout_06.png"
    0.02
    "vfx/vrpowerout_07.png"
    0.02
    "vfx/vrpowerout_08.png"
    0.02
    "vfx/vrpowerout_09.png"
    0.02
    "vfx/vrpowerout_10.png"
    0.02
    "vfx/vrpowerout_11.png"
    0.02
    "vfx/vrpowerout_12.png"
    0.02
    "vfx/vrpowerout_13.png"
    0.02
    "vfx/vrpowerout_14.png"
    0.02
    "vfx/vrpowerout_15.png"
    0.02
    "vfx/vrpowerout_16.png"                           ## Fun fact, I accidentally made it into an animation cycle at first... it was disorienting!
    0.02

## VR GRID ANIMATION ######################################################################

## A Visual Effect created to simulate an endless grid of pink,
## which is what the world used to look like until the 90s hit.

init:
    image vrgrid = Animation("vfx/vrgrid_01.png",0.02,
                                "vfx/vrgrid_02.png",0.02,
                                "vfx/vrgrid_03.png",0.02,
                                "vfx/vrgrid_04.png",0.02,
                                "vfx/vrgrid_05.png",0.02,
                                "vfx/vrgrid_06.png",0.02,
                                "vfx/vrgrid_07.png",0.02,
                                "vfx/vrgrid_08.png",0.02,)


        
## VR GLITTER ######################################################################

## Alright, something easy to make! Let's make some falling glitter!
## In a game with a cutesy cat girl in a VR setting, anything is possible!

##We make a large .PNG, define that it is a single strip x 250 frames along that strip, and that each strip is a 5x5 px.
image vfxglitterFilmstrip = anim.Filmstrip("vfx/twfy_glittervfx.png", (5,5), (1,250), 0.01) 

## Then give it the SnowBlossom treatment, a count of a 100 on screen at a time, a border of 10px until it can vanish and rest, and then we define the x axis speed and the y axis speed~!
image vfxglitter = SnowBlossom("vfxglitterFilmstrip", count=100, border=10, xspeed=(-25, 25), yspeed=(50, 100), start=10, fast=False, horizontal=False) 


## VR Fireflies ######################################################################

## You would not believe your eyes, you would not believe your eyes, you would not believeeeeeee
## Okay, so its the same idea as the glitter, but values tweaked to get a different result

image vfxfireembersFilmstrip = anim.Filmstrip("vfx/twfy_fireembersvfx.png", (5,5), (1,250), 0.01) 
image vfxfireflies = SnowBlossom("vfxfireembersFilmstrip", count=50, border=10, xspeed=(150, -150), yspeed=(150, -150), start=10, fast=False, horizontal=False)


## VR Field ######################################################################

image fsky = "vfx/fsky.png"

image catfieldbg = "vfx/catlandfieldbg.png"

init:
    image vrfield = Animation("vfx/f1.png",0.59,
                                "vfx/f2.png",0.59,
                                "vfx/f3.png",0.59,
                                "vfx/f4.png",0.59,
                                "vfx/f5.png",0.59,
                                "vfx/f6.png",0.59,
                                "vfx/f7.png",0.59,
                                "vfx/f8.png",0.59,)

    
## VFX BLINKING ######################################################################

## A blinking animation from a First Person Perspective/ Point of View,a simply PNG
## is duplicated twice and flipped upsidedown, both entering offscreen to emulate blinking~!

image eyelidtop = Image("vfx/blink1.png",)
image eyelidbottom = im.Flip("vfx/blink1.png", vertical=True,) #Let's define the eyelids here, this one is mirrored so we can reuse it.

image blinkonce1:
    "eyelidtop"
    xpos 0.5 ypos 0.0                   #Comes from top of screen,
    linear 0.6 xpos 0.5 ypos 0.0        #stays for a moment offscreen,
    linear 0.6 xpos 0.5 ypos 1.0        #moves onto screen fully, and if in unison with the other eyelid, forms a blink
    linear 0.1 xpos 0.5 ypos 1.0        #Pauses, to emulate a slow blink
    linear 0.6 xpos 0.5 ypos 0.0               #and then goes back off screen.
    linear 0.1 xpos 0.5 ypos 0.0

image blinkonce2:
    "eyelidbottom"
    xpos 0.5 ypos 2.0
    linear 0.6 xpos 0.5 ypos 2.0
    linear 0.6 xpos 0.5 ypos 1.0
    linear 0.1 xpos 0.5 ypos 1.0
    linear 0.6 xpos 0.5 ypos 2.0
    linear 0.1 xpos 0.5 ypos 2.0



image blinktwice1:
    "eyelidtop"
    xpos 0.5 ypos 0.0 alpha 1.0
    linear 0.3 xpos 0.5 ypos 0.0
    linear 0.3 xpos 0.5 ypos 1.0
    linear 0.3 xpos 0.5 ypos 0.0
    linear 0.3 xpos 0.5 ypos 1.0
    linear 0.3 xpos 0.5 ypos 0.0

image blinktwice2:
    "eyelidbottom"
    xpos 0.5 ypos 2.0 alpha 1.0
    linear 0.3 xpos 0.5 ypos 2.0
    linear 0.3 xpos 0.5 ypos 1.0
    linear 0.3 xpos 0.5 ypos 2.0
    linear 0.3 xpos 0.5 ypos 1.0
    linear 0.3 xpos 0.5 ypos 2.0

label blinkonce:        #Call it in, don't show. Why? I don't know.
    show blinkonce1
    show blinkonce2
    with dissolve
    return              #without this return placed here, it will continue spewing out the following code beneath it~!

label blinktwice:        
    show blinktwice1
    show blinktwice2
    with dissolve
    return

## Ches Dance ######################################################################

## If this works itd be so cool!

init:
    image Cheshiredance = Animation("sprites/che/pose1/base.png",0.59,
                            "sprites/che/pose1/base2.png",0.59,)
    
image crtlines7 = im.Flip("vfx/crtlines1.png", vertical=True)
image crtlines8 = im.Flip("vfx/crtlines2.png", vertical=True)
image crtlines9 = im.Flip("vfx/crtlines3.png", vertical=True)
image crtlines10 = im.Flip("vfx/crtlines4.png", vertical=True)
image crtlines11 = im.Flip("vfx/crtlines5.png", vertical=True)
image crtlines12 = im.Flip("vfx/crtlines6.png", vertical=True)
image crtlines13 = im.Flip("vfx/crtlines1.png", horizontal=True)
image crtlines14 = im.Flip("vfx/crtlines2.png", horizontal=True)
image crtlines15 = im.Flip("vfx/crtlines3.png", horizontal=True)
image crtlines16 = im.Flip("vfx/crtlines4.png", horizontal=True)
image crtlines17 = im.Flip("vfx/crtlines5.png", horizontal=True)
image crtlines18 = im.Flip("vfx/crtlines6.png", vertical=True)

init:
    image crtvfx = Animation("vfx/crtlines1.png",0.1,
                             "vfx/crtlines2.png",0.1,
                             "vfx/crtlines3.png",0.1,
                             "vfx/crtlines4.png",0.1,
                             "vfx/crtlines5.png",0.1,
                             "vfx/crtlines6.png",0.1,
                             "vfx/crtlines1.png",0.1,
                             "crtlines7",0.1,
                             "crtlines8",0.1,
                             "crtlines9",0.1,
                             "crtlines10",0.1,
                             "crtlines11",0.1,
                             "crtlines12",0.1,
                             "crtlines13",0.1,
                             "crtlines14",0.1,
                             "crtlines15",0.1,
                             "crtlines16",0.1,
                             "crtlines17",0.1,
                             "crtlines18",0.1,)
    
## VFX Fire ######################################################################

## An animated fire for a Campfire
    
init:
    image firevfx = Animation("vfx/campfire_1.png",0.1,
                             "vfx/campfire_2.png",0.1,
                             "vfx/campfire_3.png",0.1,
                             "vfx/campfire_4.png",0.1,
                             "vfx/campfire_5.png",0.1,
                             "vfx/campfire_6.png",0.1,
                             "vfx/campfire_7.png",0.1,
                             "vfx/campfire_8.png",0.1,)

## VR GRID ANIMATION ######################################################################

## A Visual Effect created to simulate an endless grid of pink,
## which is what the world used to look like until the 90s hit.

init:
    image sunset = Animation("vfx/twfysunset_1.png",0.2,
                             "vfx/twfysunset_2.png",0.2,
                             "vfx/twfysunset_3.png",0.2,
                             "vfx/twfysunset_4.png",0.2,
                             "vfx/twfysunset_5.png",0.2,
                             "vfx/twfysunset_6.png",0.2,
                             "vfx/twfysunset_7.png",0.2,
                             "vfx/twfysunset_8.png",0.2,)
                             
