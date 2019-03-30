#
# Hub 3
#

label hub3:
    $ save_name = "Forget."
    scene bg hub hub

    pause 1
    show screen chapter_announce

    # sfx of beach louder than usual, to provide contrast with the previous droning sound
    "..."

    "In the years I spent here, I never once wondered:"

    "Why a beach?"

    "You've never said anything about the sea. Not even in passing."

    "Yet, for our VR treehouse, you've chosen this idyllic beach as the backdrop."

    "You even made it sound real, with the rolling waves and the breeze weaving between the trees."

    "Do you like the sea?"

    "I wish I asked you that."

    voice "10-hub3-1.mp3" #Cheshire (shiena)
    che "Meowsterrrrr!!! I missed you!"

    show che f happy at center, height with easeinbottom:
        zoom 1.2 ypos 1.2

    "It leaps out from behind the dresser, pawing at my chest."

    "Why are you even here? You ruin the atmosphere. Where's the off button on this damn thing?"

    "Why can’t I delete it...?"

    show che f sad

    voice "10-hub3-2.mp3" #Cheshire (shiena)
    che "Pweeeeeeease don't ignore mew!"

    show che f meh:
        linear 0.2 zoom 1 ypos 1.05

    "Mew? That doesn't even work! I shove it off, feeling only a little sorry."

    "Before it has a chance to go back in, I hold a hand out."

    mc "Don't touch me."

    voice "10-hub3-3.mp3" #Cheshire (shiena)
    che "But Meeeowster--{nw}"#interrupt

    mc "No."

    show che f sad:
        linear 0.2 zoom 0.9 ypos 1.0

    "CH35H1R3 takes a step back, acting as if it were wounded by my words."

    mc "Please stop pretending to care."

    show che f sad:
        linear 0.2 zoom 1 ypos 1.05

    voice "10-hub3-4.mp3" #Cheshire (shiena)
    che "But I dos!"

    "It takes a nervous step forward, eyes widening into that puppy-dog look."

    mc "I'm sorry, but this isn't a shitty movie; I'm not going to cave no matter how cute you are."

    show che s mehsad:
        linear 0.6 xpos 0.8

    "I move past CH35H1R3, trying my best to forget its existence."

    "Forgetting you would be the obvious choice, wouldn't it? Just forget it all happened?"

    "If only {b}she{/b} were more… forgettable."

    hide che with easeoutright

    "Damn you."

    "Forcing those thoughts away, I look at the items in front of me, and all of the memories that they share."

    #Imagemap
    call screen hubselect
