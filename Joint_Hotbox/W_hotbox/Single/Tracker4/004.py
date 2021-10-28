#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: All On TRS
#
#----------------------------------------------------------------------------------------------------------

for i in nuke.selectedNodes():
    tracks = 0
    while i.knob('tracks').isAnimated(31 * tracks + 2):
        tracks += 1

    for track in range(tracks):
        i.knob('tracks').setValue(1, 31 * track + 6)
        i.knob('tracks').setValue(1, 31 * track + 7)
        i.knob('tracks').setValue(1, 31 * track + 8)
