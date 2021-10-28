#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# IGNORE CLASSES: 0
#
#----------------------------------------------------------------------------------------------------------

ns = nuke.selectedNodes()
for n in ns:
    knobs = []
    for i in n.knobs():
        knobs.append(i)
    if 'User' in knobs:
        if n.knob('User').label() == "CProject":
            ret = True
