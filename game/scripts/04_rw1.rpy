#
# Real World 1
#

label rw1:
    $ save_name = "The World Keeps Turning"
    scene black

    #Voicemail
    voice "04-rw1-1.mp3" #Boss ()
    bos "Hey, it's your boss. How’ve you been lately?"
    voice "04-rw1-2.mp3" #Boss ()
    bos "We haven't seen you at the shop for a while."
    voice "04-rw1-3.mp3" #Boss ()
    bos "Don't worry, we've managed to cover your shifts just fine, but... it would be nice to know when you'll be coming back."
    voice "04-rw1-4.mp3" #Boss ()
    bos "Give me a call when you can, alright?"
    voice "04-rw1-5.mp3" #Boss ()
    bos "See you soon."

    pause 0.5

    scene bg ceiling ceiling empty
    show ceilingfanstatic:
        rotate 17
        xalign 0.5 yalign 0.5
    with dissolve

    "How long has it been since I’ve been to work?"

    "I don’t know. Honestly, I lost track."

    "I wonder if I should go back."

    "It's not exactly anything special after all. it's just some shitty retail job that didn't care about credentials or work experience."

    "I spend half my time standing behind the cash register, and the rest of it stocking shelves."

    "I'm honestly surprised that I haven’t been replaced by a robot yet."

    "{b}Sigh.{/b}"

    "I stare up at the fan."

    "When did I turn that off?"

    "It's probably for the best. I don't want to know how high my electricity bill is."

    "Ugh."

    "Sure my job's tedious, but I need to get money somehow."

    "And I know that if I don't go back soon, I won't have one anymore."

    call closeeyes
    scene black with dissolve

    "I know I should care, but..."

    "You're gone, but the world keeps turning."

    "I can't even muster up the energy to get angry at everyone for carrying on with their lives."

    "At the same time, my eyes have stayed dry."

    "To think I can't even shed a tear for you."

    "What kind of a friend am I?"

    #Thunder sfx
    #Rain sfx

    scene bg bedroombg open rain
    call openeyes

    "Heh. Even the sky is crying more than me."

    show bg bedroombg:
        zoom 1.5
        xalign 0.9 yalign 0.2

    "You liked the rain."

    show bg bedroombg nocurtains with dissolve

    "You always found it relaxing."

    "You liked the way it sounds, and the way it feels on your skin."

    "And… the way it washes everything away."

    "But what if I don't want that?"

    "It's just another way everyone else is moving on."

    show bg bedroombg closed with dissolve

    "Ugh. I'm done with rain."

    show bg ceiling ceiling empty
    show ceilingfanstatic:
        rotate 17
        xalign 0.5 yalign 0.5
    with dissolve

    "I don't want to be here anymore, not when the world is so determined to forget her."

    "No. I'm going back home."

    #Enter VR
    jump hub2
