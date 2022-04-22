from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.order_strategy_status_response import OrderStrategyStatusResponse
from ...models.start_order_strategy import StartOrderStrategy
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: StartOrderStrategy,
) -> Dict[str, Any]:
    url = "{}/orderStrategy/startorderstrategy".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[OrderStrategyStatusResponse]:
    if response.status_code == 200:
        response_200 = OrderStrategyStatusResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[OrderStrategyStatusResponse]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: StartOrderStrategy,
) -> Response[OrderStrategyStatusResponse]:
    """### Start a multi-bracket trading strategy.
    This endpoint is used with a WebSocket. You can create any number of brackets and add them to
    `brackets` field on the `params` object as a JSON string.

    ```js

    const URL = 'wss://demo.tradovateapi.com/v1'

    const params = {
        entryVersion: {
            orderQty: 1,
            orderType: \"Market\"
        },
        brackets: [{
            qty: 1,
            profitTarget: -30,
            stopLoss: 15,
            trailingStop: false
        }]
    }

    const body = {
        accountId: myAcctId,
        accountSpec: name,
        symbol: 'MESM1',
        action: 'Sell',
        orderStrategyTypeId: 2, //2 is 'multibracket', we currently only offer this strategy but more
    may exist in the future.
        params: JSON.stringify(params)
    }

    const mySocket = new WebSocket(URL)

    //websocket authorization procedure omitted for simplicity...

    //send this message with an authorized socket
    mySocket.send(`orderstrategy/startorderstrategy\n4\n\n${JSON.stringify(body)}`)

    ```

    For more details about working with advanced order types, see [placeOrder](/#operation/placeOrder),
    [placeOCO](/#operation/placeOCO), and [placeOSO](/#operation/placeOSO).

    Args:
        json_body (StartOrderStrategy):

    Returns:
        Response[OrderStrategyStatusResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    json_body: StartOrderStrategy,
) -> Optional[OrderStrategyStatusResponse]:
    """### Start a multi-bracket trading strategy.
    This endpoint is used with a WebSocket. You can create any number of brackets and add them to
    `brackets` field on the `params` object as a JSON string.

    ```js

    const URL = 'wss://demo.tradovateapi.com/v1'

    const params = {
        entryVersion: {
            orderQty: 1,
            orderType: \"Market\"
        },
        brackets: [{
            qty: 1,
            profitTarget: -30,
            stopLoss: 15,
            trailingStop: false
        }]
    }

    const body = {
        accountId: myAcctId,
        accountSpec: name,
        symbol: 'MESM1',
        action: 'Sell',
        orderStrategyTypeId: 2, //2 is 'multibracket', we currently only offer this strategy but more
    may exist in the future.
        params: JSON.stringify(params)
    }

    const mySocket = new WebSocket(URL)

    //websocket authorization procedure omitted for simplicity...

    //send this message with an authorized socket
    mySocket.send(`orderstrategy/startorderstrategy\n4\n\n${JSON.stringify(body)}`)

    ```

    For more details about working with advanced order types, see [placeOrder](/#operation/placeOrder),
    [placeOCO](/#operation/placeOCO), and [placeOSO](/#operation/placeOSO).

    Args:
        json_body (StartOrderStrategy):

    Returns:
        Response[OrderStrategyStatusResponse]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: StartOrderStrategy,
) -> Response[OrderStrategyStatusResponse]:
    """### Start a multi-bracket trading strategy.
    This endpoint is used with a WebSocket. You can create any number of brackets and add them to
    `brackets` field on the `params` object as a JSON string.

    ```js

    const URL = 'wss://demo.tradovateapi.com/v1'

    const params = {
        entryVersion: {
            orderQty: 1,
            orderType: \"Market\"
        },
        brackets: [{
            qty: 1,
            profitTarget: -30,
            stopLoss: 15,
            trailingStop: false
        }]
    }

    const body = {
        accountId: myAcctId,
        accountSpec: name,
        symbol: 'MESM1',
        action: 'Sell',
        orderStrategyTypeId: 2, //2 is 'multibracket', we currently only offer this strategy but more
    may exist in the future.
        params: JSON.stringify(params)
    }

    const mySocket = new WebSocket(URL)

    //websocket authorization procedure omitted for simplicity...

    //send this message with an authorized socket
    mySocket.send(`orderstrategy/startorderstrategy\n4\n\n${JSON.stringify(body)}`)

    ```

    For more details about working with advanced order types, see [placeOrder](/#operation/placeOrder),
    [placeOCO](/#operation/placeOCO), and [placeOSO](/#operation/placeOSO).

    Args:
        json_body (StartOrderStrategy):

    Returns:
        Response[OrderStrategyStatusResponse]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    json_body: StartOrderStrategy,
) -> Optional[OrderStrategyStatusResponse]:
    """### Start a multi-bracket trading strategy.
    This endpoint is used with a WebSocket. You can create any number of brackets and add them to
    `brackets` field on the `params` object as a JSON string.

    ```js

    const URL = 'wss://demo.tradovateapi.com/v1'

    const params = {
        entryVersion: {
            orderQty: 1,
            orderType: \"Market\"
        },
        brackets: [{
            qty: 1,
            profitTarget: -30,
            stopLoss: 15,
            trailingStop: false
        }]
    }

    const body = {
        accountId: myAcctId,
        accountSpec: name,
        symbol: 'MESM1',
        action: 'Sell',
        orderStrategyTypeId: 2, //2 is 'multibracket', we currently only offer this strategy but more
    may exist in the future.
        params: JSON.stringify(params)
    }

    const mySocket = new WebSocket(URL)

    //websocket authorization procedure omitted for simplicity...

    //send this message with an authorized socket
    mySocket.send(`orderstrategy/startorderstrategy\n4\n\n${JSON.stringify(body)}`)

    ```

    For more details about working with advanced order types, see [placeOrder](/#operation/placeOrder),
    [placeOCO](/#operation/placeOCO), and [placeOSO](/#operation/placeOSO).

    Args:
        json_body (StartOrderStrategy):

    Returns:
        Response[OrderStrategyStatusResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
