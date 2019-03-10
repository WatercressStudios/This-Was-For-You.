# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:
    show screen in_game_menu

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

    e "Will test the Hub selection now."

    hide screen in_game_entervr

    show hub

    # This ends the game.
    call screen hubselect

    e "Demo ends after this line."

    return
