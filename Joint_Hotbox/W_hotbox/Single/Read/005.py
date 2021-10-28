#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Open NukeScript
# COLOR: #396b89
# TEXTCOLOR: #ffffff
#
#----------------------------------------------------------------------------------------------------------

for node in nuke.selectedNodes():
    if node.knob("open_nk"):
        node.knob("open_nk").execute()
        nuke.message('opening nuke script')
