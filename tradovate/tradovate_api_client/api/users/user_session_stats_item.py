from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.user_session_stats import UserSessionStats
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    id: int,
) -> Dict[str, Any]:
    url = "{}/userSessionStats/item".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[UserSessionStats]:
    if response.status_code == 200:
        response_200 = UserSessionStats.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[UserSessionStats]:
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
) -> Response[UserSessionStats]:
    """Retrieves an entity of UserSessionStats type by its id

    Args:
        id (int):

    Returns:
        Response[UserSessionStats]
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
) -> Optional[UserSessionStats]:
    """Retrieves an entity of UserSessionStats type by its id

    Args:
        id (int):

    Returns:
        Response[UserSessionStats]
    """

    return sync_detailed(
        client=client,
        id=id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    id: int,
) -> Response[UserSessionStats]:
    """Retrieves an entity of UserSessionStats type by its id

    Args:
        id (int):

    Returns:
        Response[UserSessionStats]
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
) -> Optional[UserSessionStats]:
    """Retrieves an entity of UserSessionStats type by its id

    Args:
        id (int):

    Returns:
        Response[UserSessionStats]
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
        )
    ).parsed
