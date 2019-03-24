# The script of the game goes in this file.

# callback=speaker is needed for mouth flaps
define mc = DynamicCharacter("mc_name", callback=speaker("mc"))
define che = Character("CH35H1R3", callback=speaker("che"))
define min = Character("Ji-min", callback=speaker("min"))
define bos = Character("Boss", callback=speaker("bos"))
define mom = Character("Mom", callback=speaker("mom"))
define dad = Character("Dad", callback=speaker("dad"))
define caf = Character("Cafe Owner", callback=speaker("caf"))
define vm = Character("Friend", callback=speaker("vm"))

init python:
    # define the BGs
    DefineImages('cgs')
    DefineImages('bgs', prepend='bg')
    DefineImages('mainmenu', prepend='mm')

    # define the sprites with manual layer ordering
    #layerorder = None
    layerorder = ['base','mouth','eyes','brow','blush','shadows','glasses']
    DefineImages("sprites", composite=True, overrideLayerOrder=layerorder)

    # manually create shortcuts to more complex expressions

    #Cheshire looking forward
    MapEmote('che f happy',  'che pose1 md_default ed_default brow_default glasses_default')
    MapEmote('che f relaxed',  'che pose1 md_default ed_relaxed brow_relaxed glasses_default')

    MapEmote('che f catmouthsmall',  'che pose1 md_catmouthsmall')
    MapEmote('che f catmouth',  'che pose1 md_catmouth')
    MapEmote('che f grin',  'che pose1 md_grin')
    MapEmote('che f meh',  'che pose1 md_meh')
    MapEmote('che f sad',  'che pose1 md_sad ed_sad brow_sad glasses_default')
    MapEmote('che f thinline',  'che pose1 md_thinline')

    MapEmote('che f scanning',  'che pose1 armsscanning md_thinline ec_default brow_grumpy glasses_gendo')

    #Cheshire looking off to the side
    MapEmote('che s catmouth',  'che pose2 md_catmouth')
    MapEmote('che s meh',  'che pose2 md_meh')
    MapEmote('che s pout1',  'che pose2 md_poutlvl1')
    MapEmote('che s pout2',  'che pose2 md_poutlvl2')
    MapEmote('che s thinline',  'che pose2 md_line')
    MapEmote('che s sad',  'che pose2 md_sad')

    MapEmote('che s nya',  'che pose2 armsnyan md_default ed_default brow_default glasses_default')

# override some default mouth flap behaviours
#Pose 1

image che_pose1_md_catmouthsmall = FlapMouth("che_pose1_mc_catmouthsmall", "che_pose1_m_openmore")
image che_pose1_md_catmouth = FlapMouth("che_pose1_mc_catmouth", "che_pose1_m_openevenmore")
image che_pose1_md_meh = FlapMouth("che_pose1_mc_meh", "che_pose1_m_shocked")
image che_pose1_md_sad = FlapMouth("che_pose1_mc_sad", "che_pose1_m_shocked")
image che_pose1_md_thinline = FlapMouth("che_pose1_mc_thinline", "che_pose1_m_default")

#Pose 2

image che_pose2_md_default = FlapMouth("che_pose2_mc_default", "che_pose2_m_openmore")
image che_pose2_md_catmouth = FlapMouth("che_pose2_mc_catmouth", "che_pose2_m_openmore")
image che_pose2_md_meh = FlapMouth("che_pose2_mc_meh", "che_pose2_m_eck")
image che_pose2_md_poutlvl1 = FlapMouth("che_pose2_mc_poutlv1", "che_pose2_m_awoo")
image che_pose2_md_poutlvl2 = FlapMouth("che_pose2_mc_poutlv2", "che_pose2_m_awoo")
image che_pose2_md_line = FlapMouth("che_pose2_mc_line", "che_pose2_m_eck")
image che_pose2_md_sad = FlapMouth("che_pose2_mc_sad", "che_pose2_m_awoo")


# override some default behaviours

image che_ed_relaxed = blinkeyes("che_e_default", "che_ec_relaxed")
image che_ed_sad = blinkeyes("che_e_sad", "che_ec_relaxed")
image che_pose1_dance = Animation("sprites/che/pose1/base.png",0.59,
                        "sprites/che/pose1/dance.png",0.59,)

# The game starts here.

label start:
    menu:
        "Start game":
            $ persistent.subtitle = False
            $ visited8track = False
            $ visitedplushie = False
            $ visitedmug = False
            $ visited = 0
            show screen in_game_menu
            call screen startgame_login
        "Test":
            jump test

label start2:
    jump intro

label test:
    mc "Subtitles is [persistent.subtitle], and my name is [mc_name]"

    show vrpoweroutageeffect
    pause

    scene black
    che "Ready?"
    show vrpoweroutageeffect
    che "vrpoweroutageeffect"
    scene sunsettitle
    che "sunsettitle"
    call blinkonce
    che "call blinkonce"
    call blinktwice
    che "call blinktwice"
    show crtvfx
    che "crtvfx"
    scene woodtrail1
    show che f default
    with dissolve
    che "Bg woodtrail"

    scene woodtrail2
    show che f default
    with dissolve
    che "Bg woodtrail2"

    scene kerosene
    with dissolve
    che "Bg Kerosene"

    scene vrgrid
    show che f dance happy
    with dissolve
    che "Test Dance/Proof of concept"

    scene catfieldbg
    show fsky:
        xalign 0.5 yalign 0.3 rotate 0 zoom 1.1 alpha 0.5
        linear 60 rotate 180
        linear 60 rotate 360
        repeat
    show vrfield:
        alpha 0.5 zoom 0.75
    che "Test Bg Field"

    show vrgrid
    show vfxglitter

    pause
    show che f default

    mc "Pose1 default flap mouth."

    mc "Hover your mouse over MENU or email."
    show screen in_game_entervr

    che "Click on VR."

    hide screen in_game_entervr
    show screen in_game_exitvr

    che "Click on RW."

    hide screen in_game_exitvr

    show che s default

    che "Pose2 default flap mouth."

    show che f catmouthsmall

    che "Pose1 catmouthsmall flap mouth."

    show che f catmouth

    che "Pose1 catmouth flap mouth."

    show che f meh

    che "Pose1 meh flap mouth."

    show che f sad

    che "Pose1 sad flap mouth."

    show che f scanning

    che "Pose1 thinline flap mouth."

    show che f happy

    che "Pose1 happy flap mouth."

    show che s catmouth

    che "Pose2 catmouth flap mouth."

    show che s meh

    che "Pose2 meh flap mouth."

    show che s pout1

    che "Pose2 pout1 flap mouth."

    show che s pout2

    che "Pose2 pout2 flap mouth."

    show che s thinline

    che "Pose2 thinline flap mouth."

    show che s sad

    che "Pose2 sad flap mouth."

    scene ceiling empty
    show ceilingfan

    che "Ceiling fan animation."

    show bedroombg

    "Standard bedroom bg."

    show bedroombg nocurtains

    "Lets see the skyline."

    show bedroombg lightning
    show bedroomstorm nocurtains

    "Now for some lightning."

    hide bedroomstorm
    show bedroombg rain -lightning

    "And now some rain."

    #Zoom in and fall

    show bedroombg open -rain:
        zoom 1.5
        xalign 0.9 yalign 0.2

    "Testing bedroom zoom in."

    show bedroombg open:
        linear 0.2 yalign 0.8

    pause 0.1

    show black with vpunch:
        alpha 0
        linear 0.1 alpha 1

    show bedroombg open with vpunch

    "Testing falling effect."

    #End zoom in and fall

    show hub with dissolve

    show che f default

    che "Testing transition between sprite to CG."

    show cheshire sad hurt shocked tears ticket with dissolve

    che "Oh no poor ches."

    hide cheshire with dissolve
    hide che with dissolve

    call screen hubselect

    return
