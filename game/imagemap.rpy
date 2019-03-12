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
                action Jump("eighttrack")

        if not visitedplushie:
            hotspot (725, 472, 652, 480) at glowpulse:
                action Jump("plushie")

        if not visitedmug:
            hotspot (259, 671, 249, 239) at glowpulse:
                action Jump("mug")

label eighttrack:

    "Never Gonna Give You Up."
    $ visited8track = True

    jump itemmerge

label plushie:

    "Nya."
    $ visitedplushie = True

    jump itemmerge

label mug:

    "Awoo."
    $ visitedmug = True

    jump itemmerge

label itemmerge:

    if visited8track and visitedplushie and visitedmug:
        return
    else:
        call screen hubselect
