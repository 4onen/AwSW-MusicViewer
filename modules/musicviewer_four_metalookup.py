from tinytag import TinyTag
import renpy
import os.path

_EXTRACT_FIELDS = ['title','artist','album']

def _extract_meta(file):
    refs = TinyTag.get((file), duration=False, ignore_errors=True)
    meta = {field:getattr(refs,field) for field in _EXTRACT_FIELDS if hasattr(refs,field) and getattr(refs,field)}

    if not meta:
        return {}

    t = meta.get('title')
    if t:
        if t == os.path.basename(file):
            meta['title'] = file
    else:
        meta['title'] = file
    return meta

_meta_cache = {}

def metalookup(file):
    if not file:
        return {}
    elif file in _meta_cache:
        return _meta_cache[file]
    else:
        meta = _extract_meta(file)
        _meta_cache[file] = meta
        return meta

def is_supported(file):
    try:
        file = renpy.loader.transfn(file)
    except:
        pass
    return TinyTag.is_supported(file)
