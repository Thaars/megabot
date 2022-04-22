from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.place_order import PlaceOrder
from ...models.place_order_result import PlaceOrderResult
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: PlaceOrder,
) -> Dict[str, Any]:
    url = "{}/order/placeorder".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[PlaceOrderResult]:
    if response.status_code == 200:
        response_200 = PlaceOrderResult.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PlaceOrderResult]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: PlaceOrder,
) -> Response[PlaceOrderResult]:
    """### Make a request to place an order.
    Depending on the order type, the parameters vary. In the Trader application, you can see the details
    of placing a standard order ticket by adding the Order Ticket module to your workspace.

    #### *Market Order*
    ```js
    const URL = 'demo.tradovateapi.com/v1'
    const body = {
        accountSpec: yourUserName,
        accountId: yourAcctId,
        action: \"Buy\",
        symbol: \"MYMM1\",
        orderQty: 1,
        orderType: \"Market\",
        isAutomated: true //must be true if this isn't an order made directly by a human
    }

    const response = await fetch(URL + '/order/placeorder', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Authorization': `Bearer ${myAccessToken}`,
        },
        body: JSON.stringify(body)
    })

    const json = await response.json() // { orderId: 0000000 }

    ```

    #### *Sell Limit*
    ```js
    const URL = 'demo.tradovateapi.com/v1'
    const body = {
        accountSpec: yourUserName,
        accountId: yourAcctId,
        action: \"Sell\",
        symbol: \"MYMM1\",
        orderQty: 1,
        orderType: \"Limit\",
        price: 35000, //use for single value like limit or stop
        isAutomated: true //must be true if this isn't an order made directly by a human
    }

    const response = await fetch(URL + '/order/placeorder', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Authorization': `Bearer ${myAccessToken}`,
        },
        body: JSON.stringify(body)
    })

    const json = await response.json() // { orderId: 0000000 }

    ```

    Args:
        json_body (PlaceOrder):

    Returns:
        Response[PlaceOrderResult]
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
    json_body: PlaceOrder,
) -> Optional[PlaceOrderResult]:
    """### Make a request to place an order.
    Depending on the order type, the parameters vary. In the Trader application, you can see the details
    of placing a standard order ticket by adding the Order Ticket module to your workspace.

    #### *Market Order*
    ```js
    const URL = 'demo.tradovateapi.com/v1'
    const body = {
        accountSpec: yourUserName,
        accountId: yourAcctId,
        action: \"Buy\",
        symbol: \"MYMM1\",
        orderQty: 1,
        orderType: \"Market\",
        isAutomated: true //must be true if this isn't an order made directly by a human
    }

    const response = await fetch(URL + '/order/placeorder', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Authorization': `Bearer ${myAccessToken}`,
        },
        body: JSON.stringify(body)
    })

    const json = await response.json() // { orderId: 0000000 }

    ```

    #### *Sell Limit*
    ```js
    const URL = 'demo.tradovateapi.com/v1'
    const body = {
        accountSpec: yourUserName,
        accountId: yourAcctId,
        action: \"Sell\",
        symbol: \"MYMM1\",
        orderQty: 1,
        orderType: \"Limit\",
        price: 35000, //use for single value like limit or stop
        isAutomated: true //must be true if this isn't an order made directly by a human
    }

    const response = await fetch(URL + '/order/placeorder', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Authorization': `Bearer ${myAccessToken}`,
        },
        body: JSON.stringify(body)
    })

    const json = await response.json() // { orderId: 0000000 }

    ```

    Args:
        json_body (PlaceOrder):

    Returns:
        Response[PlaceOrderResult]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: PlaceOrder,
) -> Response[PlaceOrderResult]:
    """### Make a request to place an order.
    Depending on the order type, the parameters vary. In the Trader application, you can see the details
    of placing a standard order ticket by adding the Order Ticket module to your workspace.

    #### *Market Order*
    ```js
    const URL = 'demo.tradovateapi.com/v1'
    const body = {
        accountSpec: yourUserName,
        accountId: yourAcctId,
        action: \"Buy\",
        symbol: \"MYMM1\",
        orderQty: 1,
        orderType: \"Market\",
        isAutomated: true //must be true if this isn't an order made directly by a human
    }

    const response = await fetch(URL + '/order/placeorder', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Authorization': `Bearer ${myAccessToken}`,
        },
        body: JSON.stringify(body)
    })

    const json = await response.json() // { orderId: 0000000 }

    ```

    #### *Sell Limit*
    ```js
    const URL = 'demo.tradovateapi.com/v1'
    const body = {
        accountSpec: yourUserName,
        accountId: yourAcctId,
        action: \"Sell\",
        symbol: \"MYMM1\",
        orderQty: 1,
        orderType: \"Limit\",
        price: 35000, //use for single value like limit or stop
        isAutomated: true //must be true if this isn't an order made directly by a human
    }

    const response = await fetch(URL + '/order/placeorder', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Authorization': `Bearer ${myAccessToken}`,
        },
        body: JSON.stringify(body)
    })

    const json = await response.json() // { orderId: 0000000 }

    ```

    Args:
        json_body (PlaceOrder):

    Returns:
        Response[PlaceOrderResult]
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
    json_body: PlaceOrder,
) -> Optional[PlaceOrderResult]:
    """### Make a request to place an order.
    Depending on the order type, the parameters vary. In the Trader application, you can see the details
    of placing a standard order ticket by adding the Order Ticket module to your workspace.

    #### *Market Order*
    ```js
    const URL = 'demo.tradovateapi.com/v1'
    const body = {
        accountSpec: yourUserName,
        accountId: yourAcctId,
        action: \"Buy\",
        symbol: \"MYMM1\",
        orderQty: 1,
        orderType: \"Market\",
        isAutomated: true //must be true if this isn't an order made directly by a human
    }

    const response = await fetch(URL + '/order/placeorder', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Authorization': `Bearer ${myAccessToken}`,
        },
        body: JSON.stringify(body)
    })

    const json = await response.json() // { orderId: 0000000 }

    ```

    #### *Sell Limit*
    ```js
    const URL = 'demo.tradovateapi.com/v1'
    const body = {
        accountSpec: yourUserName,
        accountId: yourAcctId,
        action: \"Sell\",
        symbol: \"MYMM1\",
        orderQty: 1,
        orderType: \"Limit\",
        price: 35000, //use for single value like limit or stop
        isAutomated: true //must be true if this isn't an order made directly by a human
    }

    const response = await fetch(URL + '/order/placeorder', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Authorization': `Bearer ${myAccessToken}`,
        },
        body: JSON.stringify(body)
    })

    const json = await response.json() // { orderId: 0000000 }

    ```

    Args:
        json_body (PlaceOrder):

    Returns:
        Response[PlaceOrderResult]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
