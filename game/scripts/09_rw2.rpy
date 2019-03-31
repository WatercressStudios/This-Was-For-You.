#
# Real World 2
#

label rw2:
    $ save_name = "Sustenance"
    scene black

    pause 1
    show screen chapter_announce

    #Voicemail
    voice "09-rw2-1.ogg" #Dad ()
    dad "Hey kiddo, it's your parents..."
    voice "09-rw2-2.ogg" #Mom ()
    mom "How are you feeling? Have you been eating well?"
    voice "09-rw2-3.ogg" #Dad ()
    dad "You should pick up the phone sometimes. Your mom is worried about you."
    # mom is addressing dad here, not MC, so stern voice?
    voice "09-rw2-4.ogg" #Mom ()
    mom "Honey, you promised not to lecture."
    voice "09-rw2-5.ogg" #Dad ()
    dad "Sorry."
    # gentle voice again, addressing MC
    voice "09-rw2-6.ogg" #Mom ()
    mom "We're thinking about you, sweetie. Make sure you hydrate yourself properly, okay?"
    voice "09-rw2-7.ogg" #Dad ()
    dad "And call us any time, kiddo. You don't have to bottle it up. It's terrible what happened to your internet friend…"
    # Silence for a few seconds as as both parents aren't sure what to say next
    # Said with some hesitation and worry
    voice "09-rw2-8.ogg" #Mom ()
    mom "We love you, sweetie. Take care of yourself, you hear me?"
    voice "09-rw2-9.ogg" #Dad ()
    dad "We'll be here when you're ready. Call us."

    pause 0.5

    play ambient "sfx/Ambience_1_(No_Rain).ogg" fadein 2.0
    play sound "sfx/Fan.ogg" fadein 2.0 loop
    play music "music/RW_S2.ogg" fadein 2.0
    scene bg ceiling ceiling empty
    show ceilingfan
    with dissolve

    "How long has it been since I moved from this bed?"

    "My body feels heavy. Like I'm being pulled down by an anchor."

    "I don't need to go anywhere. The \"scenery\" here isn't too bad."

    "The predictability and periodic nature of the dull fan is comforting."

    "You'd hate this scenery, Ji."

    "You'd search every crook and cranny of that fan to uncover some spontaneity and color."

    "And you'd find it."

    "Just like you had for the people around you."

    "...Even me."

    if persistent.subtitle or config.sound == False:
        sfx "sfx/Stomach_grumble.ogg" "*Grumble*"
    else:
        sfx "sfx/Stomach_grumble.ogg"

    "..."

    "My stomach's been growling for awhile now."

    hide ceilingfan
    show bg bedroombg open:
        zoom 1.1
    with dissolve

    "I roll to the side in an attempt to quell my hunger."

    if persistent.subtitle or config.sound == False:
        sfx "sfx/Stomach_grumble.ogg" "*Grumble*"
    else:
        sfx "sfx/Stomach_grumble.ogg"

    "..."

    "Fine, you win."

    if persistent.subtitle or config.sound == False:
        sfx "sfx/bed.ogg" "*Rustle*"
    else:
        sfx "sfx/bed.ogg"

    show bg bedroombg open:
        linear 0.2 yalign 0.1

    pause 0.5

    show bg ceiling ceiling empty
    show ceilingfan
    with dissolve

    # camera pans up a bit, indicating MC is standing up
    # bg back to the fan, but sfx of MC walking to the kitchen and opening the fridge

    "I head over to my fridge and pull it open, the glow from the fridge illuminating my dark kitchen."

    if persistent.subtitle or config.sound == False:
        sfx "sfx/Fridge_open.ogg" "*Open Fridge*"
    else:
        sfx "sfx/Fridge_open.ogg"

    "Nothing left but a slice of two-day-old pizza."

    "Without bothering to heat it up, I start chewing on the cold, damp crust while walking to the window."

    hide ceilingfan
    show bg bedroombg open:
        zoom 1.5
        xalign 0.9 yalign 0.2
    with dissolve

    pause 0.5

    stop ambient fadeout 1.0
    #get city sounds no rain
    play ambient "sfx/City_Noise.ogg" fadein 2.0 fadeout 3.0
    show bg bedroombg nocurtains with dissolve

    # bg to the zoomed in window without the curtains
    # sfx of more city sounds than fan sounds

    "It doesn't taste of anything. The pizza."

    "If it isn't so easy to get them delivered, I wouldn't have had any in my fridge - I've never liked pizza, even when I was a kid."

    "It's one of the many ways I was different from everyone else growing up."

    "I wasn't the sort of kid who would get excited over a new cartoon or video game."

    "I was the type who'd read novels at home in the lounge with my parents."

    "Or who would help my parents bake pastries and build a doghouse."

    "I liked doing things my parents enjoyed."

    "...Maybe that was why I was so bad at making friends - I had trouble connecting with people my age."

    "Though that changed after I met you, Ji."

    "Your ability to connect with everyone and everything rubbed off on me."

    "Even your curiosity was infectious. My co-worker was surprised when I asked them about their weekend."

    "And now I have a small circle of friends. People I actually like."

    # intentionally present tense. MC will switch to past tense in Item C Real World
    "You're still my best friend, though, despite having never actually met you."

    "..."

    # close curtains and zoom out. sfx of MC getting on bed
    # fan bg, and pause for a second

    stop ambient fadeout 1.0
    play ambient "sfx/Ambience_1_(No_Rain).ogg" fadein 1.0 fadeout 3.0
    play sound "sfx/bed.ogg"
    play sound "sfx/Fan.ogg" fadein 1.0 loop fadeout 3.0

    show bg bedroombg closed with dissolve

    show bg ceiling ceiling empty
    show ceilingfan
    with dissolve

    "I hate this."

    "I hate feeling like this."

    call closeeyes from _call_closeeyes
    scene black with dissolve

    "Shutting my eyes, I try to sleep."

    "But all I can do is think about what the newscaster said a few hours ago."

    "They said that they were giving up on the search."

    "That they've done everything they could."

    "That we may never find..."

    "...No."

    scene bg ceiling ceiling empty
    show ceilingfan
    call openeyes from _call_openeyes
    stop sound fadeout 2.0
    "I can't do this. Not today."



    # Show into VR button
    play sound [ "<silence .5>", "sfx/VR_Button.ogg" ]
    call screen in_game_entervr
    stop music fadeout 1.0
    stop ambient fadeout 1.0


    jump hub3
