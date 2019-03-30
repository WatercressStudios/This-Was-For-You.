#
# Hub 1 scene
#

label hub1:
    $ save_name = "Imitation"
    scene bg hub hub
    show screen chapter_announce

    play ambient "sfx/Hub_Beach.ogg" fadein 3.0 fadeout 3.0
    play music "Music/Hub.ogg" fadein 3.0 fadeout 3.0

    "The familiar scent of an ocean breeze hits my nose first."

    "The warm rays of sunshine envelops my body soon after."

    "In my mind, I know it's nothing but lines of code, manufactured to simulate some idyllic beach."

    "But I don't care. This place, for me, is not that simple."

    "It's where I was able to see you, talk with you."

    "Where neither time zones, nor borders stood in the way of our friendship."

    "This wasn't just where we built some virtual house together."

    "No. This was… our home."

    "And now, I'm not sure what to call it."

    "I'm not entirely sure what this place even means to me anymore."

    "Yet, I always find myself back here."

    "Staring at what used to be."

    "Staring at-"

    show che s catmouth armsnyan at center, height with easeinright

    #Cheshire slides onto screen with a happy expression

    voice "02-hub1-1.ogg" #Cheshire (shiena)
    che "Nya!"

    mc "Ahh!"

    "My surprise quickly makes way for irritation."

    show che f catmouthclosed armsforward

    voice "02-hub1-2.ogg" #Cheshire (shiena)
    che "Welcome home, master!"

    "Ugh. This thing again."

    "Some kind of tutorial bot that VirtueTech added in recently."

    "At least that's the only explanation I have, anyway."

    show che f meh base

    "I haven't exactly been looking at the patch notes, and I can’t say that I remember the program updating."

    "Even so, I distinctly remember that this bot appeared about a month ago."

    show che f mehsad

    "How could I forget?"

    "After all, it was the first time I logged in after {b}that.{/b}"

    show che f sad

    voice "02-hub1-3.ogg" #Cheshire (shiena)
    che "Is meowster ignoring me?"

    "I'm trying to at least."

    "W-Wait, meowster?"

    show che f happy

    "Ugh, I just gave it the attention it wants, didn't I?"

    show che s meh:
        xzoom -1
        linear 0.6 xpos 0.2

    "Scowling, I walk away in the opposite direction."

    show che f sad:
        xzoom 1
        linear 0.6 xpos 0.5

    voice "02-hub1-4.ogg" #Cheshire (shiena)
    che "Meowster, pwease wait for me!"

    "Pwease!?"

    "This bot keeps getting worse and worse!"

    mc "What do you want?"

    voice "02-hub1-5.ogg" #Cheshire (shiena)
    che "To spend time with {b}you,{/b} meowster!"

    mc "Why?"

    voice "02-hub1-6.ogg" #Cheshire (shiena)
    che "So master won't be lonely."

    mc "Look. I don't need your company. I came here to be alone with my thoughts. The last thing I need is-"

    "Wait. Why am I treating this bot like an actual person?"

    "I'm talking to lines of code that don't have intent or reason."

    "Only an algorithm given human form VirtueTech thought was amusing enough to include in their software."

    "Well, that's a bit of a stretch. I don't know anyone who would behave so childishly or say words like 'meowster' and 'pwease'."

    "...Except for when you were feeling particularly mischievous."

    mc "Just, don't you have any other tasks to do? Some newbie to bother?"

    show che f meh

    voice "02-hub1-7.ogg" #Cheshire (shiena)
    che "Newbie?"

    "How did they manage to create a bot that doesn't know what ‘newbie’ means?"

    "I really am wasting my time speaking with this thing, huh?"

    show che s mehsad:
        linear 0.6 xpos 0.8

    "At this stage I'm resigned to the fact that it'll follow me around, but not having to see that bright neon face for a few moments works wonders."

    "I idly kick aside some sand. Sand and, was that a seashell?"

    show che f meh:
        linear 0.6 xpos 0.5

    voice "02-hub1-8.ogg" #Cheshire (shiena)
    che "Nya! You dropped something!"

    mc "What?"

    "Before I can even turn around, something is shoved towards me."

    show che f happy
    show cheshire with dissolve

    "A round, bright-red button with a trash can icon right in the middle."

    "Huh. I haven't seen {b}this{/b} in a while."

    voice "02-hub1-9.ogg" #Cheshire (shiena)
    che "Meowster should take it!"

    hide cheshire with dissolve

    "I grab it. I'm not too sure why."

    "Well, I suppose some pretty strong memories are attached to it."

    mc "Thanks."

    show che f hearteyesmf

    "I realise my mistake too late."

    voice "02-hub1-10.ogg" #Cheshire (shiena)
    che "Master thanked me? Wow!"

    show che f catmouth

    mc "Don't think about it too hard."

    "Of course, not that it could think to begin with."

    hide che
    show items uninstallbutton
    with dissolve

    "Glad for the momentary distraction, I look down at the button in my palm."

    hide items uninstallbutton
    show che f catmouth at center, height
    with dissolve

    mc "Hey. Since you're so happy with me and everything, could you do me a favour?"

    "Why am I even asking it so nicely?"

    show che f armsforward

    voice "02-hub1-11.ogg" #Cheshire (shiena)
    che "What does master want CH35H1R3 to do?"

    mc "Could you leave me alone for about… 30 minutes?"

    voice "02-hub1-12.ogg" #Cheshire (shiena)
    che "Master was mean to me earlier so, only if you say pwetty pwease!"

    mc "{b}Sigh.{/b}"

    mc "Pretty please."

    voice "02-hub1-13.ogg" #Cheshire (shiena)
    che "..."

    mc "..."

    voice "02-hub1-14.ogg" #Cheshire (shiena)
    che "..."

    mc "...pwetty pwease."

    show che s armshappy:
        linear 0.2 xpos 0.55

    voice "02-hub1-15.ogg" #Cheshire (shiena)
    che "Okays!"

    hide che with easeoutleft

    "That's what it takes to get it to leave?"

    "Does VirtueTech want to humiliate their user base or something?"

    "Well, at least the bot's gone."

    "Might as well make the most of this peace."

    show items uninstallbutton with dissolve
    stop music
    jump uninstallbutton
