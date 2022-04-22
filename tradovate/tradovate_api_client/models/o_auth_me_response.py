from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="OAuthMeResponse")


@attr.s(auto_attribs=True)
class OAuthMeResponse:
    """
    Attributes:
        error_text (Union[Unset, str]): Non-empty if the request failed
        user_id (Union[Unset, int]):
        name (Union[Unset, str]):
        full_name (Union[Unset, str]):
        email (Union[Unset, str]):
        email_verified (Union[Unset, bool]):
        is_trial (Union[Unset, bool]):
    """

    error_text: Union[Unset, str] = UNSET
    user_id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    full_name: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    email_verified: Union[Unset, bool] = UNSET
    is_trial: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        error_text = self.error_text
        user_id = self.user_id
        name = self.name
        full_name = self.full_name
        email = self.email
        email_verified = self.email_verified
        is_trial = self.is_trial

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error_text is not UNSET:
            field_dict["errorText"] = error_text
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if name is not UNSET:
            field_dict["name"] = name
        if full_name is not UNSET:
            field_dict["fullName"] = full_name
        if email is not UNSET:
            field_dict["email"] = email
        if email_verified is not UNSET:
            field_dict["emailVerified"] = email_verified
        if is_trial is not UNSET:
            field_dict["isTrial"] = is_trial

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        error_text = d.pop("errorText", UNSET)

        user_id = d.pop("userId", UNSET)

        name = d.pop("name", UNSET)

        full_name = d.pop("fullName", UNSET)

        email = d.pop("email", UNSET)

        email_verified = d.pop("emailVerified", UNSET)

        is_trial = d.pop("isTrial", UNSET)

        o_auth_me_response = cls(
            error_text=error_text,
            user_id=user_id,
            name=name,
            full_name=full_name,
            email=email,
            email_verified=email_verified,
            is_trial=is_trial,
        )

        o_auth_me_response.additional_properties = d
        return o_auth_me_response

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
