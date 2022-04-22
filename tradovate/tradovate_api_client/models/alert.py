import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.alert_status import AlertStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="Alert")


@attr.s(auto_attribs=True)
class Alert:
    """
    Attributes:
        timestamp (datetime.datetime):
        user_id (int):
        status (AlertStatus): Active, Expired, Failed, Inactive, TriggeredOut
        expression (str):
        id (Union[Unset, int]):
        valid_until (Union[Unset, datetime.datetime]):
        trigger_limits (Union[Unset, int]):
        triggered_counter (Union[Unset, int]):
        failure (Union[Unset, str]):
        message (Union[Unset, str]):
    """

    timestamp: datetime.datetime
    user_id: int
    status: AlertStatus
    expression: str
    id: Union[Unset, int] = UNSET
    valid_until: Union[Unset, datetime.datetime] = UNSET
    trigger_limits: Union[Unset, int] = UNSET
    triggered_counter: Union[Unset, int] = UNSET
    failure: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        timestamp = self.timestamp.isoformat()

        user_id = self.user_id
        status = self.status.value

        expression = self.expression
        id = self.id
        valid_until: Union[Unset, str] = UNSET
        if not isinstance(self.valid_until, Unset):
            valid_until = self.valid_until.isoformat()

        trigger_limits = self.trigger_limits
        triggered_counter = self.triggered_counter
        failure = self.failure
        message = self.message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
                "userId": user_id,
                "status": status,
                "expression": expression,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if valid_until is not UNSET:
            field_dict["validUntil"] = valid_until
        if trigger_limits is not UNSET:
            field_dict["triggerLimits"] = trigger_limits
        if triggered_counter is not UNSET:
            field_dict["triggeredCounter"] = triggered_counter
        if failure is not UNSET:
            field_dict["failure"] = failure
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        timestamp = isoparse(d.pop("timestamp"))

        user_id = d.pop("userId")

        status = AlertStatus(d.pop("status"))

        expression = d.pop("expression")

        id = d.pop("id", UNSET)

        _valid_until = d.pop("validUntil", UNSET)
        valid_until: Union[Unset, datetime.datetime]
        if isinstance(_valid_until, Unset):
            valid_until = UNSET
        else:
            valid_until = isoparse(_valid_until)

        trigger_limits = d.pop("triggerLimits", UNSET)

        triggered_counter = d.pop("triggeredCounter", UNSET)

        failure = d.pop("failure", UNSET)

        message = d.pop("message", UNSET)

        alert = cls(
            timestamp=timestamp,
            user_id=user_id,
            status=status,
            expression=expression,
            id=id,
            valid_until=valid_until,
            trigger_limits=trigger_limits,
            triggered_counter=triggered_counter,
            failure=failure,
            message=message,
        )

        alert.additional_properties = d
        return alert

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
