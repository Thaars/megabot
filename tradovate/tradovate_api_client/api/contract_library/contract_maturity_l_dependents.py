from typing import Any, Dict, List, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.contract_maturity import ContractMaturity
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    masterids: List[int],
) -> Dict[str, Any]:
    url = "{}/contractMaturity/ldeps".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_masterids = masterids

    params["masterids"] = json_masterids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[ContractMaturity]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ContractMaturity.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[ContractMaturity]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    masterids: List[int],
) -> Response[List[ContractMaturity]]:
    """Retrieves all entities of ContractMaturity type related to multiple entities of Product type

    Args:
        masterids (List[int]):

    Returns:
        Response[List[ContractMaturity]]
    """

    kwargs = _get_kwargs(
        client=client,
        masterids=masterids,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    masterids: List[int],
) -> Optional[List[ContractMaturity]]:
    """Retrieves all entities of ContractMaturity type related to multiple entities of Product type

    Args:
        masterids (List[int]):

    Returns:
        Response[List[ContractMaturity]]
    """

    return sync_detailed(
        client=client,
        masterids=masterids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    masterids: List[int],
) -> Response[List[ContractMaturity]]:
    """Retrieves all entities of ContractMaturity type related to multiple entities of Product type

    Args:
        masterids (List[int]):

    Returns:
        Response[List[ContractMaturity]]
    """

    kwargs = _get_kwargs(
        client=client,
        masterids=masterids,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    masterids: List[int],
) -> Optional[List[ContractMaturity]]:
    """Retrieves all entities of ContractMaturity type related to multiple entities of Product type

    Args:
        masterids (List[int]):

    Returns:
        Response[List[ContractMaturity]]
    """

    return (
        await asyncio_detailed(
            client=client,
            masterids=masterids,
        )
    ).parsed