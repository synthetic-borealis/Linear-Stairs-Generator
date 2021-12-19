bl_info = {
    "name" : "Linear Stairs Generator",
    "author" : "Elhanan Flesch",
    "description" : "Generates linear stairs",
    "blender" : (3, 0, 0),
    "version" : (0, 0, 3),
    "location" : "View3D > Add > Mesh",
    "warning" : "",
    "category" : "Add Mesh"
}

import bpy

from .operators import add_linear_stairs

def register():
    add_linear_stairs.register()


def unregister():
    add_linear_stairs.unregister()
