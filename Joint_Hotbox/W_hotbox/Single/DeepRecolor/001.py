#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: All
#
#----------------------------------------------------------------------------------------------------------

for node in nuke.selectedNodes():
    node.knob("channels").setValue("all")
