#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Copy/Paste Knob Values
#
#----------------------------------------------------------------------------------------------------------

ns = nuke.selectedNodes()
if len(ns)>1:
    nf = nuke.selectedNodes()[-1]
    for ni in range(len(ns)-1):
        nt = ns[ni]
        for kf in nf.knobs():
            if kf in nt.knobs() and kf not in ["xpos","ypos","name"]:
                if nt[kf].Class() not in ["Font_Knob","Text_Knob","BeginTabGroup_Knob","EndTabGroup_Knob","Script_Knob"]:
                    try:
                        nt[kf].fromScript(nf[kf].toScript())
                    except:
                        pass
