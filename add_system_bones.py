import bpy
import sys
import importlib
import functions

importlib.reload(sys.modules['functions'])

class UMA_OP_add_system_bones(bpy.types.Operator):    
    bl_idname = 'uma.add_system_bones' 
    bl_label = 'Add system bones' 
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        functions.edit('Genesis3Female')
        
        self.createBone('Position')
        self.createBone('Global')
        
        self.submiseve('Global','Position')
        self.submiseve('Position','hip')
        
        return {"FINISHED"}
            
        
    # создаём маленкую кость в начале координат    
    def createBone(self,boneName):
        bone = bpy.data.armatures[0].edit_bones.new(boneName)
        bone.head = (0,0,0)
        bone.tail = (0,0,0.1)
        
    # делаем одну кость подчинёной другой
    def submiseve(self,parent,child):
        bpy.data.armatures[0].edit_bones[child].parent = bpy.data.armatures[0].edit_bones[parent]



def register():
    bpy.utils.register_class(UMA_OP_add_system_bones)

def unregister():
    bpy.utils.unregister_class(UMA_OP_add_system_bones)


