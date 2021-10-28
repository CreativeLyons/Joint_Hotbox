#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: average
# COLOR: #69808e
#
#----------------------------------------------------------------------------------------------------------

for node in nuke.selectedNodes():
    node.knob("operation").setValue("average")
