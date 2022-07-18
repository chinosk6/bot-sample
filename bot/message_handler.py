import typing as t
from . import models

func_groupmsg: t.List[t.Callable[[models.Message], t.Any]] = []
func_privatemsg: t.List[t.Callable[[models.Message], t.Any]] = []

class EventRegist:
    @staticmethod
    def reg_groupmsg(func: t.Callable[[models.Message], t.Any]):
        global func_groupmsg
        print(f"群消息处理函数注册: {func.__name__}")
        func_groupmsg.append(func)
        return func

    @staticmethod
    def reg_privatemsg(func: t.Callable[[models.Message], t.Any]):
        global func_privatemsg
        print(f"私聊消息处理函数注册: {func.__name__}")
        func_privatemsg.append(func)
        return func
