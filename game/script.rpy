# The script of the game goes in this file.

# callback=speaker is needed for mouth flaps
define mc = DynamicCharacter("mc_name", callback=speaker("mc"))
define che = Character("CH35H1R3", callback=speaker("che"))

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
    MapEmote('che f happy',  'che pose1 base md_default ed_default brow_default glasses_default')
    MapEmote('che f relaxed',  'che pose1 base md_default ed_relaxed brow_relaxed glasses_default')

    MapEmote('che f catmouthsmall',  'che pose1 base md_catmouthsmall')
    MapEmote('che f catmouth',  'che pose1 base md_catmouth')
    MapEmote('che f grin',  'che pose1 base md_grin')
    MapEmote('che f meh',  'che pose1 base md_meh')
    MapEmote('che f sad',  'che pose1 base md_sad ed_sad brow_sad glasses_default')
    MapEmote('che f thinline',  'che pose1 base md_thinline')

    MapEmote('che f scanning',  'che pose1 armsscanning md_thinline ec_default brow_grumpy glasses_gendo')

    #Cheshire looking off to the side
    MapEmote('che s catmouth',  'che pose2 base md_catmouth')
    MapEmote('che s meh',  'che pose2 base md_meh')
    MapEmote('che s pout1',  'che pose2 base md_poutlvl1')
    MapEmote('che s pout2',  'che pose2 base md_poutlvl2')
    MapEmote('che s thinline',  'che pose2 base md_line')
    MapEmote('che s sad',  'che pose2 base md_sad')

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


# override some default blinking behaviours
#Pose 2

image che_ed_relaxed = blinkeyes("che_e_default", "che_ec_relaxed")
image che_ed_sad = blinkeyes("che_e_sad", "che_ec_relaxed")


# The game starts here.

label start:
    $ persistent.subtitle = False
    show screen in_game_menu
    call screen startgame_login

label start2:
    mc "Subtitles is [persistent.subtitle], and my name is [mc_name]"

    show vrpoweroutageeffect
    pause

    scene woodtrail
    show vfxfireflies
    mc "Testing Animated BG"
    pause

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

    scene bedroom open dark

    "Bedroom with open curtains during the blackout."

    show bedroomlightning dark

    "Bedroom with lightning during the blackout."

    scene bedroom open

    "Bedroom with open curtains."

    show bedroomlightning

    "Bedroom with lightning."

    show hub with dissolve

    show che f default

    che "Testing transition between sprite to CG."

    show cheshire sad hurt shocked tears ticket with dissolve

    che "Oh no poor ches."

    hide cheshire with dissolve
    hide che with dissolve

    call screen hubselect

    return
