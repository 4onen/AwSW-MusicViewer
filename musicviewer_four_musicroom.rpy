init:
    python in musicviewer_four:
        from musicviewer_four_ref_table import music_ref_table

        mr = renpy.store.MusicRoom(fadeout=1.0)

        for track in music_ref_table.keys():
            mr.add(track)


    screen musicviewer_four_musicroom tag gallery_page:
        text "Music Room":
            xalign 0.5
            yalign 0.5

        on "show" action Stop("music", fadeout=0.5)
        on "hide" action Play("music", "mx/menu.ogg")