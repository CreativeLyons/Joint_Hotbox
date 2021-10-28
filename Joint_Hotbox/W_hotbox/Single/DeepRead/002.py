#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Set to Latest Version
#
#----------------------------------------------------------------------------------------------------------

for node in nuke.selectedNodes():
    if node.knob("version_setlatest"):
        node.knob("version_setlatest").execute()
