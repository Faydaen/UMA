import sys

import_path = "C:\\Program Files\\Blender Foundation\\Blender 2.83\\2.83\\scripts\\addons\\UMA"

sys.path.append(import_path)

import addCube
import addCubePanel


import bpy

print(bpy.utils.register_class)

def register():
    try:
        addCube.register()
    except Exception:
        addCube.unregister()
        addCube.register()
    
    try:
        addCubePanel.register()
    except Exception:
        addCubePanel.unregister()
        addCubePanel.register()

    #addCubePanel.register()
 
def unregister():
    addCube.unregister()
    addCubePanel.unregister()
 
if __name__ == "__main__":
    #unregister()
    register()