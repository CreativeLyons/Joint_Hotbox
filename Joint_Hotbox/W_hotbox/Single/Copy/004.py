#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Inject New Channel
# COLOR: #111111
# TEXTCOLOR: #ff0000
#
#----------------------------------------------------------------------------------------------------------

n = nuke.selectedNode()
nodeClass = n.Class()

if nodeClass == 'Copy':
    nodeName = n.name()
    to0 = n.knob('to0')
    panel = nuke.Panel('New Single Channel')
    panel.setTitle('Enter New Single Channel Name')
    panel.setWidth(350)
    panel.addSingleLineInput('channelName', '')
    result = panel.show()
    if result:
        channelName = panel.value('channelName')
        if channelName != '':
            n.setName("Copy_InjectChannel")
            channelName = '_'.join(channelName.split(' '))
            fullChannelName = channelName + '.red'
            nuke.Layer('{}'.format(channelName), [fullChannelName])
            to0.setValue(fullChannelName)
            
            n.knob('tile_color').setValue(437918463)
            n.knob('note_font_color').setValue(4280090879)
