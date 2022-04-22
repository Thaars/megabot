from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.alert import Alert
from ..types import UNSET, Unset

T = TypeVar("T", bound="AlertResponse")


@attr.s(auto_attribs=True)
class AlertResponse:
    """
    Attributes:
        error_text (Union[Unset, str]): Non-empty if the request failed
        alert (Union[Unset, Alert]):
    """

    error_text: Union[Unset, str] = UNSET
    alert: Union[Unset, Alert] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        error_text = self.error_text
        alert: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.alert, Unset):
            alert = self.alert.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error_text is not UNSET:
            field_dict["errorText"] = error_text
        if alert is not UNSET:
            field_dict["alert"] = alert

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        error_text = d.pop("errorText", UNSET)

        _alert = d.pop("alert", UNSET)
        alert: Union[Unset, Alert]
        if isinstance(_alert, Unset):
            alert = UNSET
        else:
            alert = Alert.from_dict(_alert)

        alert_response = cls(
            error_text=error_text,
            alert=alert,
        )

        alert_response.additional_properties = d
        return alert_response

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
