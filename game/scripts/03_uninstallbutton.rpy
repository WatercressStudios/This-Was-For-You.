#
# Uninstall button scene
#

label uninstallbutton:
    $ save_name = "Uninstall Button"
    show screen chapter_announce
    # sfx of plastic button pressed *click*!
    #sfx "vr_uninstall_click" "click!"

    play music "Music/Uninstall_Button.ogg"

    if persistent.subtitle or config.sound == False:
        sfx "sfx/button.ogg" "*Click*"
    else:
        sfx "sfx/button.ogg"

    play sound "sfx/ping 6.ogg"

    "..."

    "Nope, still here."

    "It's not like I was expecting anything different; if I really wanted to uninstall this VR world, I’d have done it from outside - and done it already."

    "...Specifically, I'd have done it two years ago - when I crafted this button during the 'Create Your First Item' tutorial."

    "So why am I {b}finally{/b} pushing it?"

    if persistent.subtitle or config.sound == False:
        sfx "sfx/button.ogg" "*Click*"
    else:
        sfx "sfx/button.ogg"

    play sound "sfx/ping 6.ogg"
    "..."

    "Still nothing."

    show sunsettitle behind items with dissolve

    "I crafted this button partly because it was amusing, partly in protest of this world; it’s a pale imitation of the real thing, after all."

    "Yes, I was also aware of the irony of creating VR content, in VR, to protest VR..."

    "In all fairness, I was planning to log out right after and let the free trial expire on its own."

    "Too bad my plan was foiled by you, right, Ji-min? You and your judge-y eagle-eyes."

    "Somehow, even from the other end of the beach, you managed to spot all the mistakes in my creation."

    "I didn't even have time to defend my artistic vision before you ran over and snatched it right out my hands, fixing it in the process."

    "You even carved a pretty version of the trashcan icon, replacing my stick-figure."

    "Only after all that did you ask me: ‘why did you make this?’ I remember laughing for a whole minute at that."

    "It was like a scene out of a movie: we were strangers, Ji - yet you ran over and fixed my art like we were friends."

    "And then..."

    hide sunsettitle with dissolve

    "..."

    if persistent.subtitle or config.sound == False:
        sfx "sfx/button.ogg" "*Click*"
    else:
        sfx "sfx/button.ogg"

    play sound "sfx/ping 6.ogg"

    "I push the button again."

    "Yeah."

    "Still nothing."

    if persistent.subtitle or config.sound == False:
        sfx "sfx/run.ogg" "*Running*"
    else:
        sfx "sfx/run.ogg"
    pause 1.0
    show che f happy:
        zoom 2 xpos 0.1

    hide items

    # play comical sfx of someone turning up unexpectedly

    voice "voice/03-uninstallbutton-1.ogg" #Cheshire (shiena)
    che "Maybe the buttons is broken, nya~!"

    mc "Ack!"

    show che f happy:
        linear 0.2 zoom 1 xpos 0.3 ypos 0.05

    mc "What are you-- Why are you…"

    "Why is this {b}thing{/b} back?"

    show che s armsnyan:
        linear 0.2 xpos 0.35

    voice "voice/03-uninstallbutton-2.ogg" #Cheshire (shiena)
    che "Nyahaha! Maybe Master is the one who's broken~"

    "Stop."

    "Don't respond to it."

    "It's just a computer program."

    show che s sad

    voice "voice/03-uninstallbutton-3.ogg" #Cheshire (shiena)
    che "Meowster? Has your code crashed?"

    # screenshake and whip sfx, indicating MC has snapped

    show bg hub hub:
        linear 0.2 zoom 1.05
    show che s sad:
        linear 0.2 zoom 1.05
    with hpunch

    mc "Weren't you supposed to be gone for 30 minutes!?"

    show bg hub hub:
        linear 0.2 zoom 1

    show che s default base:
        linear 0.2 zoom 1

    voice "voice/03-uninstallbutton-4.ogg" #Cheshire (shiena)
    che "But Master is having trouble, so CH35H1R3 came to help, meow!"

    hide che
    show items uninstallbutton
    with dissolve

    if persistent.subtitle or config.sound == False:
        sfx "sfx/button.ogg" "*Click*"
    else:
        sfx "sfx/button.ogg"

    play sound "sfx/ping 6.ogg"

    "I try to ignore it."

    pause 0.1

    if persistent.subtitle or config.sound == False:
        sfx "sfx/button.ogg" "*Click*"
    else:
        sfx "sfx/button.ogg"

    play sound "sfx/ping 6.ogg"

    pause 0.5

    if persistent.subtitle or config.sound == False:
        sfx "sfx/button.ogg" "*Click*"
    else:
        sfx "sfx/button.ogg"

    play sound "sfx/ping 6.ogg"

    pause 0.5

    if persistent.subtitle or config.sound == False:
        sfx "sfx/button.ogg" "*Click*"
    else:
        sfx "sfx/button.ogg"

    play sound "sfx/ping 6.ogg"

    pause 0.5

    hide items uninstallbutton
    show che s:
        xpos 0.35 ypos 0.05
    with dissolve

    voice "voice/03-uninstallbutton-5.ogg" #Cheshire (shiena)
    che "Meow-be Master needs to connect the button to a function~"

    show che s catmouthclosed armsnyan

    voice "voice/03-uninstallbutton-6.ogg" #Cheshire (shiena)
    che "Master can make it do all sorts of useful things, nya!"

    mc "Can it delete you?"

    show che f happy:
        linear 0.2 xpos 0.3

    voice "voice/03-uninstallbutton-7.ogg" #Cheshire (shiena)
    che "Oh, CH35H1R3 has a great idea: it can {b}summon{/b} me!"

    "Oh hell no. Anything but that."

    show che s armsnyan:
        xzoom -1
        linear 0.2 xpos 0.25

    # ches looks confused
    voice "voice/03-uninstallbutton-8.ogg" #Cheshire (shiena)
    che "Nya? Is Master trying to delete the button? Want some help?"

    "I cradle the button against my chest instinctively, as if the bot will snatch it out of my hands."

    mc "No."

    show che s sad

    "The program stares at me, confused; its algorithms are clearly having trouble parsing my behaviour."

    "{b}I'm{/b} having trouble parsing my behaviour."

    "Why am I still so protective of this? Is it because it’s the first thing we made together?"

    "...Because it’s the thing that started our friendship?"

    show sunsettitle with dissolve:
        alpha 0.8

    "You were {b}aghast{/b} when I finally explained what my Uninstall Button was for - as if you had never met anyone so cynical in your life."

    "So I returned day after day, creating more cynical items just for you; in return, you'd create the silliest things."

    "We'd critique each other's creations for hours. Over time, our perspectives on life changed."

    "For years, we kept up with that tradition, until..."

    if persistent.subtitle or config.sound == False:
        sfx "sfx/button.ogg" "*Click*"
    else:
        sfx "sfx/button.ogg"

    play sound "sfx/ping 6.ogg"

    "..."

    play sound [ "<silence .5>", "sfx/VR_Button.ogg" ]


    # Ding! Voicemail from work arrived. MC logs out into the real world

    call screen in_game_exitvr
    stop ambient fadeout 1.0
    stop music fadeout 1.0


    jump rw1
