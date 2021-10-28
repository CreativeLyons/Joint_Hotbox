#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: RGB
#
#----------------------------------------------------------------------------------------------------------

for node in nuke.selectedNodes():
    node.knob("channels").setValue("rgb")
