#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Create + Inject New Layer
# COLOR: #111111
# TEXTCOLOR: #ff0000
#
#----------------------------------------------------------------------------------------------------------

n = nuke.selectedNode()
out2 = n.knob('out2')

xPos = n.xpos()
yPos = n.ypos()
name = n.name()

panel = nuke.Panel('New Layer')
panel.setTitle('Enter New Layer Name')
panel.setWidth(350)
panel.addSingleLineInput('layerName', '')
result = panel.show()
if result:
    layerName = panel.value('layerName')
    layerName = ''.join(layerName.split(' '))
    nuke.Layer('{}'.format(layerName) , [
    '{}.red'.format(layerName),
    '{}.green'.format(layerName),
    '{}.blue'.format(layerName),
    '{}.alpha'.format(layerName)])
    out2.setValue('{}'.format(layerName))
    n.knob('label').setValue('[value in] [ expr { [value out2] == "none" ? " " : [concat -> [value out2]] }]')
    n.knob('black').setValue('red')
    n.knob('white').setValue('green')
    n.knob('red2').setValue('blue')
    n.knob('green2').setValue('alpha')
    copy = nuke.createNode("Copy")
    copy.setName('Copy_Layer')
    copy.setInput(1, n)
    copy.setXYpos(xPos+120, yPos)
    copy.autoplace()
    copy.knob('from0').setValue("none")
    copy.knob('to0').setValue("none")
    copy.knob('channels').setValue('{}'.format(layerName))
    copy.knob('note_font_color').setValue(4294967295)
