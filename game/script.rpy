# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


# The game starts here.

label start:
    show screen in_game_menu

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    scene ceiling empty
    show ceilingfan

    "Ceiling fan animation."

    scene bedroom open dark

    "Bedroom with open curtains during the blackout."

    show bedroomlightning dark

    "Bedroom with lightning during the blackout."

    scene bedroom open

    "Bedroom with open curtains."

    show bedroomlightning

    "Bedroom with lightning."

    "Demo ends after this line."

    return
