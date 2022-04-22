from typing import Any, Dict, List, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.contract_margin import ContractMargin
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    masterid: int,
) -> Dict[str, Any]:
    url = "{}/contractMargin/deps".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["masterid"] = masterid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[ContractMargin]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ContractMargin.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[ContractMargin]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    masterid: int,
) -> Response[List[ContractMargin]]:
    """Retrieves all entities of ContractMargin type related to Contract entity

    Args:
        masterid (int):

    Returns:
        Response[List[ContractMargin]]
    """

    kwargs = _get_kwargs(
        client=client,
        masterid=masterid,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    masterid: int,
) -> Optional[List[ContractMargin]]:
    """Retrieves all entities of ContractMargin type related to Contract entity

    Args:
        masterid (int):

    Returns:
        Response[List[ContractMargin]]
    """

    return sync_detailed(
        client=client,
        masterid=masterid,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    masterid: int,
) -> Response[List[ContractMargin]]:
    """Retrieves all entities of ContractMargin type related to Contract entity

    Args:
        masterid (int):

    Returns:
        Response[List[ContractMargin]]
    """

    kwargs = _get_kwargs(
        client=client,
        masterid=masterid,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    masterid: int,
) -> Optional[List[ContractMargin]]:
    """Retrieves all entities of ContractMargin type related to Contract entity

    Args:
        masterid (int):

    Returns:
        Response[List[ContractMargin]]
    """

    return (
        await asyncio_detailed(
            client=client,
            masterid=masterid,
        )
    ).parsed
