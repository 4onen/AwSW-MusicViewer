init:
    python in musicviewer_four:
        from musicviewer_four_metalookup import metalookup

        class NowPlayingManager():
            def __init__(self):
                self.prev_nowplaying = None

            def __call__(self):
                if not renpy.store.persistent.musicviewer_four_nowplaying_off:
                    nowplaying = renpy.music.get_playing()
                    if (nowplaying and (nowplaying != self.prev_nowplaying)) or (renpy.store.persistent.musicviewer_four_nowplaying_alwayson and not renpy.get_screen("musicviewer_four_nowplaying")):
                        renpy.show_screen("musicviewer_four_nowplaying",nowplaying, metalookup(nowplaying))
                    self.prev_nowplaying = nowplaying
                elif renpy.get_screen("musicviewer_four_nowplaying"):
                    renpy.hide_screen("musicviewer_four_nowplaying")
                    self.prev_nowplaying = None

        renpy.store.config.start_interact_callbacks.append(NowPlayingManager())

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
            background Frame(renpy.display.im.FactorScale("image/ui/musicviewer_four_nowplaying_bg.png",2), 136, 20, 20, 136, tile=True)
            padding (140, 0, 0, 130)

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