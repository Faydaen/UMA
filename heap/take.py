from os import name
import bpy
from bpy.props import IntProperty, FloatProperty, StringProperty



class UMA_PT_Tools_Panel(bpy.types.Panel):
    """Панель для работы с костями"""
    bl_label = "UMA Tools"
    bl_idname = "UMA_PT_bone_panel"
    bl_space_type = "VIEW_3D" 
    bl_region_type = "UI"
    bl_category = "UMA"

    def draw(self, context):
        self.layout.label(text="Работа с костями")

        self.layout.prop(context.object,'my_global_string')
        self.layout.operator("uma.rename", text="Переименовать").cube_name = context.object.my_global_string

        #props.cube_name = context.object.my_global_string



class UMA_OP_Rename(bpy.types.Operator):
    """rename obj"""
    bl_idname = "uma.rename"
    bl_label = "Rename"
    bl_options = {'REGISTER', 'UNDO'}

    cube_name: bpy.props.StringProperty(name="name of cube",default="new 3d cube")

    def invoke(self, context, event):
        print(self.cube_name)
        context.object.name = self.cube_name
        return {'FINISHED'}  



def register():
    bpy.types.Object.my_global_string = bpy.props.StringProperty(name="Custom string")
    bpy.utils.register_class(UMA_OP_Rename)
    bpy.utils.register_class(UMA_PT_Tools_Panel)

