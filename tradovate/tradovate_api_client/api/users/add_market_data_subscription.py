from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.add_market_data_subscription import AddMarketDataSubscription
from ...models.market_data_subscription_response import MarketDataSubscriptionResponse
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: AddMarketDataSubscription,
) -> Dict[str, Any]:
    url = "{}/user/addmarketdatasubscription".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[MarketDataSubscriptionResponse]:
    if response.status_code == 200:
        response_200 = MarketDataSubscriptionResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[MarketDataSubscriptionResponse]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: AddMarketDataSubscription,
) -> Response[MarketDataSubscriptionResponse]:
    """### Add a subscription to Market Data for a user.

    Args:
        json_body (AddMarketDataSubscription):

    Returns:
        Response[MarketDataSubscriptionResponse]
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
    json_body: AddMarketDataSubscription,
) -> Optional[MarketDataSubscriptionResponse]:
    """### Add a subscription to Market Data for a user.

    Args:
        json_body (AddMarketDataSubscription):

    Returns:
        Response[MarketDataSubscriptionResponse]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: AddMarketDataSubscription,
) -> Response[MarketDataSubscriptionResponse]:
    """### Add a subscription to Market Data for a user.

    Args:
        json_body (AddMarketDataSubscription):

    Returns:
        Response[MarketDataSubscriptionResponse]
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
    json_body: AddMarketDataSubscription,
) -> Optional[MarketDataSubscriptionResponse]:
    """### Add a subscription to Market Data for a user.

    Args:
        json_body (AddMarketDataSubscription):

    Returns:
        Response[MarketDataSubscriptionResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
