bl_info = {
    'name': 'Мой создователь куба',
    'author': 'ghost',
    'description':'Плагин пример',
    'location':'3D View',
    'warning':'',
    'category': 'All',
    'version': (0, 1, 2),
    'blender': (2, 81, 0)
}

import bpy
 
 
# это команда 
# её можно вызвать через F3 -> (напечатеть) create my cube (значене поля bl_label)
# наследуетмся от bpy.types.Operator
class addCube(bpy.types.Operator):
    """Создает куб""" # также это будет тултип для меню и кнопок
    
    # придумыаем уникальный "код"
    # чтобы другие могли на него ссылкать
    # можно назвать как угодно 
    # имя до точки будет в левой колонке
    # а ещё, после того как её зарегистровать можно  
    # будет вызвать её через bpy.ops.mesh.create_cube
    bl_idname = 'mash.create_cube' 
    
    # название команды (в средней колонке), так же будет названием свертка
    bl_label = 'create my cube' 
    bl_options = {"REGISTER", "UNDO"} # разрешить Ctrl+Z

    # функция которая выполнится при старте плагина
    def execute(self, context):
        bpy.ops.mesh.primitive_cube_add()
        
        return {"FINISHED"} # говорим блендеру что операция завршилась хорошо
 

# добавит вкладку в меню (которое вызывется по N) в котрой будет кнопка
class MyPanel(bpy.types.Panel):
    bl_idname = "my_create_cube_panel"
    bl_label = "create my cube"
    bl_space_type = "VIEW_3D" # где будет отображатся панель
    bl_region_type = "UI"
    bl_category = "Add Cube" # вкладка в панели
 
    def draw(self, context):
        row = self.layout.row()
        row.operator('mash.create_cube', text='add cube') # название кнопки

 
 
def register():
    # нужно чтобы ещё была зарегестриованна команда (до создания панели)
    bpy.utils.register_class(addCube) 
    bpy.utils.register_class(MyPanel)
 
def unregister():
    bpy.utils.unregister_class(addCube)
    bpy.utils.unregister_class(MyPanel)
    
    
    
# стандартная практика питона, чтобы этот код не испольнялся 
# если этот файл использовать как модуль, но исполнялся 
# если этот файл использовать как главный
if __name__ == "__main__":
    register()