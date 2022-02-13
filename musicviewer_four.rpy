init:
    # Settings menu
    screen musicviewer_four_checkbox(label, id):
        hbox:
            spacing 10
            imagebutton:
                xcenter 0.5
                ycenter 0.5
                idle im.Scale("ui/nsfw_chbox-unchecked.png", 70, 70)
                hover im.Recolor(im.Scale("ui/nsfw_chbox-unchecked.png", 70, 70), 64, 64, 64)
                selected_idle im.Scale("ui/nsfw_chbox-checked.png", 70, 70)
                selected_hover im.Recolor(im.Scale("ui/nsfw_chbox-checked.png", 70, 70), 64, 64, 64)
                action [MTSTogglePersistentBool(id),
                        Play("audio", "se/sounds/yes.wav")]
                hovered Play("audio", "se/sounds/select.ogg")
                focus_mask None
            text label

    screen musicviewer_four_modsettings tag smallscreen2:
        modal True
        window id "musicviewer_four_modsettings" at popup2:
            style "smallwindow"
            vbox:
                align(0.5,0.5)
                spacing 10
                #text "Music Viewer"
                #use musicviewer_four_checkbox("Disable main menu \"Music\" button", "musicviewer_four_musicviewer_off")
                text "Now Playing"
                use musicviewer_four_checkbox("Disable in-game \"Now Playing\"", "musicviewer_four_nowplaying_off")
                if not persistent.musicviewer_four_nowplaying_off:
                    use musicviewer_four_checkbox("Show \"Now Playing\" at all times", "musicviewer_four_nowplaying_alwayson")
                    use musicviewer_four_checkbox("Show filenames instead of metadata in \"Now Playing\"", "musicviewer_four_nowplaying_show_filenames")
            imagebutton idle "image/ui/close_idle.png" hover "image/ui/close_hover.png" action [Show("_ml_mod_settings"), Play("audio", "se/sounds/close.ogg")] hovered Play("audio", "se/sounds/select.ogg") style "smallwindowclose" at nav_button




    python in musicviewer_four:
        from musicviewer_four_ref_table import music_ref_table

        def show_nowplaying_manager():
            renpy.show_screen("musicviewer_four_nowplaying_manager")
            print("After load callback executed.")

        if isinstance(renpy.config.after_load_callbacks, list):
            renpy.config.after_load_callbacks.append(show_nowplaying_manager)
        else:
            renpy.config.after_load_callbacks = [show_nowplaying_manager]

        prev_nowplaying = None

        def get_nowplaying_info():
            nowplaying = renpy.music.get_playing()
            if not nowplaying:
                return "- None -"
            if renpy.store.persistent.musicviewer_four_nowplaying_show_filenames:
                return nowplaying
            else:
                return music_ref_table.get(nowplaying, nowplaying)
        
        def manager_callback(prev_nowplaying):
            if not renpy.store.persistent.musicviewer_four_nowplaying_off:
                nowplaying = get_nowplaying_info()
                if (nowplaying and (nowplaying != prev_nowplaying)):# or renpy.store.persistent.musicviewer_four_nowplaying_alwayson:
                    renpy.show_screen("musicviewer_four_nowplaying",nowplaying)
                return nowplaying
            elif renpy.get_screen("musicviewer_four_nowplaying"):
                renpy.hide_screen("musicviewer_four_nowplaying")
                return None

    # Now playing
    screen musicviewer_four_nowplaying_manager:
        default prev_nowplaying = None
        python:
            prev_nowplaying = musicviewer_four.manager_callback(prev_nowplaying)

    transform musicviewer_four_nowplaying_tf:
        anchor (1.0, 0.0)
        align (1.0, 0.0)
        
        alpha 0.0 zoom 0.8

        on show:
            ease 1.2 alpha 0.8 zoom 1.0
        on hide:
            ease 0.8 alpha 0.0 zoom 1.1
        on replace:
            ease 1.0 alpha 0.8 zoom 1.0
        on replaced:
            ease 0.8 alpha 0.0 zoom 1.1
            zoom 0.8

    screen musicviewer_four_nowplaying(nowplaying):
        frame:
            at musicviewer_four_nowplaying_tf
            background Frame("image/ui/musicviewer_four_nowplaying_bg.png", 68, 10, 10, 68)
            padding (45, 0, 5, 50)
            
            has vbox
            if isinstance(nowplaying, (str,unicode)):
                text nowplaying
            else: # Is metadata dict
                text nowplaying['title']

                if 'artist' in nowplaying:
                    text nowplaying['artist']:
                        xanchor 1.0
                        xalign 1.0
                        size 26
                        color "#ddd"
                if 'album' in nowplaying:
                    text nowplaying['album']:
                        xanchor 1.0
                        xalign 1.0
                        size 24
                        color "#ddd"

        if not persistent.musicviewer_four_nowplaying_alwayson:
            timer 6.0 action Hide("musicviewer_four_nowplaying")


label musicviewer_four_show_nowplaying:
    $ musicviewer_four.show_nowplaying_manager()
    jump musicviewer_four_show_nowplaying_return