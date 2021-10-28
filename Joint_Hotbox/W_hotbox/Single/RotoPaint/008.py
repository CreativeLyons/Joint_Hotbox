#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Red Brush
# COLOR: #a82828
# TEXTCOLOR: #ffffff
#
#----------------------------------------------------------------------------------------------------------

for node in nuke.selectedNodes():
    node.knob("toolbar_paint_color").setValue(1, 0)
    node.knob("toolbar_paint_color").setValue(0, 1)
    node.knob("toolbar_paint_color").setValue(0, 2)
    node.knob("toolbar_paint_color").setValue(1, 3)
