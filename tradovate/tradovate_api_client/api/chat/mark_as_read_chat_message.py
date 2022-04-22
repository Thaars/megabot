from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.chat_message_response import ChatMessageResponse
from ...models.mark_as_read_chat_message import MarkAsReadChatMessage
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: MarkAsReadChatMessage,
) -> Dict[str, Any]:
    url = "{}/chat/markasreadchatmessage".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[ChatMessageResponse]:
    if response.status_code == 200:
        response_200 = ChatMessageResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ChatMessageResponse]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: MarkAsReadChatMessage,
) -> Response[ChatMessageResponse]:
    """### Marks a chat message as read.

    Args:
        json_body (MarkAsReadChatMessage):

    Returns:
        Response[ChatMessageResponse]
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
    json_body: MarkAsReadChatMessage,
) -> Optional[ChatMessageResponse]:
    """### Marks a chat message as read.

    Args:
        json_body (MarkAsReadChatMessage):

    Returns:
        Response[ChatMessageResponse]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: MarkAsReadChatMessage,
) -> Response[ChatMessageResponse]:
    """### Marks a chat message as read.

    Args:
        json_body (MarkAsReadChatMessage):

    Returns:
        Response[ChatMessageResponse]
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
    json_body: MarkAsReadChatMessage,
) -> Optional[ChatMessageResponse]:
    """### Marks a chat message as read.

    Args:
        json_body (MarkAsReadChatMessage):

    Returns:
        Response[ChatMessageResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
