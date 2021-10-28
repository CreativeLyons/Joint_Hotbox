#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: CardToCard3D
# COLOR: #840000
# TEXTCOLOR: #ffffff
#
#----------------------------------------------------------------------------------------------------------

thisCard = nuke.selectedNode()
xPos = thisCard.xpos()
yPos = thisCard.ypos()

xfo = thisCard["xform_order"].value()
ro = thisCard["rot_order"].value()
t = thisCard.knob("translate")
r = thisCard.knob("rotate")
s = thisCard.knob("scaling")
u_s = thisCard.knob("uniform_scale")
sk = thisCard.knob("skew")
p = thisCard.knob("pivot")

c3d = nuke.nodes.Card3D()
c3d.setXYpos(xPos+100, yPos)

c3d.knob("xform_order").setValue(xfo)
c3d.knob("rot_order").setValue(ro)
c3d.knob("translate").fromScript(t.toScript())
c3d.knob("rotate").fromScript(r.toScript())
c3d.knob("scaling").fromScript(s.toScript())
c3d.knob("uniform_scale").fromScript(u_s.toScript())
c3d.knob("skew").fromScript(sk.toScript())
c3d.knob("pivot").fromScript(p.toScript())
