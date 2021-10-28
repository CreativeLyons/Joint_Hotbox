#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Swap
#
#----------------------------------------------------------------------------------------------------------

s = int(nuke.selectedNode().knob("operation").getValue())
nuke.selectedNode().knob("operation").setValue(abs(s-1))
