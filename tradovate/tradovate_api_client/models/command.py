import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.command_command_status import CommandCommandStatus
from ..models.command_command_type import CommandCommandType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Command")


@attr.s(auto_attribs=True)
class Command:
    """
    Attributes:
        order_id (int):
        timestamp (datetime.datetime):
        command_type (CommandCommandType): Cancel, Modify, New
        command_status (CommandCommandStatus): AtExecution, ExecutionRejected, ExecutionStopped, ExecutionSuspended,
            OnHold, Pending, PendingExecution, Replaced, RiskPassed, RiskRejected
        id (Union[Unset, int]):
        cl_ord_id (Union[Unset, str]):
        sender_id (Union[Unset, int]):
        user_session_id (Union[Unset, int]):
        activation_time (Union[Unset, datetime.datetime]):
        custom_tag_50 (Union[Unset, str]):
        is_automated (Union[Unset, bool]):
    """

    order_id: int
    timestamp: datetime.datetime
    command_type: CommandCommandType
    command_status: CommandCommandStatus
    id: Union[Unset, int] = UNSET
    cl_ord_id: Union[Unset, str] = UNSET
    sender_id: Union[Unset, int] = UNSET
    user_session_id: Union[Unset, int] = UNSET
    activation_time: Union[Unset, datetime.datetime] = UNSET
    custom_tag_50: Union[Unset, str] = UNSET
    is_automated: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        order_id = self.order_id
        timestamp = self.timestamp.isoformat()

        command_type = self.command_type.value

        command_status = self.command_status.value

        id = self.id
        cl_ord_id = self.cl_ord_id
        sender_id = self.sender_id
        user_session_id = self.user_session_id
        activation_time: Union[Unset, str] = UNSET
        if not isinstance(self.activation_time, Unset):
            activation_time = self.activation_time.isoformat()

        custom_tag_50 = self.custom_tag_50
        is_automated = self.is_automated

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "orderId": order_id,
                "timestamp": timestamp,
                "commandType": command_type,
                "commandStatus": command_status,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if cl_ord_id is not UNSET:
            field_dict["clOrdId"] = cl_ord_id
        if sender_id is not UNSET:
            field_dict["senderId"] = sender_id
        if user_session_id is not UNSET:
            field_dict["userSessionId"] = user_session_id
        if activation_time is not UNSET:
            field_dict["activationTime"] = activation_time
        if custom_tag_50 is not UNSET:
            field_dict["customTag50"] = custom_tag_50
        if is_automated is not UNSET:
            field_dict["isAutomated"] = is_automated

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        order_id = d.pop("orderId")

        timestamp = isoparse(d.pop("timestamp"))

        command_type = CommandCommandType(d.pop("commandType"))

        command_status = CommandCommandStatus(d.pop("commandStatus"))

        id = d.pop("id", UNSET)

        cl_ord_id = d.pop("clOrdId", UNSET)

        sender_id = d.pop("senderId", UNSET)

        user_session_id = d.pop("userSessionId", UNSET)

        _activation_time = d.pop("activationTime", UNSET)
        activation_time: Union[Unset, datetime.datetime]
        if isinstance(_activation_time, Unset):
            activation_time = UNSET
        else:
            activation_time = isoparse(_activation_time)

        custom_tag_50 = d.pop("customTag50", UNSET)

        is_automated = d.pop("isAutomated", UNSET)

        command = cls(
            order_id=order_id,
            timestamp=timestamp,
            command_type=command_type,
            command_status=command_status,
            id=id,
            cl_ord_id=cl_ord_id,
            sender_id=sender_id,
            user_session_id=user_session_id,
            activation_time=activation_time,
            custom_tag_50=custom_tag_50,
            is_automated=is_automated,
        )

        command.additional_properties = d
        return command

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
