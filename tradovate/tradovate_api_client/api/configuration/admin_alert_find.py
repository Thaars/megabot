from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.admin_alert import AdminAlert
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    name: str,
) -> Dict[str, Any]:
    url = "{}/adminAlert/find".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["name"] = name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[AdminAlert]:
    if response.status_code == 200:
        response_200 = AdminAlert.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[AdminAlert]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    name: str,
) -> Response[AdminAlert]:
    """Retrieves an entity of AdminAlert type by its name

    Args:
        name (str):

    Returns:
        Response[AdminAlert]
    """

    kwargs = _get_kwargs(
        client=client,
        name=name,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    name: str,
) -> Optional[AdminAlert]:
    """Retrieves an entity of AdminAlert type by its name

    Args:
        name (str):

    Returns:
        Response[AdminAlert]
    """

    return sync_detailed(
        client=client,
        name=name,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    name: str,
) -> Response[AdminAlert]:
    """Retrieves an entity of AdminAlert type by its name

    Args:
        name (str):

    Returns:
        Response[AdminAlert]
    """

    kwargs = _get_kwargs(
        client=client,
        name=name,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    name: str,
) -> Optional[AdminAlert]:
    """Retrieves an entity of AdminAlert type by its name

    Args:
        name (str):

    Returns:
        Response[AdminAlert]
    """

    return (
        await asyncio_detailed(
            client=client,
            name=name,
        )
    ).parsed