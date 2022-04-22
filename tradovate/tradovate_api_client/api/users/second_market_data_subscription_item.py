from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.second_market_data_subscription import SecondMarketDataSubscription
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    id: int,
) -> Dict[str, Any]:
    url = "{}/secondMarketDataSubscription/item".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["id"] = id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[SecondMarketDataSubscription]:
    if response.status_code == 200:
        response_200 = SecondMarketDataSubscription.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[SecondMarketDataSubscription]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    id: int,
) -> Response[SecondMarketDataSubscription]:
    """Retrieves an entity of SecondMarketDataSubscription type by its id

    Args:
        id (int):

    Returns:
        Response[SecondMarketDataSubscription]
    """

    kwargs = _get_kwargs(
        client=client,
        id=id,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    id: int,
) -> Optional[SecondMarketDataSubscription]:
    """Retrieves an entity of SecondMarketDataSubscription type by its id

    Args:
        id (int):

    Returns:
        Response[SecondMarketDataSubscription]
    """

    return sync_detailed(
        client=client,
        id=id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    id: int,
) -> Response[SecondMarketDataSubscription]:
    """Retrieves an entity of SecondMarketDataSubscription type by its id

    Args:
        id (int):

    Returns:
        Response[SecondMarketDataSubscription]
    """

    kwargs = _get_kwargs(
        client=client,
        id=id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    id: int,
) -> Optional[SecondMarketDataSubscription]:
    """Retrieves an entity of SecondMarketDataSubscription type by its id

    Args:
        id (int):

    Returns:
        Response[SecondMarketDataSubscription]
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
        )
    ).parsed
