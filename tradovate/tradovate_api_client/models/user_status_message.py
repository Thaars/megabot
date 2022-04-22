from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.user_status_message_status import UserStatusMessageStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserStatusMessage")


@attr.s(auto_attribs=True)
class UserStatusMessage:
    """
    Attributes:
        error_text (Union[Unset, str]): Non-empty if the request failed
        status (Union[Unset, UserStatusMessageStatus]): Active, Closed, Initiated, TemporaryLocked, UnconfirmedEmail
    """

    error_text: Union[Unset, str] = UNSET
    status: Union[Unset, UserStatusMessageStatus] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        error_text = self.error_text
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error_text is not UNSET:
            field_dict["errorText"] = error_text
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        error_text = d.pop("errorText", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, UserStatusMessageStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = UserStatusMessageStatus(_status)

        user_status_message = cls(
            error_text=error_text,
            status=status,
        )

        user_status_message.additional_properties = d
        return user_status_message

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
