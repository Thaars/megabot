from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.check_replay_session import CheckReplaySession
from ...models.check_replay_session_response import CheckReplaySessionResponse
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: CheckReplaySession,
) -> Dict[str, Any]:
    url = "{}/replay/checkreplaysession".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[CheckReplaySessionResponse]:
    if response.status_code == 200:
        response_200 = CheckReplaySessionResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[CheckReplaySessionResponse]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: CheckReplaySession,
) -> Response[CheckReplaySessionResponse]:
    """### Before beginning a Market Replay session, checks to see if the given timeframe is within the
    scope of the user's entitlements.

    Args:
        json_body (CheckReplaySession):

    Returns:
        Response[CheckReplaySessionResponse]
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
    json_body: CheckReplaySession,
) -> Optional[CheckReplaySessionResponse]:
    """### Before beginning a Market Replay session, checks to see if the given timeframe is within the
    scope of the user's entitlements.

    Args:
        json_body (CheckReplaySession):

    Returns:
        Response[CheckReplaySessionResponse]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: CheckReplaySession,
) -> Response[CheckReplaySessionResponse]:
    """### Before beginning a Market Replay session, checks to see if the given timeframe is within the
    scope of the user's entitlements.

    Args:
        json_body (CheckReplaySession):

    Returns:
        Response[CheckReplaySessionResponse]
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
    json_body: CheckReplaySession,
) -> Optional[CheckReplaySessionResponse]:
    """### Before beginning a Market Replay session, checks to see if the given timeframe is within the
    scope of the user's entitlements.

    Args:
        json_body (CheckReplaySession):

    Returns:
        Response[CheckReplaySessionResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
