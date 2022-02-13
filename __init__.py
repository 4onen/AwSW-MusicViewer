
from renpy import ast, python, store

from modloader import modinfo, modast
from modloader.modclass import Mod, loadable_mod

@loadable_mod
class MyAwSWMod(Mod):
    name = "Music Viewer"
    version = "v0.0"
    author = "4onen"
    dependencies = ["MagmaLink"]

    @classmethod
    def mod_load(cls):
        ml = modinfo.get_mods()["MagmaLink"].import_ml()
        ml.register_mod_settings(cls, screen='musicviewer_four_modsettings')
        # ( ml.find_label('splashscreen')
        #     .search_python("renpy.pause(1.6, hard=True)")
        #     .hook_to("musicviewer_four_show_nowplaying")
        # )

        ( ml.find_label('seccont')
            .hook_to("musicviewer_four_show_nowplaying")
        )

    @staticmethod
    def mod_complete():
        pass
