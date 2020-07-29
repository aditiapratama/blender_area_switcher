# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#   https://github.com/Korchy/blender_area_switcher

from bpy.types import Operator
from bpy.utils import register_class, unregister_class


class AREA_SWITCHER_OT_main(Operator):
    bl_idname = 'area_switcher.switch_area'
    bl_label = 'Switch Area'
    bl_description = 'Switch area type to next'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        fr = [e for e in context.preferences.addons[__package__].preferences.items if e[0] == context.area.ui_type][0][5]
        print(fr)
        vl = getattr(context.preferences.addons[__package__].preferences, fr)
        print(vl)
        # print(context.area.ui_type)

        context.area.ui_type = vl

        return {'FINISHED'}


def register():
    register_class(AREA_SWITCHER_OT_main)


def unregister():
    unregister_class(AREA_SWITCHER_OT_main)
