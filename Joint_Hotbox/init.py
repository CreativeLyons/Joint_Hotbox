import os

def createWHotboxButtonsJoint():
    ''' If the folder is available inside the stamps package, it gets appended into the W_Hotbox packages. '''
    # DONE W_Hotbox buttons imported from stamps extras path
    w_hotbox_buttons_path = os.path.dirname(__file__).replace("\\","/")+"/W_hotbox"
    if os.path.exists(w_hotbox_buttons_path):
        hotbox_paths = ""
        hotbox_names = ""
        if "W_HOTBOX_REPO_PATHS" in os.environ.keys() and "W_HOTBOX_REPO_NAMES" in os.environ.keys():
            hotbox_paths = os.environ["W_HOTBOX_REPO_PATHS"]
            hotbox_names = os.environ["W_HOTBOX_REPO_NAMES"]
        if hotbox_paths != "":
            hotbox_paths += os.pathsep
        if hotbox_names != "":
            hotbox_names += os.pathsep
        os.environ["W_HOTBOX_REPO_PATHS"] = hotbox_paths + os.path.dirname(__file__).replace("\\","/")+"/W_hotbox"
        os.environ["W_HOTBOX_REPO_NAMES"] = hotbox_names + "Joint_Hotbox"

createWHotboxButtonsJoint()
