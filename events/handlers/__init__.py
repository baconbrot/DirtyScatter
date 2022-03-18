from importlib import import_module
from pkgutil import iter_modules

import events


def init():
    package_infos = iter_modules(events.handlers.__path__, prefix='events.handlers.')
    for info in package_infos:
        if info.ispkg: continue
        import_module(info.name)