from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.place_oso import PlaceOSO
from ...models.place_oso_result import PlaceOsoResult
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: PlaceOSO,
) -> Dict[str, Any]:
    url = "{}/order/placeoso".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[PlaceOsoResult]:
    if response.status_code == 200:
        response_200 = PlaceOsoResult.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PlaceOsoResult]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: PlaceOSO,
) -> Response[PlaceOsoResult]:
    """### Place an Order Sends Order order strategy.
    In the Trader application, the details of OSO orders can be viewed by adding the Order Ticket module
    to your workspace and selecting the Advanced workspace options with Brackets enabled. OSO orders
    allow for the most complex multi-bracket trading strategies. As an example, imagine MESM1 is trading
    around 4175.00 points. You want to place a Buy order for 4150.00 points, buying below market. We
    place an OSO to take profits at 4200.00 points. If the initial order is filled, the `bracket1` order
    will be sent. Below is an example in JavaScript:

    ```js
    const URL = 'demo.tradovateapi.com/v1'

    const oso = {
        action: 'Sell',
        orderType: 'Limit',
        price: 4200.00,
    }

    const initial = {
        accountSpec: yourUserName,
        accountId: yourAcctId,
        action: \"Buy\",
        symbol: \"MESM1\",
        orderQty: 1,
        orderType: \"Limit\",
        price: 4150.00,
        isAutomated: true //must be true if this isn't an order made directly by a human
        bracket1: oso
    }

    const response = await fetch(URL + '/order/placeorder', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Authorization': `Bearer ${myAccessToken}`,
        },
        body: JSON.stringify(initial)
    })

    const json = await response.json() // { orderId: 0000000 }
    ```

    Args:
        json_body (PlaceOSO):

    Returns:
        Response[PlaceOsoResult]
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
    json_body: PlaceOSO,
) -> Optional[PlaceOsoResult]:
    """### Place an Order Sends Order order strategy.
    In the Trader application, the details of OSO orders can be viewed by adding the Order Ticket module
    to your workspace and selecting the Advanced workspace options with Brackets enabled. OSO orders
    allow for the most complex multi-bracket trading strategies. As an example, imagine MESM1 is trading
    around 4175.00 points. You want to place a Buy order for 4150.00 points, buying below market. We
    place an OSO to take profits at 4200.00 points. If the initial order is filled, the `bracket1` order
    will be sent. Below is an example in JavaScript:

    ```js
    const URL = 'demo.tradovateapi.com/v1'

    const oso = {
        action: 'Sell',
        orderType: 'Limit',
        price: 4200.00,
    }

    const initial = {
        accountSpec: yourUserName,
        accountId: yourAcctId,
        action: \"Buy\",
        symbol: \"MESM1\",
        orderQty: 1,
        orderType: \"Limit\",
        price: 4150.00,
        isAutomated: true //must be true if this isn't an order made directly by a human
        bracket1: oso
    }

    const response = await fetch(URL + '/order/placeorder', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Authorization': `Bearer ${myAccessToken}`,
        },
        body: JSON.stringify(initial)
    })

    const json = await response.json() // { orderId: 0000000 }
    ```

    Args:
        json_body (PlaceOSO):

    Returns:
        Response[PlaceOsoResult]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: PlaceOSO,
) -> Response[PlaceOsoResult]:
    """### Place an Order Sends Order order strategy.
    In the Trader application, the details of OSO orders can be viewed by adding the Order Ticket module
    to your workspace and selecting the Advanced workspace options with Brackets enabled. OSO orders
    allow for the most complex multi-bracket trading strategies. As an example, imagine MESM1 is trading
    around 4175.00 points. You want to place a Buy order for 4150.00 points, buying below market. We
    place an OSO to take profits at 4200.00 points. If the initial order is filled, the `bracket1` order
    will be sent. Below is an example in JavaScript:

    ```js
    const URL = 'demo.tradovateapi.com/v1'

    const oso = {
        action: 'Sell',
        orderType: 'Limit',
        price: 4200.00,
    }

    const initial = {
        accountSpec: yourUserName,
        accountId: yourAcctId,
        action: \"Buy\",
        symbol: \"MESM1\",
        orderQty: 1,
        orderType: \"Limit\",
        price: 4150.00,
        isAutomated: true //must be true if this isn't an order made directly by a human
        bracket1: oso
    }

    const response = await fetch(URL + '/order/placeorder', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Authorization': `Bearer ${myAccessToken}`,
        },
        body: JSON.stringify(initial)
    })

    const json = await response.json() // { orderId: 0000000 }
    ```

    Args:
        json_body (PlaceOSO):

    Returns:
        Response[PlaceOsoResult]
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
    json_body: PlaceOSO,
) -> Optional[PlaceOsoResult]:
    """### Place an Order Sends Order order strategy.
    In the Trader application, the details of OSO orders can be viewed by adding the Order Ticket module
    to your workspace and selecting the Advanced workspace options with Brackets enabled. OSO orders
    allow for the most complex multi-bracket trading strategies. As an example, imagine MESM1 is trading
    around 4175.00 points. You want to place a Buy order for 4150.00 points, buying below market. We
    place an OSO to take profits at 4200.00 points. If the initial order is filled, the `bracket1` order
    will be sent. Below is an example in JavaScript:

    ```js
    const URL = 'demo.tradovateapi.com/v1'

    const oso = {
        action: 'Sell',
        orderType: 'Limit',
        price: 4200.00,
    }

    const initial = {
        accountSpec: yourUserName,
        accountId: yourAcctId,
        action: \"Buy\",
        symbol: \"MESM1\",
        orderQty: 1,
        orderType: \"Limit\",
        price: 4150.00,
        isAutomated: true //must be true if this isn't an order made directly by a human
        bracket1: oso
    }

    const response = await fetch(URL + '/order/placeorder', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Authorization': `Bearer ${myAccessToken}`,
        },
        body: JSON.stringify(initial)
    })

    const json = await response.json() // { orderId: 0000000 }
    ```

    Args:
        json_body (PlaceOSO):

    Returns:
        Response[PlaceOsoResult]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
