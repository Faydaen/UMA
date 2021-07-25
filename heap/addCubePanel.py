import bpy

# class addCubePanel(bpy.types.Panel):
#     bl_idname = "panel.add_cube_panel"
#     bl_label = "AddCube"
#     bl_space_type = "VIEW_3D"
#     bl_region_type = "TOOLS"
#     bl_category = "Add Cube Panel"
# 
#     def draw(self, context):
#         self.layout.operator("mesh.add_cube_sample", icon='MESH_CUBE', text="Add Cube")

class DazToUMAPanel(bpy.types.Panel):
    bl_idname = "daz_to_uma_panel"
    bl_label = "import to uma"
    bl_space_type = "VIEW_3D" 
    bl_region_type = "UI"
    bl_category = "UMA"
 
    def draw(self, context):
        row = self.layout.row()
        self.layout.label(text="Hello World")
        row.operator('object.move_x', text='подвинуть всё') # todo rm
        
        #row.operator('mash.daz_to_uma', text='Выделить вертексы') # название кнопки
        #row.operator('mash.remove_bones', text='Удалить кости')
        
        #row = self.layout.row()
        #row.operator('mash.add_system_bones', text='Служебные кости')

        #row = self.layout.row()
        #row.operator('mash.daz_to_uma', text='Объеденить материалы')
        #row.operator('mash.daz_to_uma', text='Скомбинировать текстуры')        




def register():
    print("[+] "+__name__)
    bpy.utils.register_class(DazToUMAPanel)

def unregister():
    print("[-] "+__name__)
    bpy.utils.unregister_class(DazToUMAPanel)