#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: MM baked
# COLOR: #6853a3
# TEXTCOLOR: #ffffff
#
#----------------------------------------------------------------------------------------------------------

n = nuke.selectedNode()
n.knob('cornerPinOptions').setValue(7)

n.knob('createCornerPin').execute()
