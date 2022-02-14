
from renpy import ast, python, store

from modloader import modinfo, modast
from modloader.modclass import Mod, loadable_mod

import jz_magmalink as ml

@loadable_mod
class MyAwSWMod(Mod):
    name = "Music Viewer"
    version = "v0.0"
    author = "4onen"
    dependencies = ["MagmaLink"]

    def mod_load(self):
        ml.register_mod_settings(self, screen='musicviewer_four_modsettings')

    @staticmethod
    def mod_complete():
        pass
