import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateAlert")


@attr.s(auto_attribs=True)
class CreateAlert:
    """
    Attributes:
        expression (str):
        valid_until (Union[Unset, datetime.datetime]):
        trigger_limits (Union[Unset, int]):
        message (Union[Unset, str]):
    """

    expression: str
    valid_until: Union[Unset, datetime.datetime] = UNSET
    trigger_limits: Union[Unset, int] = UNSET
    message: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        expression = self.expression
        valid_until: Union[Unset, str] = UNSET
        if not isinstance(self.valid_until, Unset):
            valid_until = self.valid_until.isoformat()

        trigger_limits = self.trigger_limits
        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "expression": expression,
            }
        )
        if valid_until is not UNSET:
            field_dict["validUntil"] = valid_until
        if trigger_limits is not UNSET:
            field_dict["triggerLimits"] = trigger_limits
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        expression = d.pop("expression")

        _valid_until = d.pop("validUntil", UNSET)
        valid_until: Union[Unset, datetime.datetime]
        if isinstance(_valid_until, Unset):
            valid_until = UNSET
        else:
            valid_until = isoparse(_valid_until)

        trigger_limits = d.pop("triggerLimits", UNSET)

        message = d.pop("message", UNSET)

        create_alert = cls(
            expression=expression,
            valid_until=valid_until,
            trigger_limits=trigger_limits,
            message=message,
        )

        create_alert.additional_properties = d
        return create_alert

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
