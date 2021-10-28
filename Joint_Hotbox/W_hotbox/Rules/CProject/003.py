#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Set Current Ref Frame
# COLOR: #998d6c
# TEXTCOLOR: #ffffff
#
#----------------------------------------------------------------------------------------------------------

ns = nuke.selectedNodes()
for n in ns:
    n.knob('python_button').execute()
