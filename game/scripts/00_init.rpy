# The script of the game goes in this file.

# callback=speaker is needed for mouth flaps
define mc = DynamicCharacter("mc_name", callback=speaker("mc"), what_prefix="[[[mc_name]] ", what_color="#f4d6a7")
define che = Character("CH35H1R3", callback=speaker("che"), what_prefix="[[CH35H1R3] ", what_color="#A4FBFE")
define min = Character("Ji-min", callback=speaker("min"), what_prefix="[[Ji-min] ", what_color="#e1e1e1")
define bos = Character("Boss", callback=speaker("bos"), what_prefix="[[Boss] ", what_color="#e1e1e1")
define mom = Character("Mom", callback=speaker("mom"), what_prefix="[[Mom] ", what_color="#e1e1e1")
define dad = Character("Dad", callback=speaker("dad"), what_prefix="[[Dad] ", what_color="#e1e1e1")
define caf = Character("Cafe Owner", callback=speaker("caf"), what_prefix="[[Cafe Owner] ", what_color="#e1e1e1")
define vm = Character("Friend", callback=speaker("vm"), what_prefix="[[Friend] ", what_color="#e1e1e1")

init python:
    # define VA info and parsing
    voices = {}
    voices['che'] = '#Cheshire (shiena)'
    voices['min'] = '#Ji-min (Ariane "Starleeter" Marchese)'
    voices['bos'] = '#Boss (Bryce Buckley)'
    voices['mom'] = '#Mom (Kenkoy)'
    voices['dad'] = '#Dad (Adam Warren)'
    voices['caf'] = '#Cafe Owner ()'
    voices['vm'] =  '#Friend (1_ Kenneth Faircloth 2_ Siddharta Villanueva)'
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

# new ambient sound channel

init python:
    renpy.music.register_channel("ambient", "music", True)


# override some default behaviours

image che_ed_relaxed = blinkeyes("che_e_default", "che_ec_relaxed")
image che_ed_sad = blinkeyes("che_e_sad", "che_ec_relaxed")

image che_pose1_dance = Animation("sprites/che/pose1/base.png",0.59,
                        "sprites/che/pose1/dance.png",0.59,)

# The game starts here.

label start:
    $ in_main_menu = False
    $ save_name = "Memories of You"
    $ _game_menu_screen = None
    $ visible_emails = ["intro"]
    $ read_emails = []

    #$ persistent.subtitle = False
    $ visited8track = False
    $ visitedplushie = False
    $ visitedmug = False
    $ visited = 0
    $ relogin = False
    show screen in_game_menu
    call screen startgame_login

    # menu:
    #     "Start game":
    #         $ persistent.subtitle = False
    #         $ visited8track = False
    #         $ visitedplushie = False
    #         $ visitedmug = False
    #         $ visited = 0
    #         $ relogin = False
    #         show screen in_game_menu
    #         call screen startgame_login
    #     "Test":
    #         jump test

label start2:
    jump intro

label test:
    show screen in_game_entervr
    show screen in_game_exitvr

    mc "Subtitles is [persistent.subtitle], and my name is [mc_name]"
    sfx "sfx/curtains.wav"
    voice "voice/00-test-1.ogg" #Cheshire (shiena)
    che "SFX without any subtitles"
    sfx [ "<silence 1>", "sfx/thunder_2.ogg" ] "Clicked!"

    #sfx "sfx/curtains.wav" "*Click!*"
    voice "voice/00-test-2.ogg" #Cheshire (shiena)
    che "SFX with subtitles"

    show vrpoweroutageeffect
    pause

    scene black
    voice "voice/00-test-3.ogg" #Cheshire (shiena)
    che "Ready?"
    show vrpoweroutageeffect
    voice "voice/00-test-4.ogg" #Cheshire (shiena)
    che "vrpoweroutageeffect"
    scene sunsettitle
    voice "voice/00-test-5.ogg" #Cheshire (shiena)
    che "sunsettitle"
    call blinkonce
    voice "voice/00-test-6.ogg" #Cheshire (shiena)
    che "call blinkonce"
    call blinktwice
    voice "voice/00-test-7.ogg" #Cheshire (shiena)
    che "call blinktwice"
    show crtvfx
    voice "voice/00-test-8.ogg" #Cheshire (shiena)
    che "crtvfx"
    scene woodtrail1
    show che f default
    with dissolve
    voice "voice/00-test-9.ogg" #Cheshire (shiena)
    che "Bg woodtrail"

    scene woodtrail2
    show che f default
    with dissolve
    voice "voice/00-test-10.ogg" #Cheshire (shiena)
    che "Bg woodtrail2"

    scene kerosene
    with dissolve
    voice "voice/00-test-11.ogg" #Cheshire (shiena)
    che "Bg Kerosene"

    scene vrgrid
    show che f dance happy
    with dissolve
    voice "voice/00-test-12.ogg" #Cheshire (shiena)
    che "Test Dance/Proof of concept"

    scene catfieldbg
    show fsky:
        xalign 0.5 yalign 0.3 rotate 0 zoom 1.1 alpha 0.5
        linear 60 rotate 180
        linear 60 rotate 360
        repeat
    show vrfield:
        alpha 0.5 zoom 0.75
    voice "voice/00-test-13.ogg" #Cheshire (shiena)
    che "Test Bg Field"

    show vrgrid
    show vfxglitter

    pause
    show che f default

    mc "Pose1 default flap mouth."

    mc "Hover your mouse over MENU or email."
    show screen in_game_entervr

    voice "voice/00-test-14.ogg" #Cheshire (shiena)
    che "Click on VR."

    hide screen in_game_entervr
    show screen in_game_exitvr

    voice "voice/00-test-15.ogg" #Cheshire (shiena)
    che "Click on RW."

    hide screen in_game_exitvr

    show che s default

    voice "voice/00-test-16.ogg" #Cheshire (shiena)
    che "Pose2 default flap mouth."

    show che f catmouthsmall

    voice "voice/00-test-17.ogg" #Cheshire (shiena)
    che "Pose1 catmouthsmall flap mouth."

    show che f catmouth

    voice "voice/00-test-18.ogg" #Cheshire (shiena)
    che "Pose1 catmouth flap mouth."

    show che f meh

    voice "voice/00-test-19.ogg" #Cheshire (shiena)
    che "Pose1 meh flap mouth."

    show che f sad

    voice "voice/00-test-20.ogg" #Cheshire (shiena)
    che "Pose1 sad flap mouth."

    show che f scanning

    voice "voice/00-test-21.ogg" #Cheshire (shiena)
    che "Pose1 thinline flap mouth."

    show che f happy

    voice "voice/00-test-22.ogg" #Cheshire (shiena)
    che "Pose1 happy flap mouth."

    show che s catmouth

    voice "voice/00-test-23.ogg" #Cheshire (shiena)
    che "Pose2 catmouth flap mouth."

    show che s meh

    voice "voice/00-test-24.ogg" #Cheshire (shiena)
    che "Pose2 meh flap mouth."

    show che s pout1

    voice "voice/00-test-25.ogg" #Cheshire (shiena)
    che "Pose2 pout1 flap mouth."

    show che s pout2

    voice "voice/00-test-26.ogg" #Cheshire (shiena)
    che "Pose2 pout2 flap mouth."

    show che s thinline

    voice "voice/00-test-27.ogg" #Cheshire (shiena)
    che "Pose2 thinline flap mouth."

    show che s sad

    voice "voice/00-test-28.ogg" #Cheshire (shiena)
    che "Pose2 sad flap mouth."

    scene bg ceiling ceiling empty
    show ceilingfan

    voice "voice/00-test-29.ogg" #Cheshire (shiena)
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

    voice "voice/00-test-30.ogg" #Cheshire (shiena)
    che "Testing transition between sprite to CG."

    show cheshire sad hurt shocked tears ticket with dissolve

    voice "voice/00-test-31.ogg" #Cheshire (shiena)
    che "Oh no poor ches."

    hide cheshire with dissolve
    hide che with dissolve

    call screen hubselect

    return
