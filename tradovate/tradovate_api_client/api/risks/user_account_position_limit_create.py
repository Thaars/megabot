from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.user_account_position_limit import UserAccountPositionLimit
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: UserAccountPositionLimit,
) -> Dict[str, Any]:
    url = "{}/userAccountPositionLimit/create".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[UserAccountPositionLimit]:
    if response.status_code == 200:
        response_200 = UserAccountPositionLimit.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[UserAccountPositionLimit]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: UserAccountPositionLimit,
) -> Response[UserAccountPositionLimit]:
    """Creates a new entity of UserAccountPositionLimit

    Args:
        json_body (UserAccountPositionLimit):

    Returns:
        Response[UserAccountPositionLimit]
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
    json_body: UserAccountPositionLimit,
) -> Optional[UserAccountPositionLimit]:
    """Creates a new entity of UserAccountPositionLimit

    Args:
        json_body (UserAccountPositionLimit):

    Returns:
        Response[UserAccountPositionLimit]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: UserAccountPositionLimit,
) -> Response[UserAccountPositionLimit]:
    """Creates a new entity of UserAccountPositionLimit

    Args:
        json_body (UserAccountPositionLimit):

    Returns:
        Response[UserAccountPositionLimit]
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
    json_body: UserAccountPositionLimit,
) -> Optional[UserAccountPositionLimit]:
    """Creates a new entity of UserAccountPositionLimit

    Args:
        json_body (UserAccountPositionLimit):

    Returns:
        Response[UserAccountPositionLimit]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
