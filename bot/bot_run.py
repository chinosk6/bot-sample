import websocket
from threading import Thread
import base_settings
import json
import bot


def on_message(ws, message):
    # print(f"message: {message}")
    bot.message_processor.msg_in(json.loads(message))


def on_error(ws, error):
    print(error)


def on_close(ws, *args):
    print("websocket连接失败", args)


def on_open(ws):
    def run(*args):
        print("websocket连接成功, 开始运行")

    Thread(target=run).start()

def start():
    websocket.enableTrace(False)
    host = f"ws://{base_settings.CQhttp.ip}:{base_settings.CQhttp.cq_ws_port}"
    ws = websocket.WebSocketApp(host,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()


if __name__ == "__main__":
    start()
