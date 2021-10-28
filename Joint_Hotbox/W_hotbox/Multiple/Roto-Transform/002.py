#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Combine Roto/Transform
# COLOR: #006b27
# TEXTCOLOR: #ffffff
#
#----------------------------------------------------------------------------------------------------------

import nuke
import nukescripts

n = nuke.selectedNodes()

for i in n:
    if i.Class() == 'Roto':
        roto = i
    if i.Class() == 'Transform':
        transform = i

for i in nuke.selectedNodes():
    i['selected'].setValue(False)

roto['selected'].setValue(True)

nukescripts.node_copypaste()

roto = nuke.selectedNode()
track = nuke.toNode('{}'.format(transform.name()))

x = int(roto['xpos'].value())
y = int(roto['ypos'].value())
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


roto.setName(roto.name() + '_MM')
roto['tile_color'].setValue(11632127)

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
