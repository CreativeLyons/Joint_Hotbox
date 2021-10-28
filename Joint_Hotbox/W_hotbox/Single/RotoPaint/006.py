#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Green Brush
# COLOR: #27a837
# TEXTCOLOR: #ffffff
#
#----------------------------------------------------------------------------------------------------------

for node in nuke.selectedNodes():
    node.knob("toolbar_paint_color").setValue(0, 0)
    node.knob("toolbar_paint_color").setValue(1, 1)
    node.knob("toolbar_paint_color").setValue(0, 2)
    node.knob("toolbar_paint_color").setValue(1, 3)
