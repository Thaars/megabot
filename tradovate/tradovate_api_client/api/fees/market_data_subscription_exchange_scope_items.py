from typing import Any, Dict, List, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.market_data_subscription_exchange_scope import MarketDataSubscriptionExchangeScope
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    ids: List[int],
) -> Dict[str, Any]:
    url = "{}/marketDataSubscriptionExchangeScope/items".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_ids = ids

    params["ids"] = json_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[MarketDataSubscriptionExchangeScope]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = MarketDataSubscriptionExchangeScope.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[MarketDataSubscriptionExchangeScope]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    ids: List[int],
) -> Response[List[MarketDataSubscriptionExchangeScope]]:
    """Retrieves multiple entities of MarketDataSubscriptionExchangeScope type by its ids

    Args:
        ids (List[int]):

    Returns:
        Response[List[MarketDataSubscriptionExchangeScope]]
    """

    kwargs = _get_kwargs(
        client=client,
        ids=ids,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    ids: List[int],
) -> Optional[List[MarketDataSubscriptionExchangeScope]]:
    """Retrieves multiple entities of MarketDataSubscriptionExchangeScope type by its ids

    Args:
        ids (List[int]):

    Returns:
        Response[List[MarketDataSubscriptionExchangeScope]]
    """

    return sync_detailed(
        client=client,
        ids=ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    ids: List[int],
) -> Response[List[MarketDataSubscriptionExchangeScope]]:
    """Retrieves multiple entities of MarketDataSubscriptionExchangeScope type by its ids

    Args:
        ids (List[int]):

    Returns:
        Response[List[MarketDataSubscriptionExchangeScope]]
    """

    kwargs = _get_kwargs(
        client=client,
        ids=ids,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    ids: List[int],
) -> Optional[List[MarketDataSubscriptionExchangeScope]]:
    """Retrieves multiple entities of MarketDataSubscriptionExchangeScope type by its ids

    Args:
        ids (List[int]):

    Returns:
        Response[List[MarketDataSubscriptionExchangeScope]]
    """

    return (
        await asyncio_detailed(
            client=client,
            ids=ids,
        )
    ).parsed
