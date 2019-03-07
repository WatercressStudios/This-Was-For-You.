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

    show eileen happy

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
