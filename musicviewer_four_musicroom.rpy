init:
    python in musicviewer_four:
        from musicviewer_four_metalookup import metalookup, is_supported

        mr = None
        tracks = []

        def setup():
            global mr
            global tracks

            tracklist = sorted([f if f.startswith('mx/') else f[f.find('/mx/')+1:] for f in renpy.list_files() if (f.startswith("mx/") or '/mx/' in f) and is_supported(f)])
            seen_tracks = set()
            tracks = []

            for track in tracklist:
                if track in seen_tracks:
                    continue
                seen_tracks.add(track)
                tracks.append(track)


            mr = renpy.store.MusicRoom(fadeout=0.5, fadein=0.5)

            for track in tracks:
                mr.add(track, always_unlocked = renpy.store.persistent.musicviewer_four_musicviewer_unlockall)

    style musicviewer_four_musicroom_select_btn:
        background "#3333339B"
        hover_background "#ffffff9B"
        insensitive_background "#0000009B"
        selected_background "#ffffaa9B"
        xfill True
        xminimum 50
        yminimum 50

    style musicviewer_four_musicroom_select_btn_text:
        color "#ffffff"
        insensitive_color "#cccccc"

    screen musicviewer_four_musicroom():
        tag gallery_page
        on "show" action Stop("music", fadeout=0.5)
        on "hide" action Play("music", "mx/menu.ogg")

        hbox:
            area (130, 135, 1790, 900)
            spacing 80

            side "c l":
                xysize (830, 855)
                vpgrid id "musicselect_vp":
                    cols 1
                    spacing 5
                    draggable True
                    mousewheel True

                    for filename in musicviewer_four.tracks:
                        $ songlabel = "[filename]" if musicviewer_four.mr.is_unlocked(filename) else "{s}[filename]{/s}" 
                        textbutton songlabel:
                            style "musicviewer_four_musicroom_select_btn"
                            xfill True
                            text_style "musicviewer_four_musicroom_select_btn_text"

                            action [Play("audio","se/sounds/select.ogg"),
                                    musicviewer_four.mr.Play(filename=filename)]

                bar value YScrollValue("musicselect_vp"):
                    style "modmenu_select_slider"

            frame:
                xysize (830, 855)
                background "#0000009B"

                has vbox

                python:
                    nowplaying = renpy.music.get_playing()
                    meta = musicviewer_four.metalookup(nowplaying)

                if not nowplaying:
                    text "{b}Select a song{/b}":
                        text_align 0.5
                else:
                    text "{b}Now Playing:{/b}":
                        text_align 0.5
                # Metadata box
                frame:
                    background "#ffffff9B"
                    ysize 400
                    xfill True
                    xalign 0.5

                    has vbox

                    if not nowplaying:
                        null
                    elif meta:
                        text "[nowplaying]":
                            size 26
                            color "#ddd"
                            xfill True
                            text_align 0.5
                        if 'title' in meta:
                            text meta['title']:
                                xfill True
                                text_align 0.5
                        else:
                            text nowplaying:
                                xfill True
                                text_align 0.5
                        if 'artist' in meta:
                            text meta['artist']:
                                xfill True
                                text_align 0.5
                        if 'album' in meta:
                            text meta['album']:
                                xfill True
                                text_align 0.5
                    else:
                        text "[nowplaying]":
                            xfill True
                            text_align 0.5
                        text "Metadata not found":
                            size 26
                            color "#ddd"
                            xfill True
                            text_align 0.5

                # Controls box
                hbox:
                    xalign 0.5
                    spacing 10
                    # Prev button
                    imagebutton:
                        idle renpy.display.im.Flip("image/ui/buttons/quick_skip_idle.png",horizontal=True)
                        hover renpy.display.im.Flip("image/ui/buttons/quick_skip_hover2.png",horizontal=True)
                        selected_idle renpy.display.im.Flip("image/ui/buttons/quick_skip_hover2.png",horizontal=True)
                        action [Play("audio","se/sounds/select.ogg"), musicviewer_four.mr.Previous()]
                        style "musicviewer_four_musicroom_select_btn"
                        # xpadding 84
                        xfill False
                    # Stop Button
                    textbutton "Stop" action [Play("audio","se/sounds/select.ogg"), musicviewer_four.mr.Stop()]:
                        style "musicviewer_four_musicroom_select_btn"
                        xsize 200
                        text_style "musicviewer_four_musicroom_select_btn_text"
                    # Random Button
                    textbutton "Random" action [Play("audio","se/sounds/select.ogg"), musicviewer_four.mr.RandomPlay()]:
                        style "musicviewer_four_musicroom_select_btn"
                        xsize 200
                        text_style "musicviewer_four_musicroom_select_btn_text"
                    # Next button
                    imagebutton:
                        idle "image/ui/buttons/quick_skip_idle.png"
                        hover "image/ui/buttons/quick_skip_hover2.png"
                        selected_idle "image/ui/buttons/quick_skip_hover2.png"
                        action [Play("audio","se/sounds/select.ogg"), musicviewer_four.mr.Next()]
                        style "musicviewer_four_musicroom_select_btn"
                        # xpadding 84
                        xfill False

                # Shuffle/Loop box
                vbox:
                    yalign 1.0
                    textbutton "Shuffle" action [Play("audio","se/sounds/select.ogg"), musicviewer_four.mr.ToggleShuffle()]:
                        style "musicviewer_four_musicroom_select_btn"
                        text_style "musicviewer_four_musicroom_select_btn_text"
                    textbutton "Single Track" action [Play("audio","se/sounds/select.ogg"), musicviewer_four.mr.ToggleSingleTrack()]:
                        style "musicviewer_four_musicroom_select_btn"
                        text_style "musicviewer_four_musicroom_select_btn_text"
