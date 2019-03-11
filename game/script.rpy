# The script of the game goes in this file.

# callback=speaker is needed for mouth flaps
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
    MapEmote('che f happy',  'che base md_default ed_default brow_default glasses_default')
    MapEmote('che f relaxed',  'che base md_default ed_relaxed brow_relaxed glasses_default')
    MapEmote('che f sad',  'che base md_sad ed_sad brow_sad glasses_default')
    MapEmote('che f scanning',  'che armsscanning md_thinline ec_default brow_grumpy shadows glasses_gendo')

# override some default mouth flap behaviours
image che_md_sad = FlapMouth("che_mc_sad", "che_m_shocked")

# override some default blinking behaviours

image che_ed_relaxed = blinkeyes("che_e_default", "che_ec_relaxed")
image che_ed_sad = blinkeyes("che_e_sad", "che_ec_relaxed")


# The game starts here.

label start:
    show screen in_game_menu
    scene bg room
    show che f sad

    che "Hover your mouse over MENU to test."

    show che f happy
    show screen in_game_entervr

    che "Hover your mouse over ENTER VR and press to test."

    hide screen in_game_entervr
    hide screen in_game_entervr_showing
    show screen in_game_exitvr

    che "Hover your mouse over EXIT VR and press to test."

    hide screen in_game_exitvr
    hide screen in_game_exitvr_showing

    che "Testing hub items chooser now."

    hide screen in_game_entervr

    show hub with dissolve

    # This ends the game.
    call screen hubselect

    che "Demo ends after this line."

    return
