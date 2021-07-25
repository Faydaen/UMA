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


import_path = os.path.join(addons_dir, addon_name)
print(import_path)

#import addCube
#addCube.register()






print("---- modules full names ----")
modulesFullNames = {}
for currentModuleName in modulesNames:
    modulesFullName = '{}.{}'.format(addon_name, currentModuleName)
    modulesFullNames[currentModuleName] = modulesFullName
    globals()[modulesFullName] = importlib.import_module(modulesFullName)
    print('modulesFullNames[{}] = {}'.format(currentModuleName, modulesFullName))
print("")

print("---- globals ----")
gg = globals().copy()
for g in gg:
    print('glob::{} = {}'.format(g,type(gg[g])))
print("")

print("---- uma modules ----")
for m in sys.modules:
    if (m.startswith("UMA") or m.startswith("addCube")):
        print("{} - {}".format(m, sys.modules[m]))





