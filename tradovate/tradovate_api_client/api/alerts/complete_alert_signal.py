from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.admin_alert_signal_response import AdminAlertSignalResponse
from ...models.complete_alert_signal import CompleteAlertSignal
from ...types import Response


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    json_body: CompleteAlertSignal,
) -> Dict[str, Any]:
    url = "{}/adminAlertSignal/completealertsignal".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[AdminAlertSignalResponse]:
    if response.status_code == 200:
        response_200 = AdminAlertSignalResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[AdminAlertSignalResponse]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    json_body: CompleteAlertSignal,
) -> Response[AdminAlertSignalResponse]:
    """### Silences an \"incomplete\" notification.
    An \"Incomplete\" notification is one that has not yet been viewed by a user. Once a user has
    interacted with a notification it should be \"completed\".

    Args:
        json_body (CompleteAlertSignal):

    Returns:
        Response[AdminAlertSignalResponse]
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
    json_body: CompleteAlertSignal,
) -> Optional[AdminAlertSignalResponse]:
    """### Silences an \"incomplete\" notification.
    An \"Incomplete\" notification is one that has not yet been viewed by a user. Once a user has
    interacted with a notification it should be \"completed\".

    Args:
        json_body (CompleteAlertSignal):

    Returns:
        Response[AdminAlertSignalResponse]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    json_body: CompleteAlertSignal,
) -> Response[AdminAlertSignalResponse]:
    """### Silences an \"incomplete\" notification.
    An \"Incomplete\" notification is one that has not yet been viewed by a user. Once a user has
    interacted with a notification it should be \"completed\".

    Args:
        json_body (CompleteAlertSignal):

    Returns:
        Response[AdminAlertSignalResponse]
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
    json_body: CompleteAlertSignal,
) -> Optional[AdminAlertSignalResponse]:
    """### Silences an \"incomplete\" notification.
    An \"Incomplete\" notification is one that has not yet been viewed by a user. Once a user has
    interacted with a notification it should be \"completed\".

    Args:
        json_body (CompleteAlertSignal):

    Returns:
        Response[AdminAlertSignalResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
