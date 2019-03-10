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
    MapEmote('che f sad',  'che base md_sad ed_sad brow_sad glasses_default')
    MapEmote('che f scanning',  'che armsscanning md_thinline e_none brow_grumpy shadows glasses_gendo')

# override some default mouth flap behaviours
image che_md_sad = FlapMouth("che_mc_sad", "che_m_shocked")


# The game starts here.

label start:
    show screen in_game_menu

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show che f sad

    # These display lines of dialogue.

    che "Hover your mouse over MENU to test."

    show screen in_game_entervr

    che "Hover your mouse over ENTER VR and press to test."

    hide screen in_game_entervr
    hide screen in_game_entervr_showing

    show screen in_game_exitvr

    che "Hover your mouse over EXIT VR and press to test."

    hide screen in_game_exitvr
    hide screen in_game_exitvr_showing

    che "Demo ends after this line."

    hide screen in_game_entervr

    # This ends the game.

    return
