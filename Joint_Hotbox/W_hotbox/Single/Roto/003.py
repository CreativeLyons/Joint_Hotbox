#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Remove Root Animations
# COLOR: #7a5252
# TEXTCOLOR: #ffffff
#
#----------------------------------------------------------------------------------------------------------


import nuke, nukescripts

originalRoto = nuke.selectedNode()
nukescripts.node_copypaste()

roto = nuke.selectedNode()

track = nuke.createNode('Transform')
# Get the width and height of the frame format
#rVal = nuke.Root()
#xfVal = rVal.width()/2
#yfVal = rVal.height()/2

# Translate to center of frame format
#track['center'].setValue(xfVal, 0)
#track['center'].setValue(yfVal, 1)

x = int(originalRoto['xpos'].value())
y = int(originalRoto['ypos'].value())
roto.setXYpos(x+30,y+60)
#roto.autoplace()
#roto['label'].setValue(track['label'].value())
first = nuke.Root().knob('first_frame').getValue()
first = int(first)
last = nuke.Root().knob('last_frame').getValue()
last = int(last)+1
frame = first
Knobs = roto['curves']
root=Knobs.rootLayer
transform = root.getTransform()


roto.setName(roto.name().replace('_MM', '_STBL'))
roto['tile_color'].setValue(1908830719)

roto.setSelected(True)
track.setSelected(False)
while frame<last:
    r = track['rotate'].getValueAt(frame,0)
    rr = transform.getRotationAnimCurve(2)
    rr.addKey(frame,r)
    tx = track['translate'].getValueAt(frame,0)
    translx = transform.getTranslationAnimCurve(0)
    translx.addKey(frame,tx)
    ty = track['translate'].getValueAt(frame,1)
    transly = transform.getTranslationAnimCurve(1)
    transly.addKey(frame,ty)
    sx = track['scale'].getValueAt(frame,0)
    ssx = transform.getScaleAnimCurve(0)
    ssx.addKey(frame,sx)
    sy = track['scale'].getValueAt(frame,1)
    ssy = transform.getScaleAnimCurve(1)
    ssy.addKey(frame,sy)
    cx = track['center'].getValueAt(frame,0)
    ccx = transform.getPivotPointAnimCurve(0)
    ccx.addKey(frame,cx)
    cy = track['center'].getValueAt(frame,1)
    ccy = transform.getPivotPointAnimCurve(1)
    ccy.addKey(frame,cy)
    frame = frame+1

nuke.delete(track)
## Remove animation from all Roto and RotoPaint nodes

def eliminateRotoAnimation():

    nodeClasses = ['Roto', 'RotoPaint']

    invalidNodeClasses = ['Viewer', 'Backdrop', 'StickyNote']

    validSelNodes = [i for i in nuke.selectedNodes() if i.Class() not in invalidNodeClasses]

    curFrame = nuke.frame()

    if validSelNodes:
        rotoNodes = [i for i in nuke.selectedNodes() if i.Class() in nodeClasses]
        groupNodes = [i for i in nuke.selectedNodes() if i.Class() == 'Group']
    else:
        rotoNodes = [i for i in nuke.allNodes() if i.Class() in nodeClasses]
        groupNodes = [i for i in nuke.allNodes() if i.Class() == 'Group']

    for groupNode in checkForGroups(groupNodes):
        with groupNode:
            rotoNodes += [i for i in nuke.allNodes() if i.Class() in nodeClasses]

    for nd in rotoNodes:
        ndCurves = nd['curves']
        rootLayer = ndCurves.rootLayer
        for curve in rootLayer:

            #print dir(curve.getAttributes())
            #curveLtAttr = curve.getAttributes().kLifeTimeTypeAttribute
            #print dir(curveLtAttr)
            for point in curve:
                try:
                    point.center.removeAllKeys()
                    point.featherCenter.removeAllKeys()
                    point.featherLeftTangent.removeAllKeys()
                    point.featherRightTangent.removeAllKeys()
                    point.leftTangent.removeAllKeys()
                    point.rightTangent.removeAllKeys()
                except:
                    pass
                try:
                    point.removeAllKeys()
                except:
                    pass

            curveXform = curve.getTransform()
            curveXform.getPivotPointAnimCurve(0).removeAllKeys()
            curveXform.getPivotPointAnimCurve(1).removeAllKeys()
            curveXform.getRotationAnimCurve(0).removeAllKeys()
            curveXform.getRotationAnimCurve(1).removeAllKeys()
            curveXform.getRotationAnimCurve(2).removeAllKeys()
            curveXform.getScaleAnimCurve(0).removeAllKeys()
            curveXform.getScaleAnimCurve(1).removeAllKeys()
            curveXform.getSkewXAnimCurve(0).removeAllKeys()
            curveXform.getSkewXAnimCurve(1).removeAllKeys()
            curveXform.getTranslationAnimCurve(0).removeAllKeys()
            curveXform.getTranslationAnimCurve(1).removeAllKeys()
            curveXform.getExtraMatrixAnimCurve(0, 0).removeAllKeys()
            curveXform.getExtraMatrixAnimCurve(0, 1).removeAllKeys()
            curveXform.getExtraMatrixAnimCurve(0, 2).removeAllKeys()
            curveXform.getExtraMatrixAnimCurve(0, 3).removeAllKeys()
            curveXform.getExtraMatrixAnimCurve(1, 0).removeAllKeys()
            curveXform.getExtraMatrixAnimCurve(1, 1).removeAllKeys()
            curveXform.getExtraMatrixAnimCurve(1, 2).removeAllKeys()
            curveXform.getExtraMatrixAnimCurve(1, 3).removeAllKeys()
            curveXform.getExtraMatrixAnimCurve(2, 0).removeAllKeys()
            curveXform.getExtraMatrixAnimCurve(2, 1).removeAllKeys()
            curveXform.getExtraMatrixAnimCurve(2, 2).removeAllKeys()
            curveXform.getExtraMatrixAnimCurve(2, 3).removeAllKeys()
            curveXform.getExtraMatrixAnimCurve(3, 0).removeAllKeys()
            curveXform.getExtraMatrixAnimCurve(3, 1).removeAllKeys()
            curveXform.getExtraMatrixAnimCurve(3, 2).removeAllKeys()
            curveXform.getExtraMatrixAnimCurve(3, 3).removeAllKeys()

            xFormKeysNum = curveXform.getNumberOfTransformKeys()
            for keyNum in range(xFormKeysNum):
                curveXform.removeTransformKey(keyNum)

            curveAttrs = curve.getAttributes()
            if 'ltt' in curveAttrs:      #lifetime type to all
                curveAttrs.remove('ltt')
                curveAttrs.add('ltt', 0)

            attrIndex = 0

            while True:
                try:
                    curveAttrs.removeKeys(attrIndex)
                except:
                    break
                attrIndex += 1


        rootXform = rootLayer.getTransform()
        rootXform.getPivotPointAnimCurve(0).removeAllKeys()
        rootXform.getPivotPointAnimCurve(1).removeAllKeys()
        rootXform.getRotationAnimCurve(0).removeAllKeys()
        rootXform.getRotationAnimCurve(1).removeAllKeys()
        rootXform.getRotationAnimCurve(2).removeAllKeys()
        rootXform.getScaleAnimCurve(0).removeAllKeys()
        rootXform.getScaleAnimCurve(1).removeAllKeys()
        rootXform.getSkewXAnimCurve(0).removeAllKeys()
        rootXform.getSkewXAnimCurve(1).removeAllKeys()
        rootXform.getTranslationAnimCurve(0).removeAllKeys()
        rootXform.getTranslationAnimCurve(1).removeAllKeys()
        rootXform.getExtraMatrixAnimCurve(0, 0).removeAllKeys()
        rootXform.getExtraMatrixAnimCurve(0, 1).removeAllKeys()
        rootXform.getExtraMatrixAnimCurve(0, 2).removeAllKeys()
        rootXform.getExtraMatrixAnimCurve(0, 3).removeAllKeys()
        rootXform.getExtraMatrixAnimCurve(1, 0).removeAllKeys()
        rootXform.getExtraMatrixAnimCurve(1, 1).removeAllKeys()
        rootXform.getExtraMatrixAnimCurve(1, 2).removeAllKeys()
        rootXform.getExtraMatrixAnimCurve(1, 3).removeAllKeys()
        rootXform.getExtraMatrixAnimCurve(2, 0).removeAllKeys()
        rootXform.getExtraMatrixAnimCurve(2, 1).removeAllKeys()
        rootXform.getExtraMatrixAnimCurve(2, 2) .removeAllKeys()
        rootXform.getExtraMatrixAnimCurve(2, 3).removeAllKeys()
        rootXform.getExtraMatrixAnimCurve(3, 0).removeAllKeys()
        rootXform.getExtraMatrixAnimCurve(3, 1).removeAllKeys()
        rootXform.getExtraMatrixAnimCurve(3, 2).removeAllKeys()
        rootXform.getExtraMatrixAnimCurve(3, 3).removeAllKeys()
        rootAttrs = rootLayer.getAttributes()
        attrIndex = 0
        while True:
            try:
                rootAttrs.removeKeys(attrIndex)
            except:
                break
            attrIndex += 1
        for name, knob in nd.knobs().items():
            if knob.isAnimated():
                knob.clearAnimated()
        ndCurves.changed() # updates the Roto UI


if __name__ == '__main__':
    eliminateRotoAnimation()
