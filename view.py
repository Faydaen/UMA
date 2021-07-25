import bpy


class UMA_PT_tools_panel(bpy.types.Panel):
    """Панель для работы с костями"""
    bl_label = "UMA Tools"
    bl_idname = "UMA_PT_bone_panel"
    bl_space_type = "VIEW_3D" 
    bl_region_type = "UI"
    bl_category = "UMA"

    def draw(self, context):
        self.layout.label(text="Объеденить дочерние кости")
        row = self.layout.row()
        row.operator("uma.select_all_children", text="Выделить вертиксы")
        #row = self.layout.row()
        # todo - change
        #row.operator("uma.select_all_children", text="Выделить вертексы")






def register():
    bpy.utils.register_class(UMA_PT_tools_panel)

def unregister():
    bpy.utils.unregister_class(UMA_PT_tools_panel)
    
    
