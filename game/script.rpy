# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


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
    
    show vrhelmet:
        xalign 0.5 yalign 1.3 alpha 1.0 zoom 0.8
        linear 1.0 xalign 0.5 yalign 1.0 alpha 1.0 zoom 0.8
        linear 2.0 xalign 0.5 yalign 0.09 alpha 1.0 zoom 0.8
        linear 1.0 xalign 0.5 yalign 0.09 alpha 1.0 zoom 0.99
        linear 1.0 xalign 0.5 yalign 0.09 alpha 0.5 zoom 0.99
    

    show eileen happy with Dissolve(2.0)
    


    # These display lines of dialogue.

    e "Hover your mouse over MENU to test."

    show screen in_game_entervr

    e "Hover your mouse over ENTER VR and press to test."
    

    hide screen in_game_entervr
    hide screen in_game_entervr_showing

    show screen in_game_exitvr

    e "Hover your mouse over EXIT VR and press to test."

    hide screen in_game_exitvr
    hide screen in_game_exitvr_showing

    e "Demo ends after this line."

    hide screen in_game_entervr

    # This ends the game.

    return
    
# Enjoy Anagrams broken code

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
    
