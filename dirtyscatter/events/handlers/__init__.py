from importlib import import_module
from pkgutil import iter_modules

import dirtyscatter


def init():
    package_infos = iter_modules(dirtyscatter.events.handlers.__path__, prefix='dirtyscatter.events.handlers.')
    for info in package_infos:
        if info.ispkg: continue
        import_module(info.name)