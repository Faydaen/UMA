import bpy


class UMA_PT_tools_panel(bpy.types.Panel):
    """Панель для работы с костями"""
    bl_label = "UMA Tools"
    bl_idname = "UMA_PT_bone_panel"
    bl_space_type = "VIEW_3D" 
    bl_region_type = "UI"
    bl_category = "UMA"

    def draw(self, context):
        self.layout.label(text="Работа с костями")
        row = self.layout.row()
        row.operator("uma.combine_children_bones", text="Объеденить кость")
        row = self.layout.row()
        row.operator("uma.add_system_bones", text="Добавить служебные кости")

def register():
    bpy.utils.register_class(UMA_PT_tools_panel)

def unregister():
    bpy.utils.unregister_class(UMA_PT_tools_panel)
    
    
