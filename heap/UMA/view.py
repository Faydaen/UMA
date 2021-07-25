import bpy

class BonesPanel(bpy.types.Panel):
    bl_idname = "daz_to_uma_panel"
    bl_label = "import to uma"
    bl_space_type = "VIEW_3D" 
    bl_region_type = "UI"
    bl_category = "UMA"
 
    def draw(self, context):
        row = self.layout.row()
        #row.operator('mash.daz_to_uma', text='Выделить вертексы') # название кнопки
        row.operator('mash.remove_bones', text='Удалить кости')
        
        row = self.layout.row()
        row.operator('mash.add_system_bones', text='Служебные кости')