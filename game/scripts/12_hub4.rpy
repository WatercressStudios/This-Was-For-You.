#
# Hub 4
#

label hub4:
    $ save_name = "The Gift"
    scene bg hub hub

    pause 1

    "Here we are again."

    show che f at center:
        ypos 2
        linear 2.8 ypos 1.6

    "The waves lapping against the shore calm me, as they alwa--{nw}" #interrupt function I forget how

    mc "Stop right there."

    show che f meh

    voice "12-hub4-1.mp3" #Cheshire (shiena)
    che "Nya?"

    show che f catmouth:
        linear 0.6 ypos 1.05

    # ches slides in shakily and slowly from the bottom

    voice "12-hub4-2.mp3" #Cheshire (shiena)
    che "Ehehehe, master found out~!"

    "I'm so used to it now that I'm starting to predict when this thing is about to jump scare me."

    mc "Can't you just, I don't know, walk up to your players like a normal person?"

    "I know, I realise how stupid I sound as soon as I said it. That thing's not a person. It's a cat."

    "{b}A bot!{/b} I mean it's a bot."

    "...dammit, it's really fucking with my head."

    show che f catmouthclosed

    voice "12-hub4-3.mp3" #Cheshire (shiena)
    che "But I likes giving master gifts!"

    mc "Gifts? What gifts?"

    show che s catmouth armsnyan:
        linear 0.2 xpos 0.55

    voice "12-hub4-4.mp3" #Cheshire (shiena)
    che "My happy surprises! Nya~! Meowster looooves surprises, right?"

    mc "...Happy surprises?"

    "Wait…by {b}surprises{/b}, did it mean the {b}jump scares{/b}?"

    show che f:
        linear 0.2 xpos 0.5

    voice "12-hub4-5.mp3" #Cheshire (shiena)
    che "The gift is me surprising master! Does master likes it?"

    show che f:
        zoom 1.05

    show bg hub hub with hpunch:
        zoom 1.05

    mc "So you’ve been doing it on purpose?!"

    show bg hub hub:
        linear 0.2 zoom 1

    show che f:
        linear 0.2 zoom 1

    mc "...Ugh, what am I doing, shouting at a…"

    mc "Look, just stop, okay? I don't want any 'gifts'. Turn off gift mode!"

    show che f sad

    voice "12-hub4-6.mp3" #Cheshire (shiena)
    che "..."

    mc "W-What?"

    "It doesn't say anything and it just sniffs. Is it… crying?"

    show che s catmouth armshappy:
        xzoom -1
        linear 0.2 xpos 0.45

    voice "12-hub4-7.mp3" #Cheshire (shiena)
    che "Ehehehe, meowster fell for it~!"

    mc "..."

    "What's wrong with you VirtueTech? Why is your tutorial bot emotionally blackmailing your players?"

    hide che with easeoutleft

    "Screw this. I turn around and rest my eyes on the scenery."

    "Soon, I'm filled with a sense of calm."

    "My gaze slowly shifts to one of the things we've made. Do you remember about this, Ji?"

    "As I reach out for it, I hear a sniff behind me."

    show che f sad at left, height with easeinleft

    # ches sound slightly more human-like suddenly for this line
    voice "12-hub4-8.mp3" #Cheshire (shiena)
    che "Master...I don't understand why do you keep ignoring me like--"

    mc "Nice try, but I’m not falling for that again."

    show che f happyclosed

    voice "12-hub4-9.mp3" #Cheshire (shiena)
    che "Nya~"

    "Someone at VirtueTech has way too much time in their hands."

    show che f happy

    voice "12-hub4-10.mp3" #Cheshire (shiena)
    che "Does master wants to be left alone this time, too?"

    "I nod while waving it away impatiently."

    show che f happy armsscanning

    voice "12-hub4-11.mp3" #Cheshire (shiena)
    che "CH3SH1R3 is on the case~!"

    hide che with easeoutleft

    "..."

    #Imagemap
    call screen hubselect
