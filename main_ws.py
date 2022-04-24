"""
    Reconnect / Refresh Access Token: https://community.tradovate.com/t/sequence-numbers/4102/4
    Contract Month Codes: https://www.cmegroup.com/month-codes.html
    Automated Orders: https://api.tradovate.com/#section/Automated-Orders
"""
import hashlib
import json

import pandas as pd
import math
import os.path
import time

import asyncio
import websockets
from binance.client import Client
from datetime import timedelta, datetime, date
from dateutil import parser
import yfinance as yf
from pandas_finance import Equity

# API
import definitions
from api_key import *
from db import DB

from tradovate.tradovate_api_client import Client as TradovateClient
from tradovate.tradovate_api_client import AuthenticatedClient
from tradovate.tradovate_api_client.api.accounting import account_list
from tradovate.tradovate_api_client.api.authentication import access_token_request
from tradovate.tradovate_api_client.api.users import user_list, sync_request
from tradovate.tradovate_api_client.models import AccessTokenRequest


async def get_tradovate_data():

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
    access_token = access_token_response.access_token
    authenticated_client = AuthenticatedClient(
        base_url=definitions.TRADOVATE_URL,
        token=access_token
    )

    account_list_response = account_list.sync(client=authenticated_client)
    #
    # user_list_response = user_list.sync(client=authenticated_client)

    await open_ws(access_token)


async def heartbeat(websocket):
    while True:
        await asyncio.sleep(2.5)
        await websocket.send('[]')


async def get_chart(websocket, request_id):
    body = {
        "symbol": definitions.SYMBOL,
        "chartDescription": {
            "underlyingType": "MinuteBar",
            "elementSize": 1,
            "elementSizeUnit": "UnderlyingUnits",
            "withHistogram": False,
        },
        "timeRange": {
            "asFarAsTimestamp": "2022-01-01T00:00Z",
            "closestTimestamp": "2022-01-20T00:00Z",
            # "closestTickId": 123,
            # "asMuchAsElements": 66
        }
    }
    # message = [
    #     "md/getChart",
    #     str(request_id),
    #     "",
    #     json.dumps(body)
    # ]
    # await websocket.send(message)
    await asyncio.sleep(1)
    print(f"md/getChart\n{request_id}\n\n{json.dumps(body)}")
    await websocket.send(f"md/getChart\n{request_id}\n\n{json.dumps(body)}")
    while True:
        await asyncio.sleep(30)


async def subscribe_quote(websocket, request_id):
    await asyncio.sleep(2)
    body = {
        "symbol": definitions.SYMBOL
    }
    message = [
        "md/subscribeQuote",
        str(request_id),
        "\n",
        json.dumps(body)
    ]
    await websocket.send(message)
    # print(f"md/subscribeQuote\n{request_id}\n\n{json.dumps(body)}")
    # await websocket.send(f"md/subscribeQuote\n{request_id}\n\n{json.dumps(body)}")


async def receive(websocket):
    while True:
        response = await websocket.recv()
        print(f"receive: {response}")

        if response:
            response_type = response[0]
            if response_type == "h":
                print("\tws -- MD -- heartbeat -- ")
            elif response_type == "c":
                print("ws -- close message -- [{0}]".format(response))
            elif response_type == "a":
                jmsg = json.loads(response[2:-1])
                event_msg = jmsg.get('e')
                response_status = jmsg.get('s')
                if response_status is not None:
                    if response_status == 200:
                        response_id = jmsg['i']
                        historical_id = jmsg.get('historicalId')
                        realtime_id = jmsg.get('realtimeId')
                    else:
                        print("got response ERROR --\n{0}\n".format(jmsg))

                if event_msg is not None:
                    charts = jmsg.get('d', {}).get('charts', {})

                    if charts is not None:
                        for chart in charts:
                            bars = chart.get('bars')

                            if bars is not None:
                                for ix, item in enumerate(bars):

                                    result_list = [
                                        definitions.SYMBOL,
                                        item['timestamp'].replace('T', ' ').replace('Z', ':00'),
                                        float(item['open']),
                                        float(item['high']),
                                        float(item['low']),
                                        float(item['close']),
                                        float(item['upVolume']),
                                        float(item['downVolume']),
                                        float(item['upTicks']),
                                        float(item['downTicks']),
                                        float(item['bidVolume']),
                                        float(item['offerVolume']),
                                    ]
                                    result_hash = get_hash_from_list(result_list)
                                    result_list += [result_hash]

                                    db = DB().db
                                    db_cursor = db.cursor(dictionary=True)
                                    db_cursor.execute(
                                        "select * from minute_bars where `hash` = %s",
                                        [result_hash]
                                    )
                                    db_cursor.fetchone()
                                    if db_cursor.rowcount == -1:
                                        db_cursor = db.cursor()
                                        db_cursor.execute(
                                            "insert into minute_bars ("
                                                "`symbol`,"
                                                "`timestamp`,"
                                                "`open`,"
                                                "`high`,"
                                                "`low`,"
                                                "`close`,"
                                                "`up_volume`,"
                                                "`down_volume`,"
                                                "`up_ticks`,"
                                                "`down_ticks`,"
                                                "`bid_volume`,"
                                                "`offer_volume`,"
                                                "`hash`"
                                            ") values ("
                                                "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s"
                                            ")", tuple(result_list))
                                        db.commit()
                # else:
                #     response_status = jmsg['s']
                #     if response_status == 200:
                #         response_id = jmsg['i']
                #         if jmsg.get('d') is not None:
                #             response_pld = jmsg['d']
                #
                #     else:
                #         print("got response ERROR --\n{0}\n".format(jmsg))


async def open_ws(access_token):
    request_id = 1
    async with websockets.connect(definitions.TRADOVATE_WEBSOCKET_URL) as websocket:

        receive_task = asyncio.create_task(receive(websocket), name='receive')

        await websocket.send(f"authorize\n{request_id}\n\n{access_token}")
        request_id += 1

        # asyncio.create_task(chart(websocket, request_id), name='chart')
        # request_id += 1
        # asyncio.create_task(subscribe_quote(websocket, request_id), name='subscribe_quote')
        # request_id += 1

        asyncio.create_task(heartbeat(websocket), name='heartbeat')

        asyncio.create_task(get_chart(websocket, request_id), name='chart')
        request_id += 1

        # asyncio.create_task(subscribe_quote(websocket, request_id), name='subscribe_quote')
        # request_id += 1

        await asyncio.Future()  # run forever


def get_hash_from_list(hashable_list):
    return hashlib.md5(b'' + json.dumps(hashable_list).encode('UTF-8')).hexdigest()


async def main():
    print('run ws')
    await get_tradovate_data()


asyncio.run(main())
