from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.change_speed import ChangeSpeed
from ...models.simple_response import SimpleResponse
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: ChangeSpeed,
) -> Dict[str, Any]:
    url = "{}/replay/changespeed".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[SimpleResponse]:
    if response.status_code == 200:
        response_200 = SimpleResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[SimpleResponse]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: ChangeSpeed,
) -> Response[SimpleResponse]:
    """### Change the playback speed of a Market Replay session.

    Args:
        json_body (ChangeSpeed):

    Returns:
        Response[SimpleResponse]
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
    json_body: ChangeSpeed,
) -> Optional[SimpleResponse]:
    """### Change the playback speed of a Market Replay session.

    Args:
        json_body (ChangeSpeed):

    Returns:
        Response[SimpleResponse]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: ChangeSpeed,
) -> Response[SimpleResponse]:
    """### Change the playback speed of a Market Replay session.

    Args:
        json_body (ChangeSpeed):

    Returns:
        Response[SimpleResponse]
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
    json_body: ChangeSpeed,
) -> Optional[SimpleResponse]:
    """### Change the playback speed of a Market Replay session.

    Args:
        json_body (ChangeSpeed):

    Returns:
        Response[SimpleResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed