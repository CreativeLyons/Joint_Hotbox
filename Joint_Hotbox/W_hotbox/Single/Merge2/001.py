#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: mask
# COLOR: #604d4d
#
#----------------------------------------------------------------------------------------------------------

for node in nuke.selectedNodes():
    node.knob("operation").setValue("mask")
    node.knob("bbox").setValue("A")
