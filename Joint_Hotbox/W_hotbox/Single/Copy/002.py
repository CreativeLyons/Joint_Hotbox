#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: RG -> Motion
# COLOR: #435b3e
#
#----------------------------------------------------------------------------------------------------------

for n in nuke.selectedNodes():
    n['from0'].setValue("rgba.red")
    n['to0'].setValue("motion.u")
    n['from1'].setValue("rgba.green")
    n['to1'].setValue("motion.v")
