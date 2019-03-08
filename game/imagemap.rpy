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

        hotspot (1479, 493, 359, 223) at glowpulse:
            action Jump("eighttrack")
        hotspot (725, 472, 652, 480) at glowpulse:
            action Jump("plushie")
        hotspot (259, 671, 249, 239) at glowpulse:
            action Jump("mug")

label eighttrack:

    "Never Gonna Give You Up."

    return

label plushie:

    "Nya."

    return

label mug:

    "Awoo."

    return
