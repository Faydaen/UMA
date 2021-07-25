import bpy
import bmesh
import sys
import importlib
import functions

importlib.reload(sys.modules['functions'])

functions.assaciate_selected_wetix_with()

class UMA_OP_combine_children_bones(bpy.types.Operator):
    """Combine all children bones"""
    bl_idname = "uma.combine_children_bones"
    bl_label = "Combine children"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        self.select_vertix()
        self.assine_bones()
        self.remove_bones()
        return {"FINISHED"}

    # выделяем все вертексы которые пренадлежат кости головы, и её потомкам
    def select_vertix(self):
        functions.edit('Genesis3Female') 
        functions.select_one_bone("head")
        bpy.ops.armature.select_similar(type='CHILDREN')
        bonesNames = functions.get_selected_bones_names()
        functions.edit('Genesis3Female.Shape')
        functions.select_vetetex(names = bonesNames, objectName = 'Genesis3Female.Shape')

    def assine_bones(self):
        # ищем вертекс группу head
        vertex_groups = bpy.context.active_object.vertex_groups 
        vertex_group = None
        for vg in vertex_groups:
            if vg.name == "head":
                vertex_group = vg

        if vertex_group is None:
            print("vertex_group not found")
            return

        # получаем индексы всех выделенных вертиксов
        bm = bmesh.from_edit_mesh(bpy.data.meshes['Genesis3Female'])
        selected_vetix = []
        for v in bm.verts:
            if v.select:
                selected_vetix.append(v.index)

        # добавлем в группу головы все выделенные вертексы
        bpy.ops.object.mode_set(mode='OBJECT') # нужно перейти в объектный режим чтобы назначить вертексы
        vertex_group.add(selected_vetix, 1.0, "ADD")

    # удаляем все кости кроме кости головы
    def remove_bones(self):
        functions.edit('Genesis3Female') 
        functions.select_one_bone('head') # выделяем кость
        bpy.ops.armature.select_similar(type='CHILDREN') # выделяем потомков кости
        bpy.context.object.data.edit_bones['head'].select = False
        bpy.ops.armature.delete()







def register():
    bpy.utils.register_class(UMA_OP_combine_children_bones)

def unregister():
    bpy.utils.unregister_class(UMA_OP_combine_children_bones)


