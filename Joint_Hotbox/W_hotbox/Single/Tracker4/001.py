#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: STBL baked
# COLOR: #6f458e
# TEXTCOLOR: #ffffff
#
#----------------------------------------------------------------------------------------------------------

n = nuke.selectedNode()
n.knob('cornerPinOptions').setValue(6)

n.knob('createCornerPin').execute()
