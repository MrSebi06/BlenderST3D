import bpy


def extrude_function():
    for area in bpy.context.screen.areas:
        if area.type == "VIEW_3D":
            with bpy.context.temp_override(area=area):
                bpy.ops.object.mode_set(mode="EDIT")
                bpy.ops.wm.tool_set_by_id(name="builtin.extrude_region")
