bl_info = {
    "name": "UMA",
    "author": "Faydaen",
    "version": (0, 1, 1),
    "blender": (2, 80, 0),
    "location": "View3D",
    "description": "Some tools to help export character to UMA",
    "category": "Development",
}


import sys
import os
import importlib

print("___________________________________________________________________________________________________________________________________________________________________________")

addons_dir = "C:\\Program Files\\Blender Foundation\\Blender 2.83\\2.83\\scripts\\addons"
addon_name ="UMA"
modulesNames = ['addCube','addCubePanel']


#import_path = "C:\\Program Files\\Blender Foundation\\Blender 2.83\\2.83\\scripts\\addons\\UMA"
#sys.path.append(import_path)
#from . import addCube
#from . import addCubePanel

import_path = os.path.join(addons_dir, addon_name)
print(import_path)




sys.path.append(import_path)


