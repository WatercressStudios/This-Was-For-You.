#
# Real World 4
#

label rw4:

    # MC did not receive a notification of "New voicemail!" for this voicemail (just vary up how they leave VR a little)

    show vrpoweroutageeffect

    # play SFX of a VR headset being powered down (it'll be cool if we can have a TV blinking off visual effect to go with it)
    # also hide the menu buttons (temporarily, for a few seconds)

    play sound "sfx/VR-OFF.ogg"

    hide screen in_game_menu

    pause 0.5

    scene bg bedroombg rain darker dim opendark dark
    show black
    hide vrpoweroutageeffect
    hide black with dissolve

    play ambient "sfx/Ambience_1_(Rain).ogg" fadein 2.0

    if persistent.subtitle or config.sound == False:
        sfx "sfx/thunder_2.ogg" "*Thunder*"
    else:
        sfx "sfx/thunder_2.ogg"

    "What? What happened?"

    play music "music/RW_S4.ogg" fadein 3.0

    # sfx of a thunder, followed by a BG change to the window and sfx of MC sitting up on bed. it's also super dark out there.

    show bg bedroombg lightning
    show bedroomstorm darkblue darkflash darklightning

    if persistent.subtitle or config.sound == False:
        sfx "sfx/Thunder_1.ogg" "*Thunder*"
    else:
        sfx "sfx/Thunder_1.ogg"

    # flash the lightning outside the window! a second of two later, play sfx of another thunder.

    if persistent.subtitle or config.sound == False:
        sfx [ "<silence 3>", "sfx/thunder_2.ogg" ] "*Thunder*"
    else:
        sfx [ "<silence 3>", "sfx/thunder_2.ogg" ]

    pause 1

    # sfx of the VR headset powering on, and the room goes to normal brightness again

    if persistent.subtitle or config.sound == False:
        sfx "sfx/VR-On.ogg" "*Restored Power*"
    else:
        sfx "sfx/VR-On.ogg"

    hide bedroomstorm
    show screen in_game_menu
    show bg bedroombg normal lit open bright -lightning
    with dissolve



    "...a blackout?"

    "Haven't had that in awhile."

    # ding! new voicemail

    "At least the power's back on. Or are we on a generator right now? I don't actually know if we even have one. Not that it matters."

    # sfx for "access denied" or "cannot access this UI function at this time"
    "..."

    "I'm trying to go back into the VR world, but the button's greyed out."

    "It says \"Initializing…\" on the display."

    "Of course… it just had a hard reset from the blackout, so the headset needs time to boot up."

    "Dammit."

    "Joke's on me, huh."

    "...guess I should listen to this voicemail after all."

    $ relogin = True
    call screen thumbprint_active with Dissolve(0.5)

label rw4_continue:
    # show the thumbprint scanner from the start of the game again, and animate it in the same way, to re-authenticate

    $ save_name = "Friendships"
    scene black
    show screen chapter_announce

    #voice "voice/13-rw4_continue-1.ogg" #Friend (1_ Kenneth Faircloth 2_ Siddharta Villanueva)
    vm "Heya! So uh, where do I start…"
    #voice "voice/13-rw4_continue-2.ogg" #Friend (1_ Kenneth Faircloth 2_ Siddharta Villanueva)
    vm "Right! I don't wanna call you out or anything, but you kinda missed our last four hangouts."
    #voice "voice/13-rw4_continue-3.ogg" #Friend (1_ Kenneth Faircloth 2_ Siddharta Villanueva)
    vm "Wait that counts as calling you out, isn't it? Sorry. *laughs*"
    #voice "voice/13-rw4_continue-4.ogg" #Friend (1_ Kenneth Faircloth 2_ Siddharta Villanueva)
    vm "So umm… your friends wanna see your stupid face."
    #voice "voice/13-rw4_continue-5.ogg" #Friend (1_ Kenneth Faircloth 2_ Siddharta Villanueva)
    vm "I'm sure you'll forgive us for tomorrow, cuz you're a good person."
    #voice "voice/13-rw4_continue-6.ogg" #Friend (1_ Kenneth Faircloth 2_ Siddharta Villanueva)
    vm "Also, you owe us one."
    #voice "voice/13-rw4_continue-7.ogg" #Friend (1_ Kenneth Faircloth 2_ Siddharta Villanueva)
    vm "Oh right, I forgot to mention… we're coming over tomorrow."
    #voice "voice/13-rw4_continue-8.ogg" #Friend (1_ Kenneth Faircloth 2_ Siddharta Villanueva)
    vm "Just the three of us, don't worry. Take care!"
    # abruptly hangs up, as if the caller was afraid the MC would say "no" even though it's a freaking voicemail

    pause 0.5

    $ visible_emails.append('spam3')
    $ visible_emails.append('boss2')
    $ visible_emails.append('funeral2')
    show screen notify("You have unread emails.")

    play ambient "sfx/Ambience_2_Window_Open.ogg" fadein 1.0 fadeout 1.0

    scene bg bedroombg nocurtains rain:
        zoom 1.5
        xalign 0.9 yalign 0.2
    with dissolve

    pause 0.5

    show bg bedroombg lightning
    show bedroomstorm nocurtains:
        zoom 1.5
        xalign 0.9 yalign 0.2

    pause 1

    hide bedroomstorm

    # fade back into the window scene, zoomed into the outside view. a lightning flashed and thundered again

    if persistent.subtitle or config.sound == False:
        sfx "sfx/Thunder_1.ogg" "*Thunder*"
    else:
        sfx "sfx/Thunder_1.ogg"

    "...so it's come to this, huh."

    "My friends are no longer giving me a choice."

    "If I knew this was going to happen, I'd have replied to their emails."

    "...maybe."

    show bg bedroombg lightning
    show bedroomstorm nocurtains:
        zoom 1.5
        xalign 0.9 yalign 0.2

    pause 1

    hide bedroomstorm

    # lightning flash and sfx again
    # pause a second or two

    if persistent.subtitle or config.sound == False:
        sfx "sfx/thunder_2.ogg" "*Thunder*"
    else:
        sfx "sfx/thunder_2.ogg"

    "Was it a mistake to tell them about Ji-min?"

    "They never understood my friendship with her."

    "And ever since I told them what happened, they've been treating me as if I've lost a lover."

    "\"Ji's my best friend,\" I've said countless of times."

    "They mean well, and to their credit, I think they do try. They just never had a close online friend themselves, so they can't relate."

    "And when they come tomorrow, I'll have to say it again."

    "...No."

    "This time, I'll have to say…she {b}was{/b}…my best friend."

    "..."

    # sfx of beeping sound indicating VR is ready to be launched

    if persistent.subtitle or config.sound == False:
        sfx "sfx/Chime - DX EP.ogg" "*Initialization Complete*"
    else:
        sfx "sfx/Chime - DX EP.ogg"

    "Shaking my head, I look at the display. The VR app has finished initializing."

    "I start to head back, but--"

    show bg bedroombg:
        linear 0.2 yalign 0.8

    pause 0.1

    show black with vpunch:
        alpha 0
        linear 0.1 alpha 1

    show bg bedroombg with vpunch

    # sfx of someone tripping over something and falling flat, like a pizza box or something
    # slide the BG up into a black screen to indicate a fall
    # fade in the room again, window view

    play ambient "sfx/Ambience_1_(Rain).ogg" fadeout 3.0

    if persistent.subtitle or config.sound == False:
        sfx "sfx/box_fall.ogg" "*Trip And Fall*"
    else:
        sfx "sfx/box_fall.ogg"

    pause 0.1

    scene black

    "I rub my elbow, trying to soothe the part of it that had an unfortunate meeting with the ground."

    "What did I trip over?"

    "...a pizza box?"

    show bg bedroombg open rain
    call openeyes from _call_openeyes_1

    "I look around my apartment and, for the first time, notice the state it’s in."

    "It's a filthy mess."

    "...my friends aren't going to react well to this, are they?"

    "I don't even have any food or drinks to offer them - the leftover pizza and coffee sachets ran out days ago."

    "And the light bulb at the front door still needs changing."

    "..."

    "Yeah, my friends will definitely throw a fit."

    "Maybe I should clean up a bit first?"

    # sfx new email! This time it's from work, with subject line "URGENT reply immediately"
    # player has option to read or ignore the email. the basic gist of it is that the MC has missed too many days of work, and the boss will have no choice but reluctantly hire someone new if this goes on.

    show bg bedroombg lightning
    show bedroomstorm

    if persistent.subtitle or config.sound == False:
        sfx "sfx/Thunder_3.ogg" "*Thunder*"
    else:
        sfx "sfx/Thunder_3.ogg"

    # lightning flash and sfx again
    # pause a second or two

    "..."

    show bg bedroombg closed with dissolve

    "I can do it tomorrow."

    "Just… one more time."

    # MC goes back to bed and opens VR scene. Have MC walk around in VR silently a few times first, revisiting all the BGs, before going into Julia's scene.

    play sound [ "<silence .5>", "sfx/VR_Button.ogg" ]
    stop ambient fadeout 1.0
    call screen in_game_entervr

    stop music fadeout 3.0

    jump planeticket
