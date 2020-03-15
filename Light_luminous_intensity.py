# -*- coding:utf-8 -*-

# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110- 1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8 compliant>

# ----------------------------------------------------------
# Author: Stephen Leger (s-leger)
#
# ----------------------------------------------------------

bl_info = {
    'name': 'Light intensity',
    'description': 'Add luminous intensity setting to lights',
    'author': 's-leger support@blender-archipack.org',
    'license': 'GPL',
    'deps': '',
    'blender': (2, 80, 0),
    'version': (0, 0, 1),
    'location': 'Properties > Data > Light',
    'warning': '',
    'wiki_url': '',
    'tracker_url': '',
    'link': 'https://github.com/s-leger/blender-light_luminous_intensity',
    'support': 'COMMUNITY',
    'category': 'Lighting'
}

from math import pi
from bpy.utils import register_class, unregister_class
from bpy.types import Light, Panel
from bpy.props import (
    FloatProperty
)

# https://en.wikipedia.org/wiki/Luminous_efficacy#Lighting_efficiency

def get_lumen(self):
    return self.energy * 683


def set_lumen(self, lumen):
    self.energy = lumen / 683
    return None


def get_candela(self):
    return self.energy * 683 / (4 * pi)


def set_candela(self, candela):
    self.energy = candela * 4 * pi / 683
    return None


class LIGHT_PT_luminous_intensity(Panel):
    bl_idname = "LIGHT_PT_luminous_intensity"
    bl_label = "Luminous intensity"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "data"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return context.light and not context.light.cycles.is_portal

    def draw(self, context):
        light = context.light
        layout = self.layout
        layout.use_property_decorate = False
        layout.prop(light, "lumen")
        layout.prop(light, "candela")


def register():
    register_class(LIGHT_PT_luminous_intensity)
    Light.candela = FloatProperty(
        name="Candela",
        get=get_candela,
        set=set_candela
    )
    Light.lumen = FloatProperty(
        name="Lumen",
        get=get_lumen,
        set=set_lumen
    )


def unregister():
    unregister_class(LIGHT_PT_luminous_intensity)
    del Light.candela
    del Light.lumen


if __name__ == 'main':
    register()
