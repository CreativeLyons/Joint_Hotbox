#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: all
# COLOR: #6b5252
# TEXTCOLOR: #ffffff
#
#----------------------------------------------------------------------------------------------------------

for node in nuke.selectedNodes():
    node.knob("channels").setValue("all")
