import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.order_action import OrderAction
from ..models.order_ord_status import OrderOrdStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="Order")


@attr.s(auto_attribs=True)
class Order:
    """
    Attributes:
        account_id (int):
        timestamp (datetime.datetime): Create Time
        action (OrderAction): Buy, Sell
        ord_status (OrderOrdStatus): Canceled, Completed, Expired, Filled, PendingCancel, PendingNew, PendingReplace,
            Rejected, Suspended, Unknown, Working
        admin (bool):
        id (Union[Unset, int]):
        contract_id (Union[Unset, int]):
        spread_definition_id (Union[Unset, int]):
        execution_provider_id (Union[Unset, int]):
        oco_id (Union[Unset, int]):
        parent_id (Union[Unset, int]):
        linked_id (Union[Unset, int]):
    """

    account_id: int
    timestamp: datetime.datetime
    action: OrderAction
    ord_status: OrderOrdStatus
    admin: bool
    id: Union[Unset, int] = UNSET
    contract_id: Union[Unset, int] = UNSET
    spread_definition_id: Union[Unset, int] = UNSET
    execution_provider_id: Union[Unset, int] = UNSET
    oco_id: Union[Unset, int] = UNSET
    parent_id: Union[Unset, int] = UNSET
    linked_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_id = self.account_id
        timestamp = self.timestamp.isoformat()

        action = self.action.value

        ord_status = self.ord_status.value

        admin = self.admin
        id = self.id
        contract_id = self.contract_id
        spread_definition_id = self.spread_definition_id
        execution_provider_id = self.execution_provider_id
        oco_id = self.oco_id
        parent_id = self.parent_id
        linked_id = self.linked_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountId": account_id,
                "timestamp": timestamp,
                "action": action,
                "ordStatus": ord_status,
                "admin": admin,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if contract_id is not UNSET:
            field_dict["contractId"] = contract_id
        if spread_definition_id is not UNSET:
            field_dict["spreadDefinitionId"] = spread_definition_id
        if execution_provider_id is not UNSET:
            field_dict["executionProviderId"] = execution_provider_id
        if oco_id is not UNSET:
            field_dict["ocoId"] = oco_id
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if linked_id is not UNSET:
            field_dict["linkedId"] = linked_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        account_id = d.pop("accountId")

        timestamp = isoparse(d.pop("timestamp"))

        action = OrderAction(d.pop("action"))

        ord_status = OrderOrdStatus(d.pop("ordStatus"))

        admin = d.pop("admin")

        id = d.pop("id", UNSET)

        contract_id = d.pop("contractId", UNSET)

        spread_definition_id = d.pop("spreadDefinitionId", UNSET)

        execution_provider_id = d.pop("executionProviderId", UNSET)

        oco_id = d.pop("ocoId", UNSET)

        parent_id = d.pop("parentId", UNSET)

        linked_id = d.pop("linkedId", UNSET)

        order = cls(
            account_id=account_id,
            timestamp=timestamp,
            action=action,
            ord_status=ord_status,
            admin=admin,
            id=id,
            contract_id=contract_id,
            spread_definition_id=spread_definition_id,
            execution_provider_id=execution_provider_id,
            oco_id=oco_id,
            parent_id=parent_id,
            linked_id=linked_id,
        )

        order.additional_properties = d
        return order

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
