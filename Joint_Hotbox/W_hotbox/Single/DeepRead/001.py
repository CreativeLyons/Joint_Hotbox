#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Check Version
#
#----------------------------------------------------------------------------------------------------------

for node in nuke.selectedNodes():
    if node.knob("version_update"):
        node.knob("version_update").execute()
