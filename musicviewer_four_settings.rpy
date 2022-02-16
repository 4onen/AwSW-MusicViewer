init:
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
                text "Music Viewer"
                use musicviewer_four_checkbox("Disable main menu \"Music\" button", "musicviewer_four_musicviewer_off")
                if not persistent.musicviewer_four_musicviewer_off:
                    use musicviewer_four_checkbox("Make all songs available (Can't be undone!)", "musicviewer_four_musicviewer_unlockall")
                text "Now Playing"
                use musicviewer_four_checkbox("Disable \"Now Playing\"", "musicviewer_four_nowplaying_off")
                if not persistent.musicviewer_four_nowplaying_off:
                    use musicviewer_four_checkbox("Show \"Now Playing\" at all times", "musicviewer_four_nowplaying_alwayson")
                    use musicviewer_four_checkbox("Show filenames in \"Now Playing\"", "musicviewer_four_nowplaying_show_filenames")
            imagebutton idle "image/ui/close_idle.png" hover "image/ui/close_hover.png" action [Show("_ml_mod_settings"), Play("audio", "se/sounds/close.ogg")] hovered Play("audio", "se/sounds/select.ogg") style "smallwindowclose" at nav_button

