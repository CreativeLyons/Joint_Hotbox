#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Freeze Input
# COLOR: #895d59
# TEXTCOLOR: #ffffff
#
#----------------------------------------------------------------------------------------------------------

ns = nuke.selectedNodes()
for n in ns:
    knob = n.knob('FreezeInput')
    currentState = knob.getValue()
    newState = abs(currentState-1)
    knob.setValue(newState)
