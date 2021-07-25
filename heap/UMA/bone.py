import bpy
import functions

class AddSystemBones(bpy.types.Operator):    
    bl_idname = 'mash.add_system_bones' 
    bl_label = 'add system bones' 
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        functions.edit('Genesis8Female')
        
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
    
    
    
class RemoveBones(bpy.types.Operator):    
    bl_idname = 'mash.remove_bones' 
    bl_label = 'remove bones' 
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        functions.edit('Genesis8Female') 
        
        boneName = 'head'     
        functions.selectOneBone(boneName) # выделяем кость
        bpy.ops.armature.select_similar(type='CHILDREN') # выделяем потомков кости
        bpy.context.object.data.edit_bones[boneName].select = False # снимаем выделение кости
        return {"FINISHED"}
            
        

        
        