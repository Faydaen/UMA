bl_info = {
    "name": "UMA",
    "author": "Faydaen",
    "version": (0, 1, 1),
    "blender": (2, 80, 0),
    "location": "View3D",
    "description": "Some tools to help export character to UMA",
    "category": "Development",
}

modulesNames = ['addCube','addCubePanel']
#modulesNames = []

 
import sys
import importlib
 
modulesFullNames = {}
for currentModuleName in modulesNames:
    modulesFullNames[currentModuleName] = ('{}.{}'.format(__name__, currentModuleName))
 
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
    
    
    
    
    
    