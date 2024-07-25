bl_info = {
    "name": "BlenderST3D",
    "author": "TASK Studio",
    "version": (0, 1),
    "blender": (2, 80, 0),  # Ensure this matches your Blender version
    "description": "Enables speech recognition for Blender",
    "category": "3D View",
}

# if "bpy" in locals():
#     import imp
#     imp.reload(mycube)
#     imp.reload(mysphere)
#     imp.reload(mycylinder)
#     print("Reloaded multifiles")
# else:
#     print("Imported multifiles")

# classes = (
#     OBJECT_OT_add_object,
#     # Add other classes here as needed
# )


def register():
    pass


def unregister():
    pass


if __name__ == "__main__":
    register()
