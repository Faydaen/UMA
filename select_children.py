import bpy
import functions
import importlib, sys
import bmesh

class UMA_OP_select_all_children(bpy.types.Operator):
    """Select all children of object"""
    bl_idname = "uma.select_all_children"
    bl_label = "Select all child"
    bl_options = {'REGISTER', 'UNDO'}


    

    def execute(self, context):
        self.select_vertix()
        self.assine_bones()
        self.remove_bones()
        return {"FINISHED"}

    # выделяем все вертексы которые пренадлежат кости головы, и её потомкам
    def select_vertix(self):
        functions.edit('Genesis3Female') 
        functions.selectOneBone("head")
        bpy.ops.armature.select_similar(type='CHILDREN')

        ## снимаем выделение с кости предка, чтобы получить вертексы только потомков
        # bpy.data.objects['head'].select_set(False)

        bonesNames = functions.getSelectedBonesNames()
        #print(bonesNames)
        functions.edit('Genesis3Female.Shape')
        functions.selectVetetex(names = bonesNames, objectName = 'Genesis3Female.Shape')

    def assine_bones(self):
        # ищем вертекс группу head
        vertex_groups = bpy.context.active_object.vertex_groups
        vertex_group = None
        for vg in vertex_groups:
            if vg.name == "head":
                vertex_group = vg
        #print(vertex_group.name)

        if vertex_group is None:
            print("vertex_group not found")
            return

        # получаем индексы всех выделенных вертиксов
        bm=bmesh.from_edit_mesh(bpy.data.meshes['Genesis3Female'])
        selected_vetix=[]
        for v in bm.verts:
            if v.select:
                selected_vetix.append(v.index)
                #print(v.index, end=' ')

        # добавлем в группу головы все выделенные вертексы
        bpy.ops.object.mode_set(mode='OBJECT') # нужно перейти в объектный режим чтобы назначить вертексы
        #print(selected_vetix)
        vertex_group.add(selected_vetix, 1.0, "ADD")

    # удаляем все кости кроме кости головы
    def remove_bones(self):
        functions.edit('Genesis3Female') 
        functions.selectOneBone('head') # выделяем кость
        bpy.ops.armature.select_similar(type='CHILDREN') # выделяем потомков кости
        bpy.context.object.data.edit_bones['head'].select = False
        bpy.ops.armature.delete()




# перезагрузка модуля 
# todo - remove
importlib.reload(sys.modules['functions'])



def register():
    bpy.utils.register_class(UMA_OP_select_all_children)

def unregister():
    bpy.utils.unregister_class(UMA_OP_select_all_children)


