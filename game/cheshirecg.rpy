image eyes_sad = blinkeyes("cgs/cheshire/eyes_sad.png", "cgs/cheshire/eyes_closedsad.png")

layeredimage cheshire:
    always:
        "cgs/cheshire/hubblur.png"

    group body:
        attribute armsforward default:
            "cgs/cheshire/armsforward.png"

    group eyes:
        attribute closed default:
            "cgs/cheshire/eyes_closed.png"

        attribute closedsad:
            "cgs/cheshire/eyes_closedsad.png"

        attribute sad:
            "eyes_sad"

    group tears:
        attribute tears:
            "cgs/cheshire/tears.png"

    group mouth:
        attribute cheerful default:
            "cgs/cheshire/mouth_cheerful.png"

        attribute hurt:
            "cgs/cheshire/mouth_hurt.png"

    group brows:
        attribute happy default:
            "cgs/cheshire/brows_happy.png"

        attribute shocked:
            "cgs/cheshire/brows_shocked.png"

    always:
        "cgs/cheshire/glasses.png"

    group item:
        attribute button default:
            "cgs/cheshire/button.png"

        attribute ticket:
            "cgs/cheshire/ticket.png"
