#
# Real World 3
#

label rw3:
    $ save_name = "Only The Good Die Young."
    scene black

    pause 1
    show screen chapter_announce

    ##"Good People Always Die First."
    ##Voicemail
    voice "voice/11-rw3-1.ogg" #Cafe Owner (Amanda Hufford)
    if persistent.subtitle or config.sound == False:
        caf "Hey, it’s been a while since I’ve seen ya at the cafe; I just thought I’d check in."
    else:
        "{nw}"
    voice "voice/11-rw3-2.ogg" #Cafe Owner (Amanda Hufford)
    if persistent.subtitle or config.sound == False:
        caf "I know things are rough right now - lord, that’s the understatement of the century, isn’t it? When my brother died…"
    else:
        "{nw}"
    voice "voice/11-rw3-3.ogg" #Cafe Owner (Amanda Hufford)
    if persistent.subtitle or config.sound == False:
        caf "Well, they say it gets better - but it doesn’t. You just kinda… learn to deal with it, I guess?"
    else:
        "{nw}"
    voice "voice/11-rw3-4.ogg" #Cafe Owner (Amanda Hufford)
    if persistent.subtitle or config.sound == False:
        caf "Well, we’re here for ya; you’re more than just a regular: you’re family!"
    else:
        "{nw}"
    voice "voice/11-rw3-5.ogg" #Cafe Owner (Amanda Hufford)
    if persistent.subtitle or config.sound == False:
        caf "If ya need anything, just give me a call, a text - whatever floats your boat. Drinks are on me for however long you need, okay?"
    else:
        "{nw}"

    pause 0.5

    $ visible_emails.append('family')
    $ visible_emails.append('friend4')
    $ visible_emails.append('friend5')
    show screen notify("You have unread emails.")

    scene bg ceiling ceiling empty
    show ceilingfan
    with dissolve

    play music "music/RW_S3.ogg" fadein 3.0
    play ambient "sfx/Ambience_1_(No_Rain).ogg" fadein 3.0
    play sound "sfx/Fan.ogg" fadein 5.0 loop

    "I can almost feel it, you know?"

    "The bitter aroma of coffee, the clinking of mugs, the gentle murmur of polite guests, the soothing lights warming up the place - all of it."

    "You'd always sit next to me and just… chat. About everything and nothing, really."

    "I remember feeling so bad for my awkwardness, since I didn’t really know what to say when you first sat down."

    "I wasn't expecting a business owner to care; I came to learn that you treat it all as a hobby, for fun, as a community, rather than a business."

    "The culture of it all, that’s how you succeeded. It was a place to belong, not a place to buy merchandise; it's a place that cares."

    call closeeyes from _call_closeeyes_1
    scene black with dissolve

    "Drinks on you…"

    "I know how rough that'd be. Your business isn't exactly bustling and most of us customers are regulars."

    "{b}Us{/b} regulars. Yeah right."

    "I used to go there every day, work on some ideas, enjoy the quiet comfort, and talk to Ji on my laptop."

    "God, I wish she could’ve seen it; you would have loved her - and she would have loved you."

    "She was that type of person."

    "She was; she really, really was."

    "We would have sat in that booth from sunup to sundown, chatting and chatting. Like I said, about anything at all."

    "It would have been wonderful to get out of that damned VR world."

    "Honestly, I used to dream of the day we'd meet in person and enjoy something ‘real’ for once."

    "That place - the experiences I made - I don't think I ever really appreciated them."

    "I was a bit cynical, paying too much heed to what's real and what's not…"

    "But I loved it all the same."

    scene bg ceiling ceiling empty
    show ceilingfan
    call openeyes from _call_openeyes_2

    "Now I can't even tell what day of the week it is."

    "Everything's the same shade of grey, the days growing into an amorphous blob of incongruity."

    "Is it 5 AM or 5 PM? Dawn or dusk? Day or night? I can't tell."

    "But free drinks {b}do{/b} sound nice. No one else made my drink quite like you did."

    "I wish I could go, but I can't - not even with that well-meaning bribe."

    "Why are you so willing to sacrifice that for me? For us? Why are you so kind!?"

    "I'd only be a burden; I'd hurt {b}you{/b} and everyone else."

    "As much as I used to love going to your cafe… I'm not really worth that."

    "I'm sorry that I haven't been around - I really am."

    "And I'm sorry that I won't be telling you how much I care right now. Maybe I'll take the trip later…"

    "I guess I’ll get around to it eventually if nothing else."

    hide ceilingfan
    show bg bedroombg open
    with dissolve

    stop sound fadeout 2.0

    "I'm taken back to my room, suddenly feeling very cold and {b}very{/b} alone in the darkness."

    "A sliver of moonlight shines through a slit in the curtains onto my desk - or is that sunlight?"

    "On second thought, {b}I don't care.{/b}"

    "The headset gently glows in the dim light, pulsing in and out, illuminating all of my VR equipment."

    "Why do all of the good people have to die!?"

    "The universe is cold and uncaring, unfair and cruel - but I know that's not true."

    "The universe is unbiased."

    "It doesn't have any opinion one way or the other, it doesn't pretend that it has goals."

    "It just exists, nothing more and nothing less."

    "It's empty, hollow, a set of rules and logic and laws, just like CH35H1R3."

    "Shitty things happen to good people."

    "And all good people die eventually."

#    "To the universe, that’s the same as crushing an ant."

    #enter VR?
    #yes
    #end scene

    play sound [ "<silence .5>", "sfx/VR_Button.ogg" ]

    call screen in_game_entervr
    stop music fadeout 1.0
    stop ambient fadeout 1.0

    jump hub4
