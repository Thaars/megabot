from typing import Any, Dict, List, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.account_risk_status import AccountRiskStatus
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    masterids: List[int],
) -> Dict[str, Any]:
    url = "{}/accountRiskStatus/ldeps".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[List[AccountRiskStatus]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AccountRiskStatus.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[AccountRiskStatus]]:
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
) -> Response[List[AccountRiskStatus]]:
    """Retrieves all entities of AccountRiskStatus type related to multiple entities of Account type

    Args:
        masterids (List[int]):

    Returns:
        Response[List[AccountRiskStatus]]
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
) -> Optional[List[AccountRiskStatus]]:
    """Retrieves all entities of AccountRiskStatus type related to multiple entities of Account type

    Args:
        masterids (List[int]):

    Returns:
        Response[List[AccountRiskStatus]]
    """

    return sync_detailed(
        client=client,
        masterids=masterids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    masterids: List[int],
) -> Response[List[AccountRiskStatus]]:
    """Retrieves all entities of AccountRiskStatus type related to multiple entities of Account type

    Args:
        masterids (List[int]):

    Returns:
        Response[List[AccountRiskStatus]]
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
) -> Optional[List[AccountRiskStatus]]:
    """Retrieves all entities of AccountRiskStatus type related to multiple entities of Account type

    Args:
        masterids (List[int]):

    Returns:
        Response[List[AccountRiskStatus]]
    """

    return (
        await asyncio_detailed(
            client=client,
            masterids=masterids,
        )
    ).parsed
