from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.sign_up_organization_member import SignUpOrganizationMember
from ...models.sign_up_response import SignUpResponse
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: SignUpOrganizationMember,
) -> Dict[str, Any]:
    url = "{}/user/signuporganizationmember".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[SignUpResponse]:
    if response.status_code == 200:
        response_200 = SignUpResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[SignUpResponse]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: SignUpOrganizationMember,
) -> Response[SignUpResponse]:
    """### Used by B2B partners to create users for their own organizations.

    Args:
        json_body (SignUpOrganizationMember):

    Returns:
        Response[SignUpResponse]
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
    json_body: SignUpOrganizationMember,
) -> Optional[SignUpResponse]:
    """### Used by B2B partners to create users for their own organizations.

    Args:
        json_body (SignUpOrganizationMember):

    Returns:
        Response[SignUpResponse]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: SignUpOrganizationMember,
) -> Response[SignUpResponse]:
    """### Used by B2B partners to create users for their own organizations.

    Args:
        json_body (SignUpOrganizationMember):

    Returns:
        Response[SignUpResponse]
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
    json_body: SignUpOrganizationMember,
) -> Optional[SignUpResponse]:
    """### Used by B2B partners to create users for their own organizations.

    Args:
        json_body (SignUpOrganizationMember):

    Returns:
        Response[SignUpResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
