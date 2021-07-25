import bpy
import math

# === переименовываем всё ===
# todo переименовывать и текстуру

def rename_obj(key, name):
    allObj = bpy.context.scene.objects;
    if (key in allObj):
        allObj[key].name = name

def rename_mesh(key, name):
    allMeshes = bpy.data.meshes
    if (key in allMeshes):
        allMeshes[key].name = name

def rename_mat(key, name):
    allMat = bpy.data.materials
    if (key in allMat):
        allMat[key].name = name

def rename_arm(key, name):
    allArmatures = bpy.data.armatures
    if (key in allArmatures):
        allArmatures[key].name = name        

def rename(key, name):
    rename_obj(key+"Mesh", name)
    rename_mesh(key, name)
    rename_mat(key,name)


# общие части
rename_obj("Game_engine", "armature")
rename_arm("Game_engine", "skeleton") 
rename("low-poly","eyes")

# женские части
rename("adult_female_genitalia","female")
rename("ponytail01","hair_ponytail")

rename("costume_leggings","leggings")
rename("highneckcroptop","croptop")
rename("shoes05","shoes_white")
rename("spaghetti_top","top")
rename("sport_briefs01","briefs")

# мужские части
rename("adult_male_genitalia","male")
rename("short01","hair_casual")

rename("male_elegantsuit01", "elegant_suit")
rename("shoes03", "shoes_black")
rename("simple_pants", "male_pants")



# === номализуем все ===

# -- делаем отображение костей в виде палок --
def change_bone_view():
    # клик на арматуру
    bpy.context.view_layer.objects.active = bpy.data.objects['armature']
    # меняем режим отображение костей
    bpy.context.object.data.display_type = 'STICK'
    
    
# после этого шага, фигура должна лечь
# (и после входа в режим редоктирования сетки не должны возвращатся менять положение)    
def clear_pose():
    # -- очищаем позу --
    bpy.context.view_layer.objects.active = bpy.data.objects['armature'] 
    bpy.ops.object.mode_set(mode='POSE') # в режим позы
    bpy.ops.pose.select_all(action='SELECT') # выделяем все
    bpy.ops.pose.transforms_clear() # очищаем 


def rotate_back():
    # -- вращаем на 90 градусов (обратно)--
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.data.objects['armature'].rotation_euler.rotate_axis('X', math.radians(-90))


# после этого шага, если удалить арматуру (в объектном режиме) меш
# не должен стать большим и развернутым
def clear_all_transform():
    for s in bpy.data.objects:
        bpy.context.view_layer.objects.active = bpy.data.objects[s.name]
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
        
    
change_bone_view()
clear_pose()
rotate_back()
clear_all_transform()



# === работа с костями ===

# пытаемся переименовать кость
if 'Root' in bpy.data.armatures['skeleton'].bones:
    bpy.data.armatures['skeleton'].bones['Root'].name = 'Position'
    
# выделяем и активируем объект, переходим в режим редактирования
bpy.data.objects['armature'].select_set(state=True)
bpy.context.view_layer.objects.active = bpy.data.objects['armature']
bpy.ops.object.mode_set(mode='EDIT', toggle=False)

# меняем её расположеение
bpy.data.armatures['skeleton'].edit_bones['Position'].head = (0,0,0)
bpy.data.armatures['skeleton'].edit_bones['Position'].tail = (0,0,0.1)


# добавляем глобальную кость
bpy.ops.object.mode_set(mode='EDIT', toggle=False)
global_bone = bpy.data.armatures['skeleton'].edit_bones.new('Global')
global_bone.head = (0,0,0)
global_bone.tail = (0,0,0.1)

# делаем кость Position подчиненной кости Global
bpy.ops.object.mode_set(mode='EDIT', toggle=False)
bpy.data.armatures['skeleton'].edit_bones['Position'].parent = bpy.data.armatures['skeleton'].edit_bones['Global']



# === продублировать меш
def deselectAll():
    for s in bpy.context.selected_objects:
        s.select_set(state=False)

def renameSelected(newName):
    for s in bpy.context.selected_objects:
        s.name = newName

def dublicateMesh(key):
    allObj = bpy.context.scene.objects;
    if (key in allObj):
        bpy.context.view_layer.objects.active = bpy.data.objects[key]
        bpy.ops.object.mode_set(mode='OBJECT')
        deselectAll()
        bpy.data.objects[key].select_set(state=True)
        bpy.ops.object.duplicate_move()
        renameSelected("seamsMesh")
        
        
dublicateMesh("female")
dublicateMesh("male")

################################################################################
################################################################################
################################################################################
################################################################################

# todo разбить на файлы, и оформить как аддон


class importToUMA(bpy.types.Operator):
    bl_idname = 'mash.import_to_uma' 
    bl_label = 'import uma' 
    bl_options = {"REGISTER", "UNDO"} # разрешить Ctrl+Z

    # главная функция
    def execute(self, context):

        
        active = bpy.context.view_layer.objects.active
        bpy.ops.object.select_all(action='SELECT') # выделяем всё
        # снимаем выделение с активного объекта
        bpy.data.objects[active.name].select_set(False) 
        # снимвам выделение с арматуры
        bpy.data.objects['armature'].select_set(False)
        # удаляем все выделенные
        bpy.ops.object.delete()
        
        
        
        return {"FINISHED"} 

# добавит вкладку в меню (которое вызывется по N) в котрой будет кнопка
class importToUmaPanel(bpy.types.Panel):
    bl_idname = "import_to_uma_panel"
    bl_label = "import to uma"
    bl_space_type = "VIEW_3D" 
    bl_region_type = "UI"
    bl_category = "UMA"
 
    def draw(self, context):
        row = self.layout.row()
        row.operator('mash.import_to_uma', text='import to uma') # название кнопки

 
 
def register():
    bpy.utils.register_class(importToUMA) 
    bpy.utils.register_class(importToUmaPanel)
 
def unregister():
    bpy.utils.unregister_class(importToUMA)
    bpy.utils.unregister_class(importToUmaPanel)
    

register()


















