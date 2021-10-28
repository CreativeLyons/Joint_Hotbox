#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Create Sandwich
#
#----------------------------------------------------------------------------------------------------------

dA = nuke.selectedNode()
dAname = dA.name()
dB = nuke.createNode('Dilate')
dB.knob('size').setValue(0,0)
dB.knob('size').setValue(1,1)
dB.knob('size').setExpression('-{}.size'.format(dAname), 0 )
dB.knob('size').setExpression('-{}.size'.format(dAname), 1 )
