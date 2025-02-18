from sanic import Sanic

from listener.base import BaseListener
from listener.client import ClientListener

LISTENER_TUPLE: tuple[type[BaseListener], ...] = (
    ClientListener,
)


def register_listener(app: Sanic) -> None:
    """注册监听"""
    for listener_cls in LISTENER_TUPLE:
        listener: BaseListener = listener_cls(app=app)
        for event in ('before_server_start', 'after_server_start', 'before_server_stop', 'after_server_stop'):
            if hasattr(listener, event):
                app.register_listener(getattr(listener, event), event)
    return None
