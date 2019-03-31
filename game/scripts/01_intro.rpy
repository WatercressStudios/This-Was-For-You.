#
# Intro scene
#

label intro:
    scene black
    show screen chapter_announce
    #Voicemail
    voice "01-intro-1.ogg" #Ji-min ()
    min "Heyyy. It's meee."
    voice "01-intro-2.ogg" #Ji-min ()
    min "I know I should be sleeping but I'm too excited, you know?"
    voice "01-intro-3.ogg" #Ji-min ()
    min "Hope I didn't wake you up!"
    voice "01-intro-4.ogg" #Ji-min ()
    min "Er, what time is it over there again?"
    voice "01-intro-5.ogg" #Ji-min ()
    min "Whatever you're doing, I hope it's going well!"
    voice "01-intro-6.ogg" #Ji-min ()
    min "I think I've talked for long enough, hehe."
    voice "01-intro-7.ogg" #Ji-min ()
    min "See you tomorrow!"

    pause 0.5

    $ visible_emails.append('funeral')
    $ visible_emails.append('friend1')
    $ visible_emails.append('spam1')
    show screen notify("You have unread emails.")

    scene bg ceiling ceiling empty
    show ceilingfan
    with dissolve

    play sound "sfx/Fan.ogg" fadein 4.0 loop
    play ambient "sfx/Ambience_1_(No_Rain).ogg" fadein 3.0 fadeout 3.0
    play music "music/RW_Intro.ogg" fadein 3.0 fadeout 3.0

    "Even now, I’m still replaying your voicemail."

    "I'm not entirely sure why."

    "Am I trying to honor your memory, or punish myself?"

    "Maybe it's both."

    "Sometimes I try and convince myself that I should stop."

    "But then I find myself back here again."

    "I must have played it at least 30 times by now."

    "Not that I'm counting."

    "Not that I want to, at least."

    "There's nothing else to mark the passage of time, nothing else to think about."

    "There's only you."

    "God, that sounds so fucking sappy."

    "Something more like what you'd say."

    "Like insisting we promise to be friends forever, even if we're both grown adults."

    "...Way to break a promise, Ji."

    "I really do miss you, you know."

    "Well... I guess you wouldn't know, would you?"

    "Ugh."

    call closeeyes from _call_closeeyes_3
    scene black with dissolve

    "I keep my eyes shut tightly."

    "Still, the sleep I desperately crave doesn't come."

    "Even listening to the hum of the ceiling fan can’t distract me."

    "My thoughts are pervasive, waves of emotion constantly crashing into my subconscious."

    stop sound fadeout 2.0

    scene bg bedroombg
    call openeyes from _call_openeyes_4

    play sound "sfx/bed.ogg"

    "Pushing my thin blanket aside, I prop myself up to a sitting position."

    "Maybe I'll pour myself a glass of water."

    "That will help, right?"

    show bg bedroombg:
        linear 0.2 zoom 1.1 yalign 0.1

    pause 0.5
    play sound "sfx/Bed_Rustle.ogg"
    show bg bedroombg with hpunch:
        linear 0.2 zoom 1.05 yalign 0.8

    "Augh!"

    "My hands manage to grip the mattress before I can fall."

    "They say that your muscles begin to atrophy If you lie down for too long."

    "I wonder if that's begun to happen to me."

    show bg bedroombg:
        linear 0.2 zoom 1.1 yalign 0.1

    "Catching my breath, I attempt to stand again."

    "My legs are shaky, but I keep my balance."

    "Okay. One step at a time now."

    "Carefully..."

    show bg ceiling ceiling empty
    show ceilingfan
    with dissolve

    "I stumble my way to the other side of my apartment, and get myself a cup of water."

    "With glass in hand, I carefully make my way back to the bed."

    hide ceilingfan
    show bg bedroombg
    with dissolve

    "My throat welcomes the cool liquid."

    "When was the last time I drank anything?"

    "Time no longer means anything to me."

    "I just drift in and out of consciousness."

    "Once, I had a great sleep schedule."

    "I'd be asleep before 12, and wake up at 8."

    "Then I met you, and I stayed up later and later, until I was going to bed at 3 in the morning."

    "I blame your personality. You were so confident, so full of energy."

    "But well, I'm nothing like that."

    show bg ceiling ceiling empty
    show ceilingfan
    with dissolve

    "I wrap myself in my blanket again."

    "Falling asleep feels as hopeless as it's always been."

    "Maybe I should turn off the lights?"

    "I should, but with the lights on I-"

    hide ceilingfan
    show bg bedroombg
    with dissolve

    "I stare at the VR equipment sitting on my nightstand."

    "When I look at the headset, all I can think of is you, and the times we spent together."

    "It hurts. It really hurts."

    "But why…"

    "Why am I…?"

    "I know I shouldn't."

    "I know this will probably cause me even more pain."

    "But…"

    "One more time. Just one more time."

    "That's all I need."

    play sound [ "<silence .5>", "sfx/VR_Button.ogg" ]

    call screen in_game_entervr
    stop ambient fadeout 1.0
    stop music fadeout 1.0

    jump hub1


    #Enter VR
