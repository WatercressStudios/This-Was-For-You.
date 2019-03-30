#
# Plushie
#

label plushie:
    $ save_name = "Apologies"
    scene bg hub hub
    show screen chapter_announce
    show catfieldbg
    show items catplushie

    "I made this for you."

    "Ever since you turned my Uninstall Button into what it is now, I felt like I needed to repay you somehow."

    "I wasn't sure of what to give you for the longest time."

    "When you're able to create basically anything you want, the possibilities are endless."

    "After a while I kind of forgot about it."

    "It became one of those things I remembered from time to time, but neglected to actually follow through with."

    "And then I hurt you."

    "It was about four months into our friendship."

    "By then, I thought I had you all figured out."

    "How painfully ignorant of me."

    "I'm not sure how you put up with me back then."

    "After all, I teased you for your love for cute things so frequently."

    "I thought I was being playful."

    "But I underestimated how easy it is to fake a smile in virtual reality."

    "How the little things can stack up until they're unbearable."

    "And then well, I crossed a line."

    "..."

    "I didn't log into VR for a week."

    "I knew I couldn't hide forever but, I also knew I had to do a bit of introspection."

    "Because well, I messed up."

    "The Ji-min I thought I knew was just a pile of assumptions I made based on certain stereotypes."

    "I wanted to be better than that."

    "For the first time I was glad of how different our time zones were."

    "It meant I could make this without you finding out about it."

    "I spent hours just trying to get the proportions right."

    "But it was all worth it."

    "I chose to make this plushie because I remembered how you said you wanted a cat."

    "Unfortunately, your allergy meant that was impossible."

    "This was the only way I could help make your dream come true."

    "I just wish I had been able to make it as a gift, rather than as an apology."

    "You know, I learned a very important lesson in that first fight of ours."

    "It was naive of me to expect us to always get along without a hitch."

    "And sometimes things need to get worse, in order to get better."

    "..."

    "I wish that were the case now."

    hide catfieldbg with dissolve

    voice "07-plushie-1.ogg" #Cheshire (shiena)
    che "Ooh. What's this?"

    show che s at centerleft, height:
        xzoom -1
    show items catplushie:
        linear 0.2 xpos 0.7
    with easeinleft

    "Here we go again."

    mc "It's a-"

    show che s catmouthclosed armsnyan

    voice "07-plushie-2.ogg" #Cheshire (shiena)
    che "It's like me, nya!"

    mc "Don't be silly. It's a plushie, not a bot like you."

    show che s default base

    voice "07-plushie-3.ogg" #Cheshire (shiena)
    che "But it's got a tail!"

    show che s catmouth

    voice "07-plushie-4.ogg" #Cheshire (shiena)
    che "And we have the same mouth!"

    "God, why did this tutorial bot have to be a catgirl of all things?"

    mc "You're both cat-like, but that's where the similarities end."

    show che f sad:
        xzoom 1
        linear 0.2 xpos 0.3

    voice "07-plushie-5.ogg" #Cheshire (shiena)
    che "Meowster's so mwean!"

    mc "Yeah, yeah."

    show che f happy

    voice "07-plushie-6.ogg" #Cheshire (shiena)
    che "But maybe master secretly cares about me!"

    mc "What gives you that impression!?"

    voice "07-plushie-7.ogg" #Cheshire (shiena)
    che "The plushie of course!"

    show che f armsscanning

    voice "07-plushie-8.ogg" #Cheshire (shiena)
    che "If you have something like that, you must like cats."

    show che s armsnyan:
        xzoom -1
        linear 0.2 xpos 0.35

    voice "07-plushie-9.ogg" #Cheshire (shiena)
    che "And I'm a cat!"

    mc "That's not how it works!"

    mc "And this isn't mine!"

    show che s meh

    mc "It's… ah forget about it."

    show che s base

    voice "07-plushie-10.ogg" #Cheshire (shiena)
    che "Master, I wants to know!"

    show catfieldbg with dissolve:
        alpha 0.8

    "\"Master\"… you know, that kind of reminds me of the time you asked me if I've ever been to a cat cafe."

    "I just, looked at you with a horrified expression and told you I'd never go to somewhere like that."

    show che s pout1

    "Turns out I had gotten cat cafes and maid cafes all mixed up."

    "You teased me about it for ages."

    hide che with easeoutright

    "Going to a cat cafe was on your bucket list."

    "Naturally, I was surprised to hear that."

    "\"Aren't you allergic to cats?\" I remember asking."

    "You laughed and said that a cat cafe would be worth it."

    "But nothing is worth your life."

    #MC logs out of VR

    if visited < 3:
        call screen in_game_exitvr

    jump itemmerge
