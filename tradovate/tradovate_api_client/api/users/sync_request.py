from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.sync_message import SyncMessage
from ...models.sync_request import SyncRequest
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: SyncRequest,
) -> Dict[str, Any]:
    url = "{}/user/syncrequest".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[SyncMessage]:
    if response.status_code == 200:
        response_200 = SyncMessage.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[SyncMessage]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: SyncRequest,
) -> Response[SyncMessage]:
    """### Used with WebSocket protocol. Returns all data associated with the user.
    This endpoint is essential for efficient use of the WebSocket API. See
    [WebSockets](/#tag/#WebSockets) for more details, or view our WebSockets
    [JavaScript](https://github.com/tradovate/example-api-js) or
    [C#](https://github.com/tradovate/example-api-csharp-trading) tutorials.

    Args:
        json_body (SyncRequest):

    Returns:
        Response[SyncMessage]
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
    json_body: SyncRequest,
) -> Optional[SyncMessage]:
    """### Used with WebSocket protocol. Returns all data associated with the user.
    This endpoint is essential for efficient use of the WebSocket API. See
    [WebSockets](/#tag/#WebSockets) for more details, or view our WebSockets
    [JavaScript](https://github.com/tradovate/example-api-js) or
    [C#](https://github.com/tradovate/example-api-csharp-trading) tutorials.

    Args:
        json_body (SyncRequest):

    Returns:
        Response[SyncMessage]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: SyncRequest,
) -> Response[SyncMessage]:
    """### Used with WebSocket protocol. Returns all data associated with the user.
    This endpoint is essential for efficient use of the WebSocket API. See
    [WebSockets](/#tag/#WebSockets) for more details, or view our WebSockets
    [JavaScript](https://github.com/tradovate/example-api-js) or
    [C#](https://github.com/tradovate/example-api-csharp-trading) tutorials.

    Args:
        json_body (SyncRequest):

    Returns:
        Response[SyncMessage]
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
    json_body: SyncRequest,
) -> Optional[SyncMessage]:
    """### Used with WebSocket protocol. Returns all data associated with the user.
    This endpoint is essential for efficient use of the WebSocket API. See
    [WebSockets](/#tag/#WebSockets) for more details, or view our WebSockets
    [JavaScript](https://github.com/tradovate/example-api-js) or
    [C#](https://github.com/tradovate/example-api-csharp-trading) tutorials.

    Args:
        json_body (SyncRequest):

    Returns:
        Response[SyncMessage]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
