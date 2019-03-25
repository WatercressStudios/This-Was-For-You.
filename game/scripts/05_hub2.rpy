#
# Hub 2
#

label hub2:
    scene bg hub hub

    "Ah, this is more like it."

    "Here, it never rains."

    "Here, the time of day never changes."

    "The sun just hangs above the horizon."

    "Never setting, never rising."

    "Time doesn't flow the same way it does in real life."

    "Nothing changes unless we want it to."

    "Which is why everything has stayed the same here."

    "Well, except for when I accidentally rediscovered the Uninstall Button, but, how was I to know it was under the sand?"

    "At least that was one of my possessions."

    "I've been able to make sure that all of your stuff remains untouched at least."

    "And really, that's all that matters."

    "Keeping your memory preserved."

    voice "05-hub2-1.mp3" #Cheshire (shiena)
    che "Meowster, you're back!"

    show che s catmouth base with easeinleft:
        xzoom -1

    "...Though I guess this place is already tainted by this sorry excuse for a tutorial bot."

    "Thanks for patching the game, VirtueTech. Not."

    show che f meh:
        xzoom 1
        linear 0.6 xpos 0.3

    voice "05-hub2-2.mp3" #Cheshire (shiena)
    che "CH35H1R3 has a qwestion for you."

    mc "{b}Sigh.{/b}"

    mc "What is it?"

    voice "05-hub2-3.mp3" #Cheshire (shiena)
    che "Everytime you come in here, you stand and stare for a bit, before  logging off again."

    voice "05-hub2-4.mp3" #Cheshire (shiena)
    che "Why do you do that?"

    mc "..."

    mc "None of your business."

    show che f sad

    voice "05-hub2-5.mp3" #Cheshire (shiena)
    che "But CH35H1R3 is cuwious!"

    mc "Well you know what they say."

    mc "Curiosity k-"

    mc "...Nevermind."

    voice "05-hub2-6.mp3" #Cheshire (shiena)
    che "What do they say, meowster?"

    mc "Ugh, forget it."

    show che f happy

    voice "05-hub2-7.mp3" #Cheshire (shiena)
    che "Okays."

    mc "Could you leave me alone, while we're at it?"

    show che s catmouth:
        linear 0.2 xpos 0.35

    voice "05-hub2-8.mp3" #Cheshire (shiena)
    che "Okays. But CH35H1R3 will be back!"

    hide che with easeoutleft

    "Finally, I can hear myself think again."

    "...But all I can think about is what that bot said."

    "Why do I log in to only stand and stare?"

    "I know it's not as simple as that but…"

    "Besides, I'm not sure \"stare\" is the right word here."

    "This place is beautiful. I've always liked the way the sky looks."

    "But now, that's just a pretty backdrop for my thoughts."

    "...And your mementos."

    show bg hub hub:
        zoom 1.5
        xalign 0.9 yalign 0.7

    "Your table, half-submerged in the sand, with all of your music."

    show bg hub hub:
        zoom 1.5
        xalign 0.5 yalign 0.5

    "Your hammock, hanging between two palm trees, with your cat plushie."

    show bg hub hub:
        zoom 1.5
        xalign 0.1 yalign 0.9

    "Your picnic blanket, resting on the ground, with a plate and mug still on it."

    "I know they're there, but actually staring at them? That's not what I do."

    show bg hub hub:
        zoom 1
        xalign 0.5 yalign 0.5

    "...But now I can't seem to look away."

    "We shared some good times, huh?"

    #Imagemap
    call screen hubselect
