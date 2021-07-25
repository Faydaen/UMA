import bpy
import math
import bmesh

MH_OBJ = 'Game_engine' # базовый объект
ARMATURE = 'Game_engine' # арматура в котрой содержатся кости

FILES_PATH = r'C:\Users\ghost\Desktop\female\\'
PLUGIN_PATH = r'C:\Users\ghost\Desktop\mh2uma\\'


class importUMA(bpy.types.Operator):
        """Импортировать модель"""
        
        bl_idname = 'uma.import' 
        bl_label = 'import UMA model' 
        bl_options = {"REGISTER", "UNDO"} 
    
        def execute(self, context):
            
            # выделяем всё (необходимо чтобы работало удаление)
            bpy.ops.object.select_all(action='SELECT')
            
            # удаляем куб (если есть)
            if bpy.data.objects.get("Cube") is not None:
                bpy.context.view_layer.objects.active = bpy.data.objects['Cube']
                bpy.ops.object.delete(use_global=False, confirm=False)  

            # удаляем камеру (если есть)
            if bpy.data.objects.get("Camera") is not None:
                bpy.context.view_layer.objects.active = bpy.data.objects['Camera']
                bpy.ops.object.delete(use_global=False, confirm=False) 

            # удаляем свет (если есть)
            if bpy.data.objects.get("Light") is not None:
                bpy.context.view_layer.objects.active = bpy.data.objects['Light']
                bpy.ops.object.delete(use_global=False, confirm=False)         
            
            # импортируем модель
            bpy.ops.import_scene.fbx(filepath = FILES_PATH + r"female.mh.fbx")

            if bpy.data.objects.get("adult_female_genitalia_healedMesh") is not None:
                bpy.data.objects["adult_female_genitalia_healedMesh"].name = "seamsMesh"


            if bpy.data.objects.get("adult_female_genitaliaMesh") is not None:
                bpy.data.objects["adult_female_genitaliaMesh"].name = "seamsMesh"


            if bpy.data.objects.get("adult_female_genitalia_remappedMesh") is not None:
                bpy.data.objects["adult_female_genitalia_remappedMesh"].name = "seamsMesh"

            # делесект всего
            bpy.ops.object.select_all(action='DESELECT')
               
            return {"FINISHED"}

class normolizeUMA(bpy.types.Operator):
    """Нормализовать модель"""
    
    bl_idname = 'uma.normolize' 
    bl_label = 'normolize UMA model' 
    bl_options = {"REGISTER", "UNDO"} 

    def execute(self, context):
        
        bpy.context.view_layer.objects.active = bpy.data.objects[MH_OBJ]
        self.clear_pose()     
        self.rotate_back()    
        self.clear_all_transform()

        # делесект всего
        bpy.ops.object.select_all(action='DESELECT')

        return {"FINISHED"}

    # -- очищаем позу -- 
    def clear_pose(self):
        bpy.ops.object.mode_set(mode='POSE') # в режим позы
        bpy.ops.pose.select_all(action='SELECT') # выделяем все
        bpy.ops.pose.transforms_clear() # очищаем 
 
 
    # -- вращаем на 90 градусов (обратно)--
    def rotate_back(self):
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.context.view_layer.objects.active.rotation_euler.rotate_axis('X', math.radians(-90))


    # после этого шага, если удалить арматуру (в объектном режиме) меш
    # не должен стать большим и развернутым
    def clear_all_transform(self):
        for s in bpy.data.objects:
            bpy.context.view_layer.objects.active = bpy.data.objects[s.name]
            bpy.ops.object.mode_set(mode='OBJECT')
            bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
     
 

class bonesUMA(bpy.types.Operator):
    """Изменить кости"""
    
    bl_idname = 'mash.bones_uma'
    bl_label = 'normolize UMA bons' 
    bl_options = {"REGISTER", "UNDO"}


    def execute(self, context):
        bpy.context.view_layer.objects.active = bpy.data.objects[MH_OBJ]


        # todo тут может ARMATURE = Game_engine.001
        # пытаемся переименовать кость
        if 'Root' in bpy.data.armatures[ARMATURE].bones:
            bpy.data.armatures[ARMATURE].bones['Root'].name = 'Global'
            

        # выделяем и активируем объект, переходим в режим редактирования
        bpy.data.objects[MH_OBJ].select_set(state=True)
        bpy.context.view_layer.objects.active = bpy.data.objects[MH_OBJ]
        bpy.ops.object.mode_set(mode='EDIT', toggle=False)

        # меняем её расположеение
        bpy.data.armatures[ARMATURE].edit_bones['Global'].head = (0,0,0)
        bpy.data.armatures[ARMATURE].edit_bones['Global'].tail = (0,0,0.1)
            
        # делесект всего
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.select_all(action='DESELECT')

        return {"FINISHED"}   
    
    
class cutUMA(bpy.types.Operator):
    """Нарезать объект модель"""
        
    bl_idname = 'uma.cat_model'
    bl_label = 'normolize UMA bons' 
    bl_options = {"REGISTER", "UNDO"} 
    
    def execute(self, context):
        self.catBodyPart('head')
        self.catBodyPart('body')
        self.catBodyPart('legs')
        self.catBodyPart('feets')
        
        # делесект всего
        bpy.ops.object.select_all(action='DESELECT')

        return {"FINISHED"}


    def catBodyPart(self,bodyPart):

        # дублируем
        selectByName("seamsMesh")
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, 0, 0), "orient_type":'GLOBAL', "orient_matrix":((0, 0, 0), (0, 0, 0), (0, 0, 0)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False})
        bpy.context.view_layer.objects.active.name = bodyPart


        # подгатавливаем к выделению
        selectByName(bodyPart)
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='DESELECT')
        meshData = bpy.data.objects[bodyPart].data
        bm = bmesh.from_edit_mesh(meshData)

        # выделяем нужные грани
        bm.faces.ensure_lookup_table() # незнаю зачем, но без неё не работает
        meshFile = open(PLUGIN_PATH + r'bodyParts\\' + bodyPart + '.txt', "r")
        for line in meshFile:
            f = int(line)
            bm.faces[f].select = True
        meshFile.close()   

        # инвертим выделение
        bpy.ops.mesh.select_all(action='INVERT')

        # удаялем фейсы
        bpy.ops.mesh.delete(type='FACE')

        # если удалить, то останется в эдит моде и будет эксептить на неверный контекст (не знаю почему)
        bpy.ops.object.mode_set(mode='OBJECT')


    

class selectedFacesToFile(bpy.types.Operator):
    """Получить информацию о выделеных вертексах"""
    
    bl_idname = 'uma.selected_faces_to_file'
    bl_label = 'calk vertex' 
    bl_options = {"REGISTER", "UNDO"}
    

    def writeSelection(self):
        c = bpy.data.objects["seamsMesh"]
        bm = bmesh.from_edit_mesh(c.data)
        output = open(r"C:\Users\ghost\Desktop\output.txt", "a")
        for f in bm.faces:
            if (f.select):
                output.write("%s\n" % str(f.index))
        output.close() 


    
    def execute(self, context):
        self.writeSelection()
        # self.cross('b','s')

        return {"FINISHED"}


    # разница между биг и смол массивом
    def cross(self, bigPart,smallPart):
        bigArr = fileToArray(FILES_PATH + r'bodyParts\\' + bigPart + '.txt')
        smallArr = fileToArray(FILES_PATH + r'bodyParts\\' + smallPart + '.txt')
        l=[]
        for big in bigArr:
            if big not in smallArr:
                l.append(big)

        arrayToFile(r"C:\Users\ghost\Desktop\output.txt", l)
        





# добавит вкладку в меню (которое вызывется по N) в котрой будет кнопка
class UMAPanel(bpy.types.Panel):
    bl_idname = "SCENE_PT_prepare_mh_to_uma_panel"
    bl_label = "prepare MH to UMA"
    bl_space_type = "VIEW_3D" # где будет отображатся панель
    bl_region_type = "UI"
    bl_category = "UMA" # вкладка в панели
 

    def draw(self, context):
        # todo сделать чтобы можно было выбирать через селект
        self.layout.row().label(text="Кости: Game_engine")
        self.layout.row().label(text="Топология: AFG/AFGH") # todo протестировать обе топологии
        self.layout.row().operator('uma.import', text='Импортировать')
        self.layout.row().operator('uma.normolize', text='Нормализовать')
        self.layout.row().operator('mash.bones_uma', text='Кости')
        self.layout.row().operator('uma.cat_model', text='Нарезать')
        #self.layout.row().operator('uma.selected_faces_to_file', text='Сохранить выделеное')
        


def selectByName(name):
    bpy.ops.object.select_all(action='DESELECT')
    bpy.context.view_layer.objects.active = bpy.data.objects[name]
    bpy.ops.object.select_pattern(pattern=name)


def fileToArray(file):
    file = open(file, "r")
    arr = []
    for line in file:
        arr.append(int(line))
    file.close()    
    return arr        


def arrayToFile(file, array):
    output = open(file, "a")
    for f in array:
        output.write("%s\n" % str(f))
    output.close()   


bpy.utils.register_class(normolizeUMA) 
bpy.utils.register_class(bonesUMA) 
bpy.utils.register_class(cutUMA) 
bpy.utils.register_class(importUMA) 
bpy.utils.register_class(selectedFacesToFile) 

bpy.utils.register_class(UMAPanel)
