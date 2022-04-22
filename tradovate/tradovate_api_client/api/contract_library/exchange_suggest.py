from typing import Any, Dict, List, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.exchange import Exchange
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    t: str,
    l: int,
) -> Dict[str, Any]:
    url = "{}/exchange/suggest".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["t"] = t

    params["l"] = l

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[Exchange]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Exchange.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[Exchange]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    t: str,
    l: int,
) -> Response[List[Exchange]]:
    """Retrieves entities of Exchange type filtered by an occurrence of a text in one of its fields

    Args:
        t (str):
        l (int):

    Returns:
        Response[List[Exchange]]
    """

    kwargs = _get_kwargs(
        client=client,
        t=t,
        l=l,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    t: str,
    l: int,
) -> Optional[List[Exchange]]:
    """Retrieves entities of Exchange type filtered by an occurrence of a text in one of its fields

    Args:
        t (str):
        l (int):

    Returns:
        Response[List[Exchange]]
    """

    return sync_detailed(
        client=client,
        t=t,
        l=l,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    t: str,
    l: int,
) -> Response[List[Exchange]]:
    """Retrieves entities of Exchange type filtered by an occurrence of a text in one of its fields

    Args:
        t (str):
        l (int):

    Returns:
        Response[List[Exchange]]
    """

    kwargs = _get_kwargs(
        client=client,
        t=t,
        l=l,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    t: str,
    l: int,
) -> Optional[List[Exchange]]:
    """Retrieves entities of Exchange type filtered by an occurrence of a text in one of its fields

    Args:
        t (str):
        l (int):

    Returns:
        Response[List[Exchange]]
    """

    return (
        await asyncio_detailed(
            client=client,
            t=t,
            l=l,
        )
    ).parsed
