#
# Ending
#

label ending:
    $ save_name = "I Miss You."
    scene black

    pause 1
    show screen chapter_announce

    play ambient "sfx/Ambience_1_(Rain).ogg" fadein 3.0 fadeout 3.0
    play music "music/RW_S5.ogg" fadein 3.0 fadeout 5.0

    scene bg ceiling ceiling empty
    show ceilingfan
    with dissolve

    "I've been through all of this before."

    "Over and over and over, I think the same stupid things."

    "My mind's a skipping record, refusing to move forward."

    "I'm just ruminating. I'm just hurting myself."

    "It's not like I'm reaching any new conclusions, visiting the world we made. Nothing new is happening when I think of you."

    "The world stands still."

    "...No, that's not right. I'm the one sitting still, with the world speeding past me."

    "I'm being left behind."

    "It's been a month since you died, and I don't feel any better. I'm supposed to move on eventually, right?"

    "I'm supposed to get used to it, expect some sort of numbness to the pain, but not this kind."

    "I'm not numb. I'm empty."

    "I just want to forget. Dear God do I want to forget."

    "But how can I?"

    "Maybe it's the VR world holding me back."

    "Or…"

    "Maybe it's her voice."

    "Someone, please tell me…"

    stop ambient fadeout 1.0

    menu:
        "How do I let go?"

        "Delete Ji-min's voicemail":
            $ jivoicemail = True

        "Keep Ji-min's voicemail":
            $ jivoicemail = False

    stop music fadeout 5.0

    #roll credits
    #end game
