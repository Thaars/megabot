from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="MarkReadAlertSignal")


@attr.s(auto_attribs=True)
class MarkReadAlertSignal:
    """
    Attributes:
        alert_id (int):
        alert_signal_id (int):
    """

    alert_id: int
    alert_signal_id: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        alert_id = self.alert_id
        alert_signal_id = self.alert_signal_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "alertId": alert_id,
                "alertSignalId": alert_signal_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        alert_id = d.pop("alertId")

        alert_signal_id = d.pop("alertSignalId")

        mark_read_alert_signal = cls(
            alert_id=alert_id,
            alert_signal_id=alert_signal_id,
        )

        mark_read_alert_signal.additional_properties = d
        return mark_read_alert_signal

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
