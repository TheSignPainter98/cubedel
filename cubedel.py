from bpy import context, ops

def cubedel():
    ctx:dict = context.copy()
    ctx['selected_objects'] = [ctx['scene'].objects['Cube']]
    ops.object.delete(ctx)
