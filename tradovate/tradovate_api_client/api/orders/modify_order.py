from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.command_result import CommandResult
from ...models.modify_order import ModifyOrder
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: ModifyOrder,
) -> Dict[str, Any]:
    url = "{}/order/modifyorder".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[CommandResult]:
    if response.status_code == 200:
        response_200 = CommandResult.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[CommandResult]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: ModifyOrder,
) -> Response[CommandResult]:
    """### Make a request to modify the parameters of an order.
    You can request changes to an order, such as the trigger price for a Stop or Limit order.
    > Note: This is no guarantee that the order can be modified in a given way. Market and exchange
    rules apply.

    Args:
        json_body (ModifyOrder):

    Returns:
        Response[CommandResult]
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
    json_body: ModifyOrder,
) -> Optional[CommandResult]:
    """### Make a request to modify the parameters of an order.
    You can request changes to an order, such as the trigger price for a Stop or Limit order.
    > Note: This is no guarantee that the order can be modified in a given way. Market and exchange
    rules apply.

    Args:
        json_body (ModifyOrder):

    Returns:
        Response[CommandResult]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: ModifyOrder,
) -> Response[CommandResult]:
    """### Make a request to modify the parameters of an order.
    You can request changes to an order, such as the trigger price for a Stop or Limit order.
    > Note: This is no guarantee that the order can be modified in a given way. Market and exchange
    rules apply.

    Args:
        json_body (ModifyOrder):

    Returns:
        Response[CommandResult]
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
    json_body: ModifyOrder,
) -> Optional[CommandResult]:
    """### Make a request to modify the parameters of an order.
    You can request changes to an order, such as the trigger price for a Stop or Limit order.
    > Note: This is no guarantee that the order can be modified in a given way. Market and exchange
    rules apply.

    Args:
        json_body (ModifyOrder):

    Returns:
        Response[CommandResult]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
