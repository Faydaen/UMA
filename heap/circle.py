import bpy
import math
from bpy.props import IntProperty, FloatProperty, StringProperty

class UMA_OP_cube_circle(bpy.types.Operator):
    """My Object Moving Script"""
    bl_idname = "uma.cubes_circle"
    bl_label = "Cubes circle"
    bl_options = {'REGISTER', 'UNDO'}


    radius: FloatProperty(name="radius", default=3, min=1, max=8)
    count: IntProperty(name="count",default=5,min=4, max=360)
    
    def draw(self, context):
        layout = self.layout
        layout.prop(self,'radius')
        layout.prop(self,'count')

    def execute(self, context):
        for i in range(self.count):
            angle = i * math.pi * 2 / self.count
            x = math.cos(angle) * self.radius
            y = math.sin(angle) * self.radius
            z = 0
            size = 1
            bpy.ops.mesh.primitive_cube_add(location=(x,y,z),size=size)
        return {'FINISHED'}

def register():    
    bpy.utils.register_class(UMA_OP_cube_circle)
