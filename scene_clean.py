from bpy import context, ops

def clean_scene():
    ctx:dict = context.copy()
    ctx['selected_objects'] = ctx['scene'].objects
    ops.object.delete(ctx)
