import bpy
import math

# перейти в режим редакитрования из любого состояния
def edit(objectName):
        # переходим в объектный режим
        bpy.ops.object.mode_set(mode='OBJECT')

        # сбрасываем выделение со всего
        bpy.ops.object.select_all(action='DESELECT')

        # делаем активным объект
        bpy.context.view_layer.objects.active = bpy.data.objects[objectName]

        # входим в режим редактирования
        bpy.ops.object.mode_set(mode='EDIT')
        
# выделить и активировать одну кость (с остальных снять выделение)
def selectOneBone(boneName = 'head'):
    for a in bpy.context.object.data.edit_bones:
        a.select = False
    bpy.context.object.data.edit_bones[boneName].select = True
    bpy.data.armatures[0].edit_bones.active  = bpy.context.object.data.edit_bones[boneName]

# получить список имён выделенных костей
def getSelectedBonesNames():
    selected = []
    for a in bpy.context.object.data.edit_bones:
        if (a.select):
            selected.append(a.name)
    return selected        

def assaciateSelectedWetixWith(vertexGroupName):
    pass

# выделить вертексы указанных групп вертексов
def selectVetetex(names = [], objectName = 'Genesis8Female.Shape'):
    # снимаем выделение со всех вертексов
    bpy.ops.mesh.select_all(action='DESELECT')
    vg = bpy.data.objects[objectName].vertex_groups
    vgNames = [v.name for v in vg]
    for n in names:
        if n in vgNames:
            vg.active_index = vg[n].index
            bpy.ops.object.vertex_group_select()


class DazToUMA(bpy.types.Operator):
    bl_idname = 'mash.daz_to_uma' 
    bl_label = 'daz to uma' 
    bl_options = {"REGISTER", "UNDO"} # разрешить Ctrl+Z

    # главная функция
    def execute(self, context):

        edit('Genesis8Female')      
        selectOneBone()
        
        # тут уже не выделение кости а обработка их
        
        # выделить всех потомков выделенной кости shift + g (текущая кость так же остается выделенной)
        bpy.ops.armature.select_similar(type='CHILDREN')
        
        bonesNames = getSelectedBonesNames()
        
        edit('Genesis8Female.Shape')
        
        selectVetetex(names = bonesNames)
        
        return {"FINISHED"} 
    
class AddSystemBones(bpy.types.Operator):    
    bl_idname = 'mash.add_system_bones' 
    bl_label = 'add system bones' 
    bl_options = {"REGISTER", "UNDO"}
    
    def execute(self, context):
        edit('Genesis8Female')
        
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
        edit('Genesis8Female') 
        
        boneName = 'head'     
        selectOneBone(boneName) # выделяем кость
        bpy.ops.armature.select_similar(type='CHILDREN') # выделяем потомков кости
        bpy.context.object.data.edit_bones[boneName].select = False # снимаем выделение кости
        return {"FINISHED"}
            
        

        
            

# добавит вкладку в меню (которое вызывется по N) в котрой будет кнопка
class DazToUMAPanel(bpy.types.Panel):
    bl_idname = "daz_to_uma_panel"
    bl_label = "import to uma"
    bl_space_type = "VIEW_3D" 
    bl_region_type = "UI"
    bl_category = "UMA"
 
    def draw(self, context):
        row = self.layout.row()
        row.operator('mash.daz_to_uma', text='Выделить вертексы') # название кнопки
        row.operator('mash.remove_bones', text='Удалить кости')
        
        row = self.layout.row()
        row.operator('mash.add_system_bones', text='Служебные кости')

        #row = self.layout.row()
        #row.operator('mash.daz_to_uma', text='Объеденить материалы')
        #row.operator('mash.daz_to_uma', text='Скомбинировать текстуры')        


 
 
def register():
    bpy.utils.register_class(DazToUMA)
    bpy.utils.register_class(AddSystemBones) 
    bpy.utils.register_class(RemoveBones) 
    bpy.utils.register_class(DazToUMAPanel)
 
def unregister():
    bpy.utils.unregister_class(DazToUMA)
    bpy.utils.unregister_class(AddSystemBones)
    bpy.utils.unregister_class(RemoveBones)
    bpy.utils.unregister_class(DazToUMAPanel)
    

register()
