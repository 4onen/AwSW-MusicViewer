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
                use musicviewer_four_checkbox("Disable \"Now Playing\"", "musicviewer_four_nowplaying_off")
                if not persistent.musicviewer_four_nowplaying_off:
                    use musicviewer_four_checkbox("Show \"Now Playing\" at all times", "musicviewer_four_nowplaying_alwayson")
                    use musicviewer_four_checkbox("Show filenames in \"Now Playing\"", "musicviewer_four_nowplaying_show_filenames")
            imagebutton idle "image/ui/close_idle.png" hover "image/ui/close_hover.png" action [Show("_ml_mod_settings"), Play("audio", "se/sounds/close.ogg")] hovered Play("audio", "se/sounds/select.ogg") style "smallwindowclose" at nav_button




    python in musicviewer_four:
        from musicviewer_four_ref_table import music_ref_table

        def get_nowplaying_info():
            nowplaying = renpy.music.get_playing()
            if not nowplaying:
                return (None, {})
            else:
                return (nowplaying, music_ref_table.get(nowplaying, {}))

        def manager_callback(prev_nowplaying):
            if not renpy.store.persistent.musicviewer_four_nowplaying_off:
                nowplaying, meta = get_nowplaying_info()
                if (nowplaying and (nowplaying != prev_nowplaying)) or renpy.store.persistent.musicviewer_four_nowplaying_alwayson:
                    renpy.show_screen("musicviewer_four_nowplaying",nowplaying, meta)
                return nowplaying
            elif renpy.get_screen("musicviewer_four_nowplaying"):
                renpy.hide_screen("musicviewer_four_nowplaying")
                return None

        class NowPlayingManager():
            def __init__(self):
                self.prev_nowplaying = None

            def __call__(self):
                self.prev_nowplaying = manager_callback(self.prev_nowplaying)

        if isinstance(renpy.store.config.start_interact_callbacks,list):
            renpy.store.config.start_interact_callbacks.append(NowPlayingManager())
        else:
            renpy.store.config.start_interact_callbacks = [NowPlayingManager()]

    # Now playing
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

    screen musicviewer_four_nowplaying(nowplaying, meta):
        frame:
            at musicviewer_four_nowplaying_tf
            background Frame("image/ui/musicviewer_four_nowplaying_bg.png", 68, 10, 10, 68)
            padding (45, 0, 5, 50)
            
            has vbox
            if nowplaying is None:
                text "- None -"
            else: # Is metadata dict
                if 'title' in meta:
                    if meta['title'] == nowplaying:
                        text nowplaying
                    else:
                        text meta['title']
                        if renpy.store.persistent.musicviewer_four_nowplaying_show_filenames:
                            text nowplaying:
                                size 26
                else:
                    text nowplaying
                if 'artist' in meta:
                    text meta['artist']:
                        xanchor 1.0
                        xalign 1.0
                        size 26
                        color "#ddd"
                if 'album' in meta:
                    text meta['album']:
                        xanchor 1.0
                        xalign 1.0
                        size 24
                        color "#ddd"

        if not persistent.musicviewer_four_nowplaying_alwayson:
            timer 6.0 action Hide("musicviewer_four_nowplaying")