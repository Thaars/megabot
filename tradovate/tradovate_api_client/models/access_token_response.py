import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.access_token_response_user_status import AccessTokenResponseUserStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="AccessTokenResponse")


@attr.s(auto_attribs=True)
class AccessTokenResponse:
    """
    Attributes:
        error_text (Union[Unset, str]): Non-empty if the request failed
        access_token (Union[Unset, str]):
        expiration_time (Union[Unset, datetime.datetime]):
        password_expiration_time (Union[Unset, datetime.datetime]):
        user_status (Union[Unset, AccessTokenResponseUserStatus]): Active, Closed, Initiated, TemporaryLocked,
            UnconfirmedEmail
        user_id (Union[Unset, int]):
        name (Union[Unset, str]):
        has_live (Union[Unset, bool]):
    """

    error_text: Union[Unset, str] = UNSET
    access_token: Union[Unset, str] = UNSET
    expiration_time: Union[Unset, datetime.datetime] = UNSET
    password_expiration_time: Union[Unset, datetime.datetime] = UNSET
    user_status: Union[Unset, AccessTokenResponseUserStatus] = UNSET
    user_id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    has_live: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        error_text = self.error_text
        access_token = self.access_token
        expiration_time: Union[Unset, str] = UNSET
        if not isinstance(self.expiration_time, Unset):
            expiration_time = self.expiration_time.isoformat()

        password_expiration_time: Union[Unset, str] = UNSET
        if not isinstance(self.password_expiration_time, Unset):
            password_expiration_time = self.password_expiration_time.isoformat()

        user_status: Union[Unset, str] = UNSET
        if not isinstance(self.user_status, Unset):
            user_status = self.user_status.value

        user_id = self.user_id
        name = self.name
        has_live = self.has_live

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error_text is not UNSET:
            field_dict["errorText"] = error_text
        if access_token is not UNSET:
            field_dict["accessToken"] = access_token
        if expiration_time is not UNSET:
            field_dict["expirationTime"] = expiration_time
        if password_expiration_time is not UNSET:
            field_dict["passwordExpirationTime"] = password_expiration_time
        if user_status is not UNSET:
            field_dict["userStatus"] = user_status
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if name is not UNSET:
            field_dict["name"] = name
        if has_live is not UNSET:
            field_dict["hasLive"] = has_live

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        error_text = d.pop("errorText", UNSET)

        access_token = d.pop("accessToken", UNSET)

        _expiration_time = d.pop("expirationTime", UNSET)
        expiration_time: Union[Unset, datetime.datetime]
        if isinstance(_expiration_time, Unset):
            expiration_time = UNSET
        else:
            expiration_time = isoparse(_expiration_time)

        _password_expiration_time = d.pop("passwordExpirationTime", UNSET)
        password_expiration_time: Union[Unset, datetime.datetime]
        if isinstance(_password_expiration_time, Unset):
            password_expiration_time = UNSET
        else:
            password_expiration_time = isoparse(_password_expiration_time)

        _user_status = d.pop("userStatus", UNSET)
        user_status: Union[Unset, AccessTokenResponseUserStatus]
        if isinstance(_user_status, Unset):
            user_status = UNSET
        else:
            user_status = AccessTokenResponseUserStatus(_user_status)

        user_id = d.pop("userId", UNSET)

        name = d.pop("name", UNSET)

        has_live = d.pop("hasLive", UNSET)

        access_token_response = cls(
            error_text=error_text,
            access_token=access_token,
            expiration_time=expiration_time,
            password_expiration_time=password_expiration_time,
            user_status=user_status,
            user_id=user_id,
            name=name,
            has_live=has_live,
        )

        access_token_response.additional_properties = d
        return access_token_response

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
