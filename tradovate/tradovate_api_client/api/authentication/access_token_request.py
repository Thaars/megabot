from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.access_token_request import AccessTokenRequest
from ...models.access_token_response import AccessTokenResponse
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: AccessTokenRequest,
) -> Dict[str, Any]:
    url = "{}/auth/accesstokenrequest".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[AccessTokenResponse]:
    if response.status_code == 200:
        response_200 = AccessTokenResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[AccessTokenResponse]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: AccessTokenRequest,
) -> Response[AccessTokenResponse]:
    """### Request an access token using your user credentials and API Key.
    See the [Access](/#tag/Access) section for more details. For a comprehensive guide on how to acquire
    and use an access token in the JavaScript language, see out [JavaScript
    tutorial](https://github.com/tradovate/example-api-js) repository. For usage examples using the C#
    language, see the [C# example](https://github.com/tradovate/example-api-csharp-trading) repository.

    Args:
        json_body (AccessTokenRequest):

    Returns:
        Response[AccessTokenResponse]
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
    client: Client,
    json_body: AccessTokenRequest,
) -> Optional[AccessTokenResponse]:
    """### Request an access token using your user credentials and API Key.
    See the [Access](/#tag/Access) section for more details. For a comprehensive guide on how to acquire
    and use an access token in the JavaScript language, see out [JavaScript
    tutorial](https://github.com/tradovate/example-api-js) repository. For usage examples using the C#
    language, see the [C# example](https://github.com/tradovate/example-api-csharp-trading) repository.

    Args:
        json_body (AccessTokenRequest):

    Returns:
        Response[AccessTokenResponse]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: AccessTokenRequest,
) -> Response[AccessTokenResponse]:
    """### Request an access token using your user credentials and API Key.
    See the [Access](/#tag/Access) section for more details. For a comprehensive guide on how to acquire
    and use an access token in the JavaScript language, see out [JavaScript
    tutorial](https://github.com/tradovate/example-api-js) repository. For usage examples using the C#
    language, see the [C# example](https://github.com/tradovate/example-api-csharp-trading) repository.

    Args:
        json_body (AccessTokenRequest):

    Returns:
        Response[AccessTokenResponse]
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
    client: Client,
    json_body: AccessTokenRequest,
) -> Optional[AccessTokenResponse]:
    """### Request an access token using your user credentials and API Key.
    See the [Access](/#tag/Access) section for more details. For a comprehensive guide on how to acquire
    and use an access token in the JavaScript language, see out [JavaScript
    tutorial](https://github.com/tradovate/example-api-js) repository. For usage examples using the C#
    language, see the [C# example](https://github.com/tradovate/example-api-csharp-trading) repository.

    Args:
        json_body (AccessTokenRequest):

    Returns:
        Response[AccessTokenResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
