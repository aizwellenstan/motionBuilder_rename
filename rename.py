from pyfbsdk import *

def rename(name, before, after):
    if "MoCap" in name: return name
    return name.replace(before, after)

def search_and_select_skeleton(node, skeletons):
    if isinstance(node, FBModelSkeleton):
        skeletons.append(node)
    for child in node.Children:
        child_name = child.Name
        child_name = rename(child_name, "_L", "_MoCap_L")
        child_name = rename(child_name, "_R", "_MoCap_R")
        child_name = rename(child_name, "_M", "_MoCap_M")
        child.Name = child_name
        search_and_select_skeleton(child, skeletons)

# Get the root node of the current scene
root = FBSystem().Scene.RootModel

# Search for all the FBModelSkeleton nodes and select them
skeletons = []
search_and_select_skeleton(root, skeletons)
for skeleton in skeletons:
    skeleton.Selected = True
