from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="OAuthToken")


@attr.s(auto_attribs=True)
class OAuthToken:
    """
    Attributes:
        grant_type (str):
        code (str):
        redirect_uri (str):
        client_id (Union[Unset, str]):
        client_secret (Union[Unset, str]):
        http_auth (Union[Unset, str]):
    """

    grant_type: str
    code: str
    redirect_uri: str
    client_id: Union[Unset, str] = UNSET
    client_secret: Union[Unset, str] = UNSET
    http_auth: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        grant_type = self.grant_type
        code = self.code
        redirect_uri = self.redirect_uri
        client_id = self.client_id
        client_secret = self.client_secret
        http_auth = self.http_auth

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "grant_type": grant_type,
                "code": code,
                "redirect_uri": redirect_uri,
            }
        )
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if client_secret is not UNSET:
            field_dict["client_secret"] = client_secret
        if http_auth is not UNSET:
            field_dict["httpAuth"] = http_auth

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        grant_type = d.pop("grant_type")

        code = d.pop("code")

        redirect_uri = d.pop("redirect_uri")

        client_id = d.pop("client_id", UNSET)

        client_secret = d.pop("client_secret", UNSET)

        http_auth = d.pop("httpAuth", UNSET)

        o_auth_token = cls(
            grant_type=grant_type,
            code=code,
            redirect_uri=redirect_uri,
            client_id=client_id,
            client_secret=client_secret,
            http_auth=http_auth,
        )

        o_auth_token.additional_properties = d
        return o_auth_token

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
