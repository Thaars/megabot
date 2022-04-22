import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.order_strategy_action import OrderStrategyAction
from ..models.order_strategy_status import OrderStrategyStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="OrderStrategy")


@attr.s(auto_attribs=True)
class OrderStrategy:
    """
    Attributes:
        account_id (int):
        timestamp (datetime.datetime):
        contract_id (int):
        order_strategy_type_id (int):
        action (OrderStrategyAction): Buy, Sell
        status (OrderStrategyStatus): ActiveStrategy, ExecutionFailed, ExecutionFinished, ExecutionInterrupted,
            InactiveStrategy, NotEnoughLiquidity, StoppedByUser
        id (Union[Unset, int]):
        initiator_id (Union[Unset, int]):
        params (Union[Unset, str]):
        uuid (Union[Unset, str]):
        failure_message (Union[Unset, str]):
        sender_id (Union[Unset, int]):
        custom_tag_50 (Union[Unset, str]):
        user_session_id (Union[Unset, int]):
    """

    account_id: int
    timestamp: datetime.datetime
    contract_id: int
    order_strategy_type_id: int
    action: OrderStrategyAction
    status: OrderStrategyStatus
    id: Union[Unset, int] = UNSET
    initiator_id: Union[Unset, int] = UNSET
    params: Union[Unset, str] = UNSET
    uuid: Union[Unset, str] = UNSET
    failure_message: Union[Unset, str] = UNSET
    sender_id: Union[Unset, int] = UNSET
    custom_tag_50: Union[Unset, str] = UNSET
    user_session_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_id = self.account_id
        timestamp = self.timestamp.isoformat()

        contract_id = self.contract_id
        order_strategy_type_id = self.order_strategy_type_id
        action = self.action.value

        status = self.status.value

        id = self.id
        initiator_id = self.initiator_id
        params = self.params
        uuid = self.uuid
        failure_message = self.failure_message
        sender_id = self.sender_id
        custom_tag_50 = self.custom_tag_50
        user_session_id = self.user_session_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountId": account_id,
                "timestamp": timestamp,
                "contractId": contract_id,
                "orderStrategyTypeId": order_strategy_type_id,
                "action": action,
                "status": status,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if initiator_id is not UNSET:
            field_dict["initiatorId"] = initiator_id
        if params is not UNSET:
            field_dict["params"] = params
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if failure_message is not UNSET:
            field_dict["failureMessage"] = failure_message
        if sender_id is not UNSET:
            field_dict["senderId"] = sender_id
        if custom_tag_50 is not UNSET:
            field_dict["customTag50"] = custom_tag_50
        if user_session_id is not UNSET:
            field_dict["userSessionId"] = user_session_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        account_id = d.pop("accountId")

        timestamp = isoparse(d.pop("timestamp"))

        contract_id = d.pop("contractId")

        order_strategy_type_id = d.pop("orderStrategyTypeId")

        action = OrderStrategyAction(d.pop("action"))

        status = OrderStrategyStatus(d.pop("status"))

        id = d.pop("id", UNSET)

        initiator_id = d.pop("initiatorId", UNSET)

        params = d.pop("params", UNSET)

        uuid = d.pop("uuid", UNSET)

        failure_message = d.pop("failureMessage", UNSET)

        sender_id = d.pop("senderId", UNSET)

        custom_tag_50 = d.pop("customTag50", UNSET)

        user_session_id = d.pop("userSessionId", UNSET)

        order_strategy = cls(
            account_id=account_id,
            timestamp=timestamp,
            contract_id=contract_id,
            order_strategy_type_id=order_strategy_type_id,
            action=action,
            status=status,
            id=id,
            initiator_id=initiator_id,
            params=params,
            uuid=uuid,
            failure_message=failure_message,
            sender_id=sender_id,
            custom_tag_50=custom_tag_50,
            user_session_id=user_session_id,
        )

        order_strategy.additional_properties = d
        return order_strategy

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
