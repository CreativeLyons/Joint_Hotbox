#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Terminal Localize
# COLOR: #517a10
# TEXTCOLOR: #ffffff
#
#----------------------------------------------------------------------------------------------------------

from pprint import pprint

import os

nuke.selectedNode().knob('localizationPolicy').setValue(0)

def prepLocalize():
    
    validClasses = ["Read", "DeepRead"]
    selected =  nuke.selectedNodes()

    allRead = []
    if selected == []:
 
        allRead=nuke.allNodes("Read")
        allDeepRead=nuke.allNodes("DeepRead")
        allRead=allRead+allDeepRead

    else:

        for node in selected:
            if node.Class() in validClasses:
                 allRead.append(node)



    allFilesList=list()
    localCachePath=nuke.toNode("preferences")["localCachePath"].evaluate()

    print localCachePath

    script_name=os.path.basename(nuke.root()["name"].value()).replace(".nk","")

    localize_file="%s.%s" % (script_name,"batch")


    localize_file_path = os.path.join(localCachePath,"batch_files",localize_file)
    print localize_file_path

    localize_dir=os.path.dirname(localize_file_path)
    print localize_dir

    if not os.path.isdir(localize_dir):
        os.makedirs(localize_dir)


    f=open(localize_file_path,"w+")


    for read in allRead:
        origfirst=read["origfirst"].value()    
        origlast=read["origlast"].value()  

        frame_range=range(origfirst,origlast+1)
        for frame in frame_range:
            file_name=read["file"].evaluate(frame).replace("/corky","")+"\n"
            f.write(file_name)



    f.close()

    print "##############################      COPY/PASTE ON TERMINAL WINDOW  ######################################"

    rsync_path="rsync --files-from=%s /corky %s/_corky/ -P" % (localize_file_path,localCachePath)

    print rsync_path
    print "#########################################################################################################"

    nuke.message("Run the follow command in a terminal window to Localize in the Background:" + "\n" + "\n" + rsync_path)

    #command = "gnome-terminal -e '%s'" % rsync_path
    
    #os.system(command)

prepLocalize()
