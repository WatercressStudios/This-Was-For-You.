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
    # define VA info and parsing
    voices = {}
    voices['che'] = '#Cheshire (shiena)'
    voices['min'] = '#Ji-min ()'
    voices['bos'] = '#Boss ()'
    voices['mom'] = '#Mom ()'
    voices['dad'] = '#Dad ()'
    voices['caf'] = '#Cafe Owner ()'
    voices['vm'] =  '#Friend ()'
    # To do VA parsing after filling the above:
    # 1. Run the game in Ren'Py
    # 2. Call the console with 'shift+o'
    # 3. Type 'ParseVoices()' and hit enter

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

    MapEmote('che f happyclosed',  'che pose1 ec_default')
    MapEmote('che f catmouthsmall',  'che pose1 md_catmouthsmall')
    MapEmote('che f catmouth',  'che pose1 md_catmouth')
    MapEmote('che f catmouthclosed',  'che pose1 md_catmouth ec_default')
    MapEmote('che f hearteyesmf',  'che pose1 md_catmouth ed_hearteyesmf')
    MapEmote('che f cheerful',  'che pose1 m_cheerful')
    MapEmote('che f cheerfulclosed',  'che pose1 m_cheerful ec_default')
    MapEmote('che f grin',  'che pose1 md_grin')
    MapEmote('che f meh',  'che pose1 md_meh')
    MapEmote('che f mehsad',  'che pose1 md_meh brow_sad')
    MapEmote('che f sad',  'che pose1 md_sad ed_sad brow_sad')
    MapEmote('che f sadclosed',  'che pose1 md_sad ec_sad brow_sad')
    MapEmote('che f thinline',  'che pose1 md_thinline')

    MapEmote('che f scanning',  'che pose1 armsscanning md_thinline ec_default brow_grumpy glasses_gendo')

    #Cheshire looking off to the side
    MapEmote('che s catmouth',  'che pose2 md_catmouth')
    MapEmote('che s catmouthclosed',  'che pose2 md_catmouth ec_default')
    MapEmote('che s meh',  'che pose2 md_meh')
    MapEmote('che s mehsad',  'che pose2 md_meh brow_sad')
    MapEmote('che s pout1',  'che pose2 md_poutlvl1')
    MapEmote('che s pout2',  'che pose2 md_poutlvl2')
    MapEmote('che s thinline',  'che pose2 md_line')
    MapEmote('che s sad',  'che pose2 md_sad brow_sad')
    MapEmote('che s awoo',  'che pose2 m_awoo ec_wolfmeme')

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
    $ in_main_menu = False
    $ save_name = "Memories of You"
    menu:
        "Start game":
            $ persistent.subtitle = False
            $ visited8track = False
            $ visitedplushie = False
            $ visitedmug = False
            $ visited = 0
            $ relogin = False
            show screen in_game_menu
            call screen startgame_login
        "Test":
            jump test

label start2:
    jump intro

label test:
    mc "Subtitles is [persistent.subtitle], and my name is [mc_name]"
    sfx "sfx/curtains.wav"
    che "SFX without any subtitles"
    sfx "sfx/curtains.wav" "*Click!*"
    che "SFX with subtitles"

    show vrpoweroutageeffect
    pause

    scene black
    voice "00-test-1.mp3" #Cheshire (shiena)
    che "Ready?"
    show vrpoweroutageeffect
    voice "00-test-2.mp3" #Cheshire (shiena)
    che "vrpoweroutageeffect"
    scene sunsettitle
    voice "00-test-3.mp3" #Cheshire (shiena)
    che "sunsettitle"
    call blinkonce
    voice "00-test-4.mp3" #Cheshire (shiena)
    che "call blinkonce"
    call blinktwice
    voice "00-test-5.mp3" #Cheshire (shiena)
    che "call blinktwice"
    show crtvfx
    voice "00-test-6.mp3" #Cheshire (shiena)
    che "crtvfx"
    scene woodtrail1
    show che f default
    with dissolve
    voice "00-test-7.mp3" #Cheshire (shiena)
    che "Bg woodtrail"

    scene woodtrail2
    show che f default
    with dissolve
    voice "00-test-8.mp3" #Cheshire (shiena)
    che "Bg woodtrail2"

    scene kerosene
    with dissolve
    voice "00-test-9.mp3" #Cheshire (shiena)
    che "Bg Kerosene"

    scene vrgrid
    show che f dance happy
    with dissolve
    voice "00-test-10.mp3" #Cheshire (shiena)
    che "Test Dance/Proof of concept"

    scene catfieldbg
    show fsky:
        xalign 0.5 yalign 0.3 rotate 0 zoom 1.1 alpha 0.5
        linear 60 rotate 180
        linear 60 rotate 360
        repeat
    show vrfield:
        alpha 0.5 zoom 0.75
    voice "00-test-11.mp3" #Cheshire (shiena)
    che "Test Bg Field"

    show vrgrid
    show vfxglitter

    pause
    show che f default

    mc "Pose1 default flap mouth."

    mc "Hover your mouse over MENU or email."
    show screen in_game_entervr

    voice "00-test-12.mp3" #Cheshire (shiena)
    che "Click on VR."

    hide screen in_game_entervr
    show screen in_game_exitvr

    voice "00-test-13.mp3" #Cheshire (shiena)
    che "Click on RW."

    hide screen in_game_exitvr

    show che s default

    voice "00-test-14.mp3" #Cheshire (shiena)
    che "Pose2 default flap mouth."

    show che f catmouthsmall

    voice "00-test-15.mp3" #Cheshire (shiena)
    che "Pose1 catmouthsmall flap mouth."

    show che f catmouth

    voice "00-test-16.mp3" #Cheshire (shiena)
    che "Pose1 catmouth flap mouth."

    show che f meh

    voice "00-test-17.mp3" #Cheshire (shiena)
    che "Pose1 meh flap mouth."

    show che f sad

    voice "00-test-18.mp3" #Cheshire (shiena)
    che "Pose1 sad flap mouth."

    show che f scanning

    voice "00-test-19.mp3" #Cheshire (shiena)
    che "Pose1 thinline flap mouth."

    show che f happy

    voice "00-test-20.mp3" #Cheshire (shiena)
    che "Pose1 happy flap mouth."

    show che s catmouth

    voice "00-test-21.mp3" #Cheshire (shiena)
    che "Pose2 catmouth flap mouth."

    show che s meh

    voice "00-test-22.mp3" #Cheshire (shiena)
    che "Pose2 meh flap mouth."

    show che s pout1

    voice "00-test-23.mp3" #Cheshire (shiena)
    che "Pose2 pout1 flap mouth."

    show che s pout2

    voice "00-test-24.mp3" #Cheshire (shiena)
    che "Pose2 pout2 flap mouth."

    show che s thinline

    voice "00-test-25.mp3" #Cheshire (shiena)
    che "Pose2 thinline flap mouth."

    show che s sad

    voice "00-test-26.mp3" #Cheshire (shiena)
    che "Pose2 sad flap mouth."

    scene bg ceiling ceiling empty
    show ceilingfan

    voice "00-test-27.mp3" #Cheshire (shiena)
    che "Ceiling fan animation."

    hide ceilingfan
    show bg bedroombg

    "Standard bedroom bg."

    show bg bedroombg nocurtains

    "Lets see the skyline."

    show bg bedroombg lightning
    show bedroomstorm nocurtains

    "Now for some lightning."

    hide bedroomstorm
    show bg bedroombg rain -lightning

    "And now some rain."

    #Zoom in and fall

    show bg bedroombg open -rain:
        zoom 1.5
        xalign 0.9 yalign 0.2

    "Testing bedroom zoom in."

    show bg bedroombg open:
        linear 0.2 yalign 0.8

    pause 0.1

    show black with vpunch:
        alpha 0
        linear 0.1 alpha 1

    show bg bedroombg open with vpunch
    hide black

    "Testing falling effect."

    #End zoom in and fall

    show bg hub hub with dissolve:
        zoom 1

    show che f default

    voice "00-test-28.mp3" #Cheshire (shiena)
    che "Testing transition between sprite to CG."

    show cheshire sad hurt shocked tears ticket with dissolve

    voice "00-test-29.mp3" #Cheshire (shiena)
    che "Oh no poor ches."

    hide cheshire with dissolve
    hide che with dissolve

    call screen hubselect

    return
