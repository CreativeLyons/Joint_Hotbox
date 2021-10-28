#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Check Version
# COLOR: #756b3f
# TEXTCOLOR: #ffffff
#
#----------------------------------------------------------------------------------------------------------

for node in nuke.selectedNodes():
    if node.knob("version_update"):
        node.knob("version_update").execute()
