#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Checker Align Nodes
# COLOR: #37595b
# TEXTCOLOR: #ffffff
#
#----------------------------------------------------------------------------------------------------------

count=0
moveBy=75

for i in nuke.selectedNodes():
    m=count%3
    i.autoplace()
    i.setXYpos(i.xpos(), i.ypos()+(m*moveBy))
    count+=1
