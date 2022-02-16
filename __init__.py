
from renpy import ast, python, store

from modloader import modinfo, modast
from modloader.modclass import Mod, loadable_mod

import jz_magmalink as ml

@loadable_mod
class MyAwSWMod(Mod):
    name = "Music Viewer"
    version = "v0.8"
    author = "4onen"
    dependencies = ["MagmaLink"]

    def mod_load(self):
        ml.register_mod_settings(self, screen='musicviewer_four_modsettings')

        ( ml.Overlay()
            .add(['imagebutton auto "image/ui/musicviewer_four_musicbutton_%s.png":'\
                 ,'    xalign 0.655'\
                 ,'    yalign 0.965'\
                 ,'    action [Show("gallery", transition=dissolve), musicviewer_four.prepare_musicroom, Show("musicviewer_four_musicroom"), Play("audio", "se/sounds/open.ogg")]'\
                 ,'    hovered Play("audio", "se/sounds/select.ogg")'\
                ], condition="not persistent.musicviewer_four_musicviewer_off")
            .compile_to("main_menu")
        )

    @staticmethod
    def mod_complete():
        pass
