#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Align Vertically |
# COLOR: #37595b
# TEXTCOLOR: #ffffff
#
#----------------------------------------------------------------------------------------------------------

from mps2 import MassivePanelPySide

nodes = nuke.selectedNodes()
mp = MassivePanelPySide()
mp.alignNodes(nodes, direction="x")