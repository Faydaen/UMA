import sys
import os
import importlib

print("___________________________________________________________________________________________________________________________________________________________________________")


addons_dir = "C:\\Program Files\\Blender Foundation\\Blender 2.83\\2.83\\scripts\\addons"
addon_name ="UMA"
modulesNames = ['view','select_children']
import_path = os.path.join(addons_dir, addon_name)

# для того чтобы можно было импортировать из модулей (например для function)
if (import_path not in sys.path):
    sys.path.append(import_path)

 
modulesFullNames = {}
for currentModuleName in modulesNames:
    modulesFullNames[currentModuleName] = ('{}.{}'.format(addon_name, currentModuleName))


for currentModuleFullName in modulesFullNames.values():
    if currentModuleFullName in sys.modules:
        print("reload "+currentModuleFullName)
        importlib.reload(sys.modules[currentModuleFullName])
    else:
        globals()[currentModuleFullName] = importlib.import_module(currentModuleFullName)
        setattr(globals()[currentModuleFullName], 'modulesNames', modulesFullNames)
 
def register():
    for currentModuleName in modulesFullNames.values():
        if currentModuleName in sys.modules:
            if hasattr(sys.modules[currentModuleName], 'register'):
                sys.modules[currentModuleName].register()
 
def unregister():
    for currentModuleName in modulesFullNames.values():
        if currentModuleName in sys.modules:
            if hasattr(sys.modules[currentModuleName], 'unregister'):
                sys.modules[currentModuleName].unregister()
    
if __name__ == "__main__":
    register()