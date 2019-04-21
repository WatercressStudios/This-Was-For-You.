#
# Generate credits screen based on parameters below
#

init python:
    credits_duration = 50.0
    credits_height = 8400
    credits_content = [
        ( "Dedicated to @TKia_ (Electro), InstantRiot",
            [
            ]
        ),
        ( "Developed for NaNoRenO 2019.",
            [
            ]
        ),
        ( "Writing",
            [
                "Tristan 'Wolf' Barber",
                "Sagittaeri",
                "Alison 'Draz' Huang",
                "Happiness+",
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
        ( "Music",
            [
                "Kierious",
                "Paul Robins",
                "Speedy",
                "Raymond 'raydee99' Demers",
            ]
        ),
        ( "Sound Design",
            [
                "Paul Robins",
                "Speedy",
            ]
        ),
        ( "VA Line Splicing",
            [
                "Alison 'Draz' Huang",
                "Happiness+",
                "Speedy",
            ]
        ),
        ( "Art Lead",
            [
                "Alison 'Draz' Huang",
            ]
        ),
        ( "Sprite Art",
            [
                "Dean 'AnagramDaine' Lewthwaite",
            ]
        ),
        ( "CG Art",
            [
                "Alison 'Draz' Huang",
            ]
        ),
        ( "UI Art+Design",
            [
                "Megan Uosiu",
            ]
        ),
        ( "Background Art",
            [
                "Dean 'AnagramDaine' Lewthwaite",
                "Alison 'Draz' Huang",
            ]
        ),
        ( "VFX",
            [
                "Dean 'AnagramDaine' Lewthwaite",
            ]
        ),
        ( "Logo Art",
            [
                "Chiba Kenta",
            ]
        ),
        ( "Code Lead",
            [
                "Sagittaeri",
            ]
        ),
        ( "UI Code",
            [
                "Sagittaeri",
                "Alison 'Draz' Huang",
                "Happiness+",
            ]
        ),
        ( "Tools Code",
            [
                "Sagittaeri",
            ]
        ),
        ( "Technical Art",
            [
                "Alison 'Draz' Huang",
                "Dean 'AnagramDaine' Lewthwaite",
            ]
        ),
        ( "Scripters",
            [
                "Alison 'Draz' Huang",
                "Sagittaeri",
                "Paul Robins",
            ]
        ),
        ( "Voice Direction",
            [
                "Sandra 'SandraMJ' Molina",
            ]
        ),
        ( "CH35H1R3 VA",
            [
                "Shiena",
            ]
        ),
        ( "Ji-min VA",
            [
                "Ariane 'Starleeter' Marchese",
            ]
        ),
        ( "Boss VA",
            [
                "Bryce Buckley",
            ]
        ),
        ( "Mom VA",
            [
                "Kenkoy",
            ]
        ),
        ( "Dad VA",
            [
                "Adam Warren",
            ]
        ),
        ( "Cafe owner VA",
            [
                "Amanda Hufford",
            ]
        ),
        ( "Friend 1 VA",
            [
                "Kenneth Faircloth",
            ]
        ),
        ( "Friend 2 VA",
            [
                "Siddharta Villanueva  ",
            ]
        ),
        ( "Friend 3 VA",
            [
                "DJ Horn",
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
                "TheAlchemyst",
            ]
        ),
        ( "Trailer Soundtrack",
            [
                "Speedy",
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
                    text name:
                        text_align 0.5
                        xalign 0.5
                        font "Arial Bold.ttf"
                        size 30
                        color "#fff"
            null height 5000
