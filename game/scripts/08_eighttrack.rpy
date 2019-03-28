#
# Eighttrack
#

label eighttrack:
    $ save_name = "Our Song"
    scene bg hub hub
    show woodtrail1 with dissolve
    show items 8track
    #MC selects the eight track

    # fade the bg music out
    "..."

    hide items 8track with dissolve

    # sound of cassette tape being inserted in cassette player
    "I slide the cassette into the player and push it close with a satisfying 'click'."

    "However, I hesitate over the 'play' button."

    "What's the point of listening to this? We never got around to finishing this."

    "Now we never will."

    "..."

    # sfx of cassette player's play button being pushed, and the sfx of spinning cassette
    "I push the 'play' button anyway."

    # song of that Ji-min composed plays, but it's missing the vocal tracks
    # after about 10 seconds of listening to the song
    # if subtitle is on, show: "(music with no vocals playing)"

    "You composed this song after your sister moved away from home, and you missed her."

    "We must had known each other for a month when you came out to me as a singer-songwriter-to-be."

    "I asked who your inspiration was, and you gave me basically a thesis on IU, your favorite South Korean singer-songwriter."

    "I think I spent that entire night just listening to you gush about her talent and inspiring origin story."

    "And then the next night you made me listen to all her songs and watch some of her shows, because of course she was an actress as well."

    "I enjoyed them more than I let on."

    "You had a beautiful singing voice, too."

    "Yet you kept practicing, in between job shifts and college classes."

    "Given how hard you worked, I was so sure it was only a matter of time before I'd hear your singing voice on the radio."

    "But life had its own ideas."

    "..."

    "This song was supposed to be ours. You might have composed it because your sister moved away, but it was about how you felt at that time."

    "That it didn't matter that your best friends are worlds apart."

    "..."

    "You were wrong. It does matter."

    "I need you here."

    show che s catmouthclosed armshappy at center, height behind woodtrail1:
        xpos 0.5
        linear 0.6 xpos 0.45
        linear 0.6 xpos 0.4
        linear 0.6 xpos 0.45
        linear 0.6 xpos 0.5
        linear 0.6 xpos 0.55
        linear 0.6 xpos 0.6
        linear 0.6 xpos 0.55
        linear 0.6 xpos 0.5
        repeat
    hide woodtrail1 with dissolve

    # ches is singing to the song…. ish. It's not actually in tune or even follows the beat or the song.
    voice "08-eighttrack-1.mp3" #Cheshire (shiena)
    che "Nya~ nya~ nya~! Nya~ nya~ nya~!"

    mc "...what are you doing?"

    show che s catmouth base:
        linear 0.2 xpos 0.5

    # ches fades in as opposed to sliding in as usual
    voice "08-eighttrack-2.mp3" #Cheshire (shiena)
    che "CH3SH1R3 was singing!"

    mc "No, you really weren't."

    show che s catmouthclosed armshappy

    voice "08-eighttrack-3.mp3" #Cheshire (shiena)
    che "Why don't Meowster joins me? Nya~ nya~ nya~!"

    show che s catmouthclosed armshappy:
        zoom 1.05

    show bg hub hub with hpunch:
        zoom 1.05

    show che s sad

    mc "Shut up!"

    show bg hub hub:
        linear 0.2 zoom 1

    show che s sad:
        linear 0.2 zoom 1

    mc "The song's not yours to sing..."

    show che s meh base

    # confused look
    voice "08-eighttrack-4.mp3" #Cheshire (shiena)
    che "Then whose is it?"

    show woodtrail1 with dissolve:
        alpha 0.8

    "It was supposed to be Ji-min's and my duet."

    "I didn't want to do it, but she insisted, and she made me promise that I'd practice it so we can record it together."

    "I still don't know what possessed me to agree to that ridiculous promise."

    "But I did."

    "And now I can never fulfill that promise…"

    # back to VR world

    jump itemmerge
