from dirtyscatter.events import handlers
from dirtyscatter.events.eventType import EventType


_listeners = {}


async def trigger(event_type: EventType, *args):
    try:
        for task in _listeners.get(event_type.value):
            await task(*args)
    except:
        print(f'No handler for {event_type}')


def register(event_type: EventType):
    def decorator(func):
        try:
            tasks = _listeners[event_type.value]
        except:
            tasks = []
        tasks.append(func)
        _listeners[event_type.value] = tasks
        return func
    return decorator


handlers.init()
