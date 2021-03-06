#
# Mug
#

label mug:
    $ save_name = "You Were so Strong."
    scene bg hub hub
    show screen chapter_announce
    show kerosene with dissolve
    show items awoomug with dissolve
    #This scene won't totally be emotionally charged cause Instant drew the original mug no

    play ambient "sfx/fire.ogg" fadein 2.0
    play music "Music/Awoo_Mug.ogg" fadein 2.0

    "Grabbing the mug, I'm brought back to the night we first gathered around the fire."

    "I remember thinking, isn't this dumb? It's a virtual fire. It's fake."

    "I used to say, isn't fire hard on system resources? It was so lifelike, it must've taken ages to design, right?"

    "...I remember when we first video called."

    "You sat next to your real fireplace, drinking from this very real mug. Homemade cocoa, your own special blend."

    "You talked about how you'd eventually make it for me."

    "\"You will absolutely loooove this recipe! I know the foofy fancy drinks you have at the cafe, this is right down your alley!\""

    "I had a mug of my own as well, of course."

    "The first one wasn't anything special, but once you bought me a matching pair, it felt like our connection was so much more real."

    "I felt justified. It didn't matter if you were a friend over the internet, you were still a friend."

    "It doesn't matter what anyone said."

    "You were my best friend."
    stop ambient
    play ambient "sfx/Hub_Beach.ogg" fadein 2.0 fadeout 2.0
    hide kerosene with dissolve

    voice "voice/06-mug-1.ogg" #Cheshire (shiena)
    che "Meowster! Wots dat?"

    show che s at centerright, height
    show items awoomug:
        linear 0.2 xpos 0.3
    with easeinright

    "My grip tightens on the mug, and I let out a breathy sigh."

    mc "It's a memento."

    voice "voice/06-mug-2.ogg" #Cheshire (shiena)
    che "Meowster, you should get your eyes checked. It's a mugs, nyat a mementos. Silly Meowster!"

    voice "voice/06-mug-3.ogg" #Cheshire (shiena)
    che "Oooh! There's writing! What's it say??"

    show che s:
        linear 0.2 zoom 1.2 ypos 1.2 xpos 0.7

    "Cheshire leans into me, looking at the words on the mug."

    voice "voice/06-mug-4.ogg" #Cheshire (shiena)
    che "Oh! Cheshire loves this!"

    show che s awoo armshappy

    voice "voice/06-mug-5.ogg" #Cheshire (shiena)
    che "Awoooooooooo!"

    show che s default base

    voice "voice/06-mug-6.ogg" #Cheshire (shiena)
    che "Can I haves? Can I haves?"

    show che s sad

    mc "No. This isn't yours, and it won't ever be yours. Go away. Please."

    voice "voice/06-mug-7.ogg" #Cheshire (shiena)
    che "Oh, okay…"

    hide che
    show items awoomug:
        linear 0.2 xpos 0.5
    with easeoutright

    "With a hurt look on its face, it sinks away, leaving me alone."

    "Putting my hand to my chest, I feel my heartbeat, willing it to slow."

    "I'm agitated. Mom would say that I woke up on the wrong side of the bed."

    "I think she understands, though."

    "She would have, too."

    hide items with dissolve
    show bg hub hub with hpunch:
        zoom 1.02 ypos 1.0

    "Collapsing to the ground, I hug the mug close to my chest."

    "Was I ever that mean to you, Ji?"

    "Did I treat you right? Was I a good influence on you, like you were for me?"

    "I should've been better. I could have been better."

    "I know this."

    stop ambient fadeout 2.0
    play ambient "sfx/fire.ogg" fadein 2.0

    show kerosene with dissolve:
        alpha 0.7

    "All of those late night chats."

    "I would watch the sunrise, still talking to you, joking about how I'd be dead tired at work."

    "It was all worth it for you. You helped me so much more than I ever helped you, and that was unfair of me."

    "Relationships should always be equal right? You were my friend and yet you always made the effort."

    "To the very end."

    "It was that way from the beginning, wasn't it?"

    "You were the one who approached me, and helped me out. You were the one that showed me how great of a world this could be."

    "How things don't have to be real to be {b}real{/b}."

    "You taught me that I don't have to make excuses for what I love, and that it doesn't matter what anyone else says."

    "You taught me to ignore those who wish to tear me down."

    "You taught me positivity. Optimism. Happiness."

    "What did I teach you?"

    "...I guess I did teach you some things."

    "I taught you why I held those feelings. I helped ground you, while you helped lift me up."

    "I talked about how things were different over here, and I taught you how the real world had grown me into who I was."

    "Was I doing the right thing?"

    "Cynicism and idealism gave way to optimistic nihilism. Was I right to do that?"

    "Or was I destroying one of the last truly innocent, truly good things in the world?"

    "It doesn't matter anymore. I just wish I would have told you the truth."

    "There were so many opportunities to tell you how good of a friend you were."

    "I never thanked you for helping me back then, did I?"

    "The kind words you gave me… I will never forget them. Ever."

    "You were always there for me, and I should have appreciated that more."

    "I should have told you how much you meant - how much you mean to me."

    "I'll never be able to do that now. All I have are a life full of regrets and this damned mug."

    "I wonder where yours is?"

    "Did they pack it all away after you died?"

    "Is it sitting unused on some dusty shelf? Maybe your parents are keeping it safe. Maybe they're using it."

    "I can't tell if I hate the thought of that or not."

    "Should things be repurposed, or should we freeze these memories in time?"

    "Is it better if it lives on through someone else?"

    "Or should it have died with you?"

    play sound [ "<silence .5>", "sfx/VR_Button.ogg" ]



    if visited < 3:
        call screen in_game_exitvr
        stop ambient fadeout 1.0
        stop music fadeout 1.0
    jump itemmerge
