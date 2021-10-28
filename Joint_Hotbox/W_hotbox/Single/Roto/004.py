#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Breakout Layers
#
#----------------------------------------------------------------------------------------------------------

import _curveknob
import nuke.rotopaint as rp

print(dir(rp.Layer))


rpNode = nuke.selectedNode()
nuke.nodeCopy("%clipboard%")
SelectedLayerToExtract = [Layer for Layer in rpNode['curves'].getSelected()]
rpNodeCopy = nuke.nodePaste("%clipcoard%")


newLayersList=[]
for EachLayer in SelectedLayerToExtract:
    rootLayerSecondLevel = rpNode["curves"].rootLayer[0]

    layer_name="%s/%s" % (rootLayerSecondLevel.name,EachLayer.name)
    newLayersList.append(rpNodeCopy['curves'].toElement(layer_name))


for layer in newLayersList:
    newNode=nuke.createNode("Roto")
    rootLayer = newNode['curves'].rootLayer.append(layer)

    nodeName = "%s_%s" % (rpNode["name"].getValue(),layer.name)
    newNode["name"].setValue(nodeName)

nuke.delete(rpNodeCopy)
