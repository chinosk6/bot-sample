from . import models
from . import message_handler
from threading import Thread


def on_new_thread(func):
    def _(*args, **kwargs):
        t = Thread(target=func, args=args, kwargs=kwargs)
        t.start()
        return t
    return _


@on_new_thread
def msg_in(msgchain: dict):
    if "message_type" in msgchain:
        msgtype = msgchain["message_type"]

        if msgtype == "group":  # 收到群消息
            sub_type = msgchain["sub_type"]
            if sub_type == "normal":  # 普通群消息
                for func in message_handler.func_groupmsg:
                    func(models.Message(**msgchain))

        elif msgtype == "private":  # 收到私聊
            sub_type = msgchain["sub_type"]
            if sub_type == "friend":  # 收到好友消息
                for func in message_handler.func_privatemsg:
                    func(models.Message(**msgchain))
