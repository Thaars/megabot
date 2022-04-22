"""
    Reconnect / Refresh Access Token: https://community.tradovate.com/t/sequence-numbers/4102/4
    Contract Month Codes: https://www.cmegroup.com/month-codes.html
    Automated Orders: https://api.tradovate.com/#section/Automated-Orders
"""
import asyncio
import json
import sys
from threading import Thread

import websocket
import _thread
import time
import rel

# API
import definitions
from api_key import *

from tradovate.tradovate_api_client import Client as TradovateClient
from tradovate.tradovate_api_client import AuthenticatedClient
from tradovate.tradovate_api_client.api.accounting import account_list
from tradovate.tradovate_api_client.api.authentication import access_token_request
from tradovate.tradovate_api_client.api.users import user_list, sync_request
from tradovate.tradovate_api_client.models import AccessTokenRequest

rel.safe_read()

_ws = None
_request_id = 0
_access_token = None


def tradovate_auth():
    global _access_token
    tradovate_client = TradovateClient(base_url=definitions.TRADOVATE_URL)

    access_token_response = access_token_request.sync(
        client=tradovate_client,
        json_body=AccessTokenRequest(
            name=TRADOVATE_NAME,
            password=TRADOVATE_API_PW,
            app_id=TRADOVATE_APP_ID,
            app_version=definitions.APP_VERSION,
            device_id=TRADOVATE_API_DEVICE_ID,
            cid=TRADOVATE_API_CID,
            sec=TRADOVATE_API_SECRET
        )
    )
    _access_token = access_token_response.access_token
    authenticated_client = AuthenticatedClient(
        base_url=definitions.TRADOVATE_URL,
        token=_access_token
    )

    # account_list_response = account_list.sync(client=authenticated_client)
    #
    # user_list_response = user_list.sync(client=authenticated_client)
    #
    # await open_ws(_access_token)


""" neuer Versuch """


def on_message(ws, message):
    print(message)


def on_error(ws, error):
    print(error)


def on_close(ws, close_status_code, close_msg):
    print("### closed ###")


def send(ws, endpoint, query=None, body=None):
    global _request_id
    _request_id += 1
    print(f"{endpoint}, {_request_id}, {query}, {body}")
    ws.send(f"{endpoint}\n{_request_id}\n{query}\n{body}")


def on_open(ws):
    print('### on_open ###')
    send(ws=ws, endpoint="authorize", body=_access_token)


def chart(*args):
    time.sleep(5)
    # send the message, then wait
    # so thread doesn't exit and socket
    # isn't closed
    print('### chart ###')
    body = {
        "symbol": definitions.TRADOVATE_SYMBOL,
        "chartDescription": {
            "underlyingType": "MinuteBar",
            "elementSize": 1,
            "elementSizeUnit": "UnderlyingUnits",
            "withHistogram": False,
        },
        "timeRange": {
            "asMuchAsElements": 20
        }
    }
    send(ws=_ws, endpoint="md/getChart", body=json.dumps(body))


if __name__ == "__main__":
    tradovate_auth()
    websocket.enableTrace(True)
    _ws = websocket.WebSocketApp(definitions.TRADOVATE_WEBSOCKET_URL,
                                 on_message=on_message,
                                 on_error=on_error,
                                 on_close=on_close,
                                 on_open=on_open)
    Thread(target=chart).start()
    # _ws.on_open = on_open
    _ws.run_forever()


""" neuer Versuch """


# # Define WebSocket callback functions
# def ws_message(_ws, message):
#     print("WebSocket thread: %s" % message)
#
#
# def ws_open(_ws):
#     global _access_token
#     _ws.send(endpoint="authorize", body=_access_token)
#     print('### ws_open ###')
#     time.sleep(2.5)
#     print('### ws_open 2 ###')
#     body = {
#         "symbol": definitions.TRADOVATE_SYMBOL,
#         "chartDescription": {
#             "underlyingType": "MinuteBar",
#             "elementSize": 1,
#             "elementSizeUnit": "UnderlyingUnits",
#             "withHistogram": False,
#         },
#         "timeRange": {
#             "asMuchAsElements": 20
#         }
#     }
#     print(f"md/getChart\n{_request_id}\n\n{json.dumps(body)}")
#     _ws.send(endpoint="md/getChart", body=json.dumps(body))
#
#
# def ws_thread(*args):
#     _ws = websocket.WebSocketApp(
#         definitions.TRADOVATE_WEBSOCKET_URL,
#         on_open=ws_open,
#         on_message=ws_message
#     )
#     _ws.run_forever()
#
#
# tradovate_auth()
# # Start a new thread for the WebSocket interface
# _thread.start_new_thread(ws_thread, ())
#
# # Continue other (non WebSocket) tasks in the main thread
# while True:
#     time.sleep(5)
#     print("Main thread: %d" % time.time())


""" neuer Versuch """


# def on_message(ws, message):
#     print(message)
#
#
# def on_error(ws, error):
#     print(error)
#
#
# def on_close(ws, close_status_code, close_msg):
#     print("### closed ###")
#
#
# def on_open(ws):
#     global _access_token
#     print("### opened ###")
#     print('### authorize ###')
#     send(ws=ws, endpoint="authorize", body=_access_token)
#     chart(ws=ws)
#
#
# def send(ws, endpoint, query=None, body=None):
#     global _request_id
#     _request_id += 1
#     print(f"{endpoint}\n{_request_id}\n{query}\n{body}")
#     ws.send(f"{endpoint}\n{_request_id}\n{query}\n{body}")
#
#
# def connect_ws():
#     print('### connect ###')
#     global _ws
#     websocket.enableTrace(True)
#     _ws = websocket.WebSocketApp(definitions.TRADOVATE_WEBSOCKET_URL,
#                                  on_open=on_open,
#                                  on_message=on_message,
#                                  on_error=on_error,
#                                  on_close=on_close)
#
#     _ws.run_forever(dispatcher=rel)  # Set dispatcher to automatic reconnection
#     rel.signal(2, rel.abort)  # Keyboard Interrupt
#
#
# # def heartbeat():
# #     asyncio.sleep(2.5)
# #     ws.send('[]')
#
#
# def chart(ws):
#     print('### chart ###')
#     body = {
#         "symbol": definitions.TRADOVATE_SYMBOL,
#         "chartDescription": {
#             "underlyingType": "MinuteBar",
#             "elementSize": 1,
#             "elementSizeUnit": "UnderlyingUnits",
#             "withHistogram": False,
#         },
#         "timeRange": {
#             "asMuchAsElements": 20
#         }
#     }
#     # print(f"md/getChart\n{_request_id}\n\n{json.dumps(body)}")
#     send(ws=ws, endpoint="md/getChart", body=json.dumps(body))
#
#
# if __name__ == "__main__":
#     tradovate_auth()
#     _thread.start_new_thread(connect_ws, ())
#     while True:
#         time.sleep(5)
#         print('### main thread ###')
