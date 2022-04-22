from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.place_oco import PlaceOCO
from ...models.place_oco_result import PlaceOcoResult
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: PlaceOCO,
) -> Dict[str, Any]:
    url = "{}/order/placeoco".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[PlaceOcoResult]:
    if response.status_code == 200:
        response_200 = PlaceOcoResult.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[PlaceOcoResult]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: PlaceOCO,
) -> Response[PlaceOcoResult]:
    """### Place a Order Cancels Order order strategy.
    OCO order strategies link 2 orders together such that if one order is filled, the other order is
    cancelled. You must provide an `other` parameter pertaining to the order linked to this one. The
    `other` must specify an `action` and an `orderType` which determines the other parameters that must
    be set. For example a Limit or Stop order must use the `price` parameter, but a Stop-Limit will
    require a `price` and a `stopPrice`. Below is an example of an OCO that either sells to take profit
    at 4200 points, or sells to stop loss at 4100 points.

    ```js
    const URL = 'demo.tradovateapi.com/v1'
    const limit = {
        action: 'Sell',
        orderType: 'Limit',
        price: 4200.00
    }
    const oco = {
        accountSpec: yourUserName,
        accountId: yourAcctId,
        action: \"Buy\",
        symbol: \"MESM1\",
        orderQty: 1,
        orderType: \"Stop\",
        price: 4100.00
        isAutomated: true, //must be true if this isn't an order made directly by a human
        other: limit
    }

    const response = await fetch(URL + '/order/placeoco', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Authorization': `Bearer ${myAccessToken}`,
        },
        body: JSON.stringify(oco)
    })

    const json = await response.json() // { orderId: 0000000, ocoId: 0000000 }
    ```

    Args:
        json_body (PlaceOCO):

    Returns:
        Response[PlaceOcoResult]
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
    json_body: PlaceOCO,
) -> Optional[PlaceOcoResult]:
    """### Place a Order Cancels Order order strategy.
    OCO order strategies link 2 orders together such that if one order is filled, the other order is
    cancelled. You must provide an `other` parameter pertaining to the order linked to this one. The
    `other` must specify an `action` and an `orderType` which determines the other parameters that must
    be set. For example a Limit or Stop order must use the `price` parameter, but a Stop-Limit will
    require a `price` and a `stopPrice`. Below is an example of an OCO that either sells to take profit
    at 4200 points, or sells to stop loss at 4100 points.

    ```js
    const URL = 'demo.tradovateapi.com/v1'
    const limit = {
        action: 'Sell',
        orderType: 'Limit',
        price: 4200.00
    }
    const oco = {
        accountSpec: yourUserName,
        accountId: yourAcctId,
        action: \"Buy\",
        symbol: \"MESM1\",
        orderQty: 1,
        orderType: \"Stop\",
        price: 4100.00
        isAutomated: true, //must be true if this isn't an order made directly by a human
        other: limit
    }

    const response = await fetch(URL + '/order/placeoco', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Authorization': `Bearer ${myAccessToken}`,
        },
        body: JSON.stringify(oco)
    })

    const json = await response.json() // { orderId: 0000000, ocoId: 0000000 }
    ```

    Args:
        json_body (PlaceOCO):

    Returns:
        Response[PlaceOcoResult]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: PlaceOCO,
) -> Response[PlaceOcoResult]:
    """### Place a Order Cancels Order order strategy.
    OCO order strategies link 2 orders together such that if one order is filled, the other order is
    cancelled. You must provide an `other` parameter pertaining to the order linked to this one. The
    `other` must specify an `action` and an `orderType` which determines the other parameters that must
    be set. For example a Limit or Stop order must use the `price` parameter, but a Stop-Limit will
    require a `price` and a `stopPrice`. Below is an example of an OCO that either sells to take profit
    at 4200 points, or sells to stop loss at 4100 points.

    ```js
    const URL = 'demo.tradovateapi.com/v1'
    const limit = {
        action: 'Sell',
        orderType: 'Limit',
        price: 4200.00
    }
    const oco = {
        accountSpec: yourUserName,
        accountId: yourAcctId,
        action: \"Buy\",
        symbol: \"MESM1\",
        orderQty: 1,
        orderType: \"Stop\",
        price: 4100.00
        isAutomated: true, //must be true if this isn't an order made directly by a human
        other: limit
    }

    const response = await fetch(URL + '/order/placeoco', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Authorization': `Bearer ${myAccessToken}`,
        },
        body: JSON.stringify(oco)
    })

    const json = await response.json() // { orderId: 0000000, ocoId: 0000000 }
    ```

    Args:
        json_body (PlaceOCO):

    Returns:
        Response[PlaceOcoResult]
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
    json_body: PlaceOCO,
) -> Optional[PlaceOcoResult]:
    """### Place a Order Cancels Order order strategy.
    OCO order strategies link 2 orders together such that if one order is filled, the other order is
    cancelled. You must provide an `other` parameter pertaining to the order linked to this one. The
    `other` must specify an `action` and an `orderType` which determines the other parameters that must
    be set. For example a Limit or Stop order must use the `price` parameter, but a Stop-Limit will
    require a `price` and a `stopPrice`. Below is an example of an OCO that either sells to take profit
    at 4200 points, or sells to stop loss at 4100 points.

    ```js
    const URL = 'demo.tradovateapi.com/v1'
    const limit = {
        action: 'Sell',
        orderType: 'Limit',
        price: 4200.00
    }
    const oco = {
        accountSpec: yourUserName,
        accountId: yourAcctId,
        action: \"Buy\",
        symbol: \"MESM1\",
        orderQty: 1,
        orderType: \"Stop\",
        price: 4100.00
        isAutomated: true, //must be true if this isn't an order made directly by a human
        other: limit
    }

    const response = await fetch(URL + '/order/placeoco', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Authorization': `Bearer ${myAccessToken}`,
        },
        body: JSON.stringify(oco)
    })

    const json = await response.json() // { orderId: 0000000, ocoId: 0000000 }
    ```

    Args:
        json_body (PlaceOCO):

    Returns:
        Response[PlaceOcoResult]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
