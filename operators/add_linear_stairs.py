import bpy
import bmesh
from bpy.types import Operator
from bpy.props import (
    IntProperty,
    FloatProperty,
    FloatVectorProperty,
    EnumProperty
)
from bpy_extras import object_utils
from bpy_extras.object_utils import AddObjectHelper

from ..utils import linear_stairs


class AddLinearStairs(Operator):
    """Add a linear stairs mesh"""

    bl_idname = "mesh.primitive_linear_stairs_add"
    bl_label = "Add Linear Stairs"
    bl_options = {'REGISTER', 'UNDO'}

    count: IntProperty(
        name="Stair Count",
        description="Number of stairs",
        default=5, min=1
    )
    width: FloatProperty(
        name="Stair Width",
        description="Stair width",
        min=0.2,
        soft_max=20.0,
        default=2.0,
    )
    depth: FloatProperty(
        name="Stair Depth",
        description="Stair depth",
        min=0.05,
        default=0.3,
    )
    height: FloatProperty(
        name="Stair Height",
        description="Stair height",
        min=0.05,
        default=0.15,
    )

    # Transform properties
    align_items = (
        ('WORLD', "World", "Align the new object to the world"),
        ('VIEW', "View", "Align the new object to the view"),
        ('CURSOR', "3D Cursor", "Align the new object to the 3D cursor")
    )
    align: EnumProperty(
        name="Align",
        items=align_items,
        default='WORLD',
        update=AddObjectHelper.align_update_callback
    )
    location: FloatVectorProperty(
        name="Location",
        subtype='TRANSLATION',
    )
    rotation: FloatVectorProperty(
        name="Rotation",
        subtype='EULER',
    )

    def execute(self, context):
        # create mesh data
        vertices, faces, uvs = linear_stairs.create(
            self.count,
            self.width,
            self.depth,
            self.height
        )

        mesh = bpy.data.meshes.new("Stairs")

        bm = bmesh.new()

        for vert in vertices:
            bm.verts.new(vert)

        bm.verts.ensure_lookup_table()
        for face in faces:
            bm.faces.new([bm.verts[i] for i in face])
        
        uv_layer = bm.loops.layers.uv.new()
        loop = bm.loops.layers.uv[0]
        for face, face_uvs in zip(bm.faces, uvs):
            for loop, uv in zip(face.loops, face_uvs):
                loop[uv_layer].uv = uv

        bm.to_mesh(mesh)
        bm.free()
        mesh.update()

        object_utils.object_data_add(context, mesh, operator=self)

        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator(AddLinearStairs.bl_idname, icon='FORWARD')


def register():
    bpy.utils.register_class(AddLinearStairs)
    bpy.types.VIEW3D_MT_mesh_add.append(menu_func)


def unregister():
    bpy.utils.unregister_class(AddLinearStairs)
    bpy.types.VIEW3D_MT_mesh_add.remove(menu_func)


if __name__ == "__main__":
    register()
