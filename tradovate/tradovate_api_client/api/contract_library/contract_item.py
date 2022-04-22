from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.contract import Contract
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    id: int,
) -> Dict[str, Any]:
    url = "{}/contract/item".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[Contract]:
    if response.status_code == 200:
        response_200 = Contract.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Contract]:
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
) -> Response[Contract]:
    """Retrieves an entity of Contract type by its id

    Args:
        id (int):

    Returns:
        Response[Contract]
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
) -> Optional[Contract]:
    """Retrieves an entity of Contract type by its id

    Args:
        id (int):

    Returns:
        Response[Contract]
    """

    return sync_detailed(
        client=client,
        id=id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    id: int,
) -> Response[Contract]:
    """Retrieves an entity of Contract type by its id

    Args:
        id (int):

    Returns:
        Response[Contract]
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
) -> Optional[Contract]:
    """Retrieves an entity of Contract type by its id

    Args:
        id (int):

    Returns:
        Response[Contract]
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
        )
    ).parsed
