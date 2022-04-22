from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.liquidate_position import LiquidatePosition
from ...models.place_order_result import PlaceOrderResult
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: LiquidatePosition,
) -> Dict[str, Any]:
    url = "{}/order/liquidateposition".format(client.base_url)

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
    json_body: LiquidatePosition,
) -> Response[PlaceOrderResult]:
    """### Send a request to cancel orders for a specific contract and close that position for the given
    account.
    This request initiates the cancellation process of open orders for an existing position held by this
    account.
    > Note: This is a request to cancel orders and close a position, not a guarantee. Any operation
    could fail for a number of reasons, ranging from Exchange rejection to incorrect parameterization.

    Args:
        json_body (LiquidatePosition):

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
    json_body: LiquidatePosition,
) -> Optional[PlaceOrderResult]:
    """### Send a request to cancel orders for a specific contract and close that position for the given
    account.
    This request initiates the cancellation process of open orders for an existing position held by this
    account.
    > Note: This is a request to cancel orders and close a position, not a guarantee. Any operation
    could fail for a number of reasons, ranging from Exchange rejection to incorrect parameterization.

    Args:
        json_body (LiquidatePosition):

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
    json_body: LiquidatePosition,
) -> Response[PlaceOrderResult]:
    """### Send a request to cancel orders for a specific contract and close that position for the given
    account.
    This request initiates the cancellation process of open orders for an existing position held by this
    account.
    > Note: This is a request to cancel orders and close a position, not a guarantee. Any operation
    could fail for a number of reasons, ranging from Exchange rejection to incorrect parameterization.

    Args:
        json_body (LiquidatePosition):

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
    json_body: LiquidatePosition,
) -> Optional[PlaceOrderResult]:
    """### Send a request to cancel orders for a specific contract and close that position for the given
    account.
    This request initiates the cancellation process of open orders for an existing position held by this
    account.
    > Note: This is a request to cancel orders and close a position, not a guarantee. Any operation
    could fail for a number of reasons, ranging from Exchange rejection to incorrect parameterization.

    Args:
        json_body (LiquidatePosition):

    Returns:
        Response[PlaceOrderResult]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
