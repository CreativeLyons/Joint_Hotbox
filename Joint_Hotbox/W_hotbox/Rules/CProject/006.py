#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Toggle MotionBlur
# COLOR: #686868
# TEXTCOLOR: #ffffff
#
#----------------------------------------------------------------------------------------------------------

ns = nuke.selectedNodes()
for n in ns:
    knob = n.knob('motionblur')
    currentState = knob.getValue()
    newState = abs(currentState-1)
    knob.setValue(newState)
