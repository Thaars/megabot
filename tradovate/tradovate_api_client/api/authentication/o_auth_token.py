from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.o_auth_token import OAuthToken
from ...models.o_auth_token_response import OAuthTokenResponse
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: OAuthToken,
) -> Dict[str, Any]:
    url = "{}/auth/oauthtoken".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[OAuthTokenResponse]:
    if response.status_code == 200:
        response_200 = OAuthTokenResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[OAuthTokenResponse]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: OAuthToken,
) -> Response[OAuthTokenResponse]:
    """### Used to exchange your OAuth code for an access token.
    Using the OAuth authorization delegation flow, we can send a request to verify that our users are
    who they say they are. For more information on using OAuth with the Tradovate API see our [OAuth
    JavaScript tutorial](https://github.com/tradovate/example-api-oauth).

    Args:
        json_body (OAuthToken):

    Returns:
        Response[OAuthTokenResponse]
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
    json_body: OAuthToken,
) -> Optional[OAuthTokenResponse]:
    """### Used to exchange your OAuth code for an access token.
    Using the OAuth authorization delegation flow, we can send a request to verify that our users are
    who they say they are. For more information on using OAuth with the Tradovate API see our [OAuth
    JavaScript tutorial](https://github.com/tradovate/example-api-oauth).

    Args:
        json_body (OAuthToken):

    Returns:
        Response[OAuthTokenResponse]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: OAuthToken,
) -> Response[OAuthTokenResponse]:
    """### Used to exchange your OAuth code for an access token.
    Using the OAuth authorization delegation flow, we can send a request to verify that our users are
    who they say they are. For more information on using OAuth with the Tradovate API see our [OAuth
    JavaScript tutorial](https://github.com/tradovate/example-api-oauth).

    Args:
        json_body (OAuthToken):

    Returns:
        Response[OAuthTokenResponse]
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
    json_body: OAuthToken,
) -> Optional[OAuthTokenResponse]:
    """### Used to exchange your OAuth code for an access token.
    Using the OAuth authorization delegation flow, we can send a request to verify that our users are
    who they say they are. For more information on using OAuth with the Tradovate API see our [OAuth
    JavaScript tutorial](https://github.com/tradovate/example-api-oauth).

    Args:
        json_body (OAuthToken):

    Returns:
        Response[OAuthTokenResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
