#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: outputMask to mask.a
# COLOR: #6b5284
# TEXTCOLOR: #ffffff
#
#----------------------------------------------------------------------------------------------------------

for node in nuke.selectedNodes():
    node.knob("outputMask").setValue("mask.a")
