#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: stencil
# COLOR: #604d4d
#
#----------------------------------------------------------------------------------------------------------

for node in nuke.selectedNodes():
    node.knob("operation").setValue("stencil")
    node.knob("bbox").setValue("B")
