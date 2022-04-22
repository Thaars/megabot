from typing import Any, Dict, List, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.alert_signal import AlertSignal
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/alertSignal/list".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[AlertSignal]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AlertSignal.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[AlertSignal]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[List[AlertSignal]]:
    """Retrieves all entities of AlertSignal type

    Returns:
        Response[List[AlertSignal]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Optional[List[AlertSignal]]:
    """Retrieves all entities of AlertSignal type

    Returns:
        Response[List[AlertSignal]]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[List[AlertSignal]]:
    """Retrieves all entities of AlertSignal type

    Returns:
        Response[List[AlertSignal]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Optional[List[AlertSignal]]:
    """Retrieves all entities of AlertSignal type

    Returns:
        Response[List[AlertSignal]]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
