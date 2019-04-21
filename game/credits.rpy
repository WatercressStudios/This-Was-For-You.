#
# Generate credits screen based on parameters below
#

init python:
    credits_duration = 50.0
    credits_height = 6800
    credits_content = [
        ( "Dedicated to @TKia_ (Electro), InstantRiot",
            [
            ]
        ),
        ( "Developed for NaNoRenO 2019.",
            [
            ]
        ),
        ( "Story Outline",
            [
                "Tristan 'Wolf' Barber",
                "Sagittaeri",
                "Alison 'Draz' Huang",
                "Happiness+",
            ]
        ),
        ( "Writing",
            [
                (
                    "Memories of You",
                    "Alison 'Draz' Huang",
                ),
                (
                    "Imitation",
                    "Alison 'Draz' Huang",
                ),
                (
                    "Uninstall Button",
                    "Sagittaeri",
                ),
                (
                    "The World Keeps Turning",
                    "Alison 'Draz' Huang",
                    "Happiness+",
                ),
                (
                    "Preservation",
                    "Alison 'Draz' Huang",
                ),
                (
                    "You Were so Strong.",
                    "Tristan 'Wolf' Barber",
                ),
                (
                    "Apologies",
                    "Alison 'Draz' Huang",
                ),
                (
                    "Our Song",
                    "Sagittaeri",
                    "Happiness+",
                ),
                (
                    "Sustenance",
                    "Sagittaeri",
                ),
                (
                    "Forget",
                    "Tristan 'Wolf' Barber",
                    "Sagittaeri",
                ),
                (
                    "Only The Good Die Young.",
                    "Tristan 'Wolf' Barber",
                ),
                (
                    "The Gift",
                    "Sagittaeri",
                    "Tristan 'Wolf' Barber",
                ),
                (
                    "Friendships",
                    "Sagittaeri",
                ),
                (
                    "What Could Have Been.",
                    "Tristan 'Wolf' Barber",
                ),
                (
                    "I Miss You.",
                    "Tristan 'Wolf' Barber",
                ),
            ]
        ),
        ( "Editing",
            [
                "Tristan 'Cipher' Hallihan",
                "TheAlchemyst",
                "Virginia 'Ginger' Doran",
                "Sagittaeri",
                "Alison 'Draz' Huang",
                "Tristan 'Wolf' Barber",
            ]
        ),

        ( "Audio",
            [
                (
                    "Music",
                    "Kierious",
                    "Paul Robins",
                    "Speedy",
                    "Raymond 'raydee99' Demers",
                ),
                (
                    "Sound Design",
                    "Paul Robins",
                    "Speedy",
                ),
                (
                    "VA Line Splicing",
                    "Alison 'Draz' Huang",
                    "Happiness+",
                    "Speedy",
                ),
            ]
        ),

        ( "Art",
            [
                (
                    "Sprite",
                    "Dean 'AnagramDaine' Lewthwaite",
                ),
                (
                    "CG",
                    "Alison 'Draz' Huang",
                ),
                (
                    "UI",
                    "Megan Uosiu",
                ),
                (
                    "Background",
                    "Dean 'AnagramDaine' Lewthwaite",
                    "Alison 'Draz' Huang",
                ),
                (
                    "VFX",
                    "Dean 'AnagramDaine' Lewthwaite",
                ),
                (
                    "Logo",
                    "Chiba Kenta",
                ),
            ]
        ),

        ( "Code",
            [
                (
                    "UI",
                    "Sagittaeri",
                    "Alison 'Draz' Huang",
                    "Happiness+",
                ),
                (
                    "Tools",
                    "Sagittaeri",
                ),
            ]
        ),

        ( "Ren'py Scripting",
            [
                (
                    "Logic",
                    "Sagittaeri",
                ),
                (
                    "Visual",
                    "Alison 'Draz' Huang",
                ),
                (
                    "Audio",
                    "Paul Robins",
                ),
                (
                    "Effects",
                    "Alison 'Draz' Huang",
                    "Dean 'AnagramDaine' Lewthwaite",
                    "Sagittaeri",
                ),
            ]
        ),

        ( "Voice Direction",
            [
                "Sandra 'SandraMJ' Molina",
            ]
        ),
        ( "Voice Overs",
            [
                (
                    "CH35H1R3",
                    "Shiena",
                ),
                (
                    "Ji-min",
                    "Ariane 'Starleeter' Marchese",
                ),
                (
                    "Boss",
                    "Bryce Buckley",
                ),
                (
                    "Mom",
                    "Kenkoy",
                ),
                (
                    "Dad",
                    "Adam Warren",
                ),
                (
                    "Cafe owner",
                    "Amanda Hufford",
                ),
                (
                    "Friend 1",
                    "Kenneth Faircloth",
                ),
                (
                    "Friend 2",
                    "Siddharta Villanueva",
                ),
                (
                    "Friend 3",
                    "DJ Horn",
                ),
            ]
        ),

        ( "Marketing",
            [
                "Caitie",
                "Tim",
                "TheAlchemyst",
            ]
        ),
        ( "Trailer",
            [
                (
                    "Video Editing",
                    "TheAlchemyst",
                ),
                (
                    "Soundtrack",
                    "Speedy",
                ),
            ]
        ),

        ( "Special thanks to",
            [
                "Ren'py Tom",
                "The Lemmasoft Forum",
                "Our Fans",
            ]
        ),
        ( "A thank you to all of our Patrons, including",
            [
                "Merritt Barber",
                "Jonas Lee",
                "TheAlchemyst",
            ]
        ),
    ]

transform credits_roll(duration, dest):
    on show:
        alpha 0 pos (0, 0)
        parallel:
            linear duration ypos -dest
        parallel:
            linear 1 alpha 1
    on hide:
        linear 1 alpha 0

screen credits():
    timer credits_duration-2 action Hide("credits")
    key "dismiss" action Hide("credits")
    frame at credits_roll(credits_duration, credits_height):
        background "#000"
        xsize 1920
        vbox:
            xalign 0.5
            null height 500
            for title, names in credits_content:
                null height 50
                text title:
                    text_align 0.5
                    xalign 0.5
                    font "BebasNeue-Regular.otf"
                    size 50
                    color "#7ECBDD"
                for name in names:
                    if type(name) == type(()):
                        hbox:
                            xalign 0.5
                            frame:
                                background None
                                padding (0,0,0,0)
                                margin (0,0,0,0)
                                xsize 900
                                text name[0]:
                                    text_align 1.0
                                    xalign 1.0
                                    font "Arial Bold.ttf"
                                    size 30
                                    color "#fff"
                            null width 50
                            frame:
                                background None
                                padding (0,0,0,0)
                                margin (0,0,0,0)
                                xsize 900
                                vbox:
                                    for n in name[1:]:
                                        text n:
                                            text_align 0.0
                                            xalign 0.0
                                            font "Arial Bold.ttf"
                                            size 30
                                            color "#fff"
                    else:
                        text name:
                            text_align 0.5
                            xalign 0.5
                            font "Arial Bold.ttf"
                            size 30
                            color "#fff"
            null height 5000
