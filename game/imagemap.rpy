default visited8track = False
default visitedplushie = False
default visitedmug = False

transform glowpulse:
    on idle:
        linear 2.0 alpha 0.2
        linear 2.0 alpha 1
        repeat

    on hover:
        alpha 1

screen hubselect:
    tag hubselect
    imagemap:
        ground "hub"
        idle "hubmap_hover"
        hover "hubmap_hover"

        if not visited8track:
            hotspot (1479, 493, 359, 223) at glowpulse:
                action Jump("eighttrack_internal")

        if not visitedplushie:
            hotspot (725, 472, 652, 480) at glowpulse:
                action Jump("plushie_internal")

        if not visitedmug:
            hotspot (259, 671, 249, 239) at glowpulse:
                action Jump("mug_internal")

label eighttrack_internal:
    $ visited8track = True
    $ visited += 1
    jump eighttrack

label plushie_internal:
    $ visitedplushie = True
    $ visited += 1
    jump plushie

label mug_internal:
    $ visitedmug = True
    $ visited += 1
    jump mug

label itemmerge:
    if visited == 1:
        jump rw2
    elif visited == 2:
        jump rw3
    else:
        jump rw4
