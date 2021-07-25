import bpy


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

# выделить арматуру
def getArmature():
    if (bpy.context.object.type == "ARMATURE"):
        pass
    else:
        pass

        
# выделить и активировать одну кость (с остальных снять выделение)
def selectOneBone(boneName = 'head'):
    for bone in bpy.context.object.data.edit_bones:
        bone.select = False
    bpy.context.object.data.edit_bones[boneName].select = True
    bpy.data.armatures[0].edit_bones.active  = bpy.context.object.data.edit_bones[boneName]


# получить список имён выделенных костей
#def getSelectedBonesNames(exclude=None):
def getSelectedBonesNames():
    selected = []
    for bone in bpy.context.object.data.edit_bones:
        #if exclude is not None and exclude == bone.name:
        #    continue

        if (bone.select):
            selected.append(bone.name)
    return selected        


def assaciateSelectedWetixWith(vertexGroupName):
    pass


# выделить вертексы указанных групп вертексов
def selectVetetex(names = [], objectName = 'Genesis3Female.Shape'):
    # снимаем выделение со всех вертексов
    bpy.ops.mesh.select_all(action='DESELECT')
    vg = bpy.data.objects[objectName].vertex_groups
    vgNames = [v.name for v in vg]
    for name in names:
        if name in vgNames:
            vg.active_index = vg[name].index
            bpy.ops.object.vertex_group_select()

