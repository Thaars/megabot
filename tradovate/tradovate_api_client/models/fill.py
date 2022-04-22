import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.fill_action import FillAction
from ..models.trade_date import TradeDate
from ..types import UNSET, Unset

T = TypeVar("T", bound="Fill")


@attr.s(auto_attribs=True)
class Fill:
    """
    Attributes:
        order_id (int):
        contract_id (int):
        timestamp (datetime.datetime):
        trade_date (TradeDate):
        action (FillAction): Buy, Sell
        qty (int):
        price (float):
        active (bool):
        finally_paired (int):
        id (Union[Unset, int]):
    """

    order_id: int
    contract_id: int
    timestamp: datetime.datetime
    trade_date: TradeDate
    action: FillAction
    qty: int
    price: float
    active: bool
    finally_paired: int
    id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        order_id = self.order_id
        contract_id = self.contract_id
        timestamp = self.timestamp.isoformat()

        trade_date = self.trade_date.to_dict()

        action = self.action.value

        qty = self.qty
        price = self.price
        active = self.active
        finally_paired = self.finally_paired
        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "orderId": order_id,
                "contractId": contract_id,
                "timestamp": timestamp,
                "tradeDate": trade_date,
                "action": action,
                "qty": qty,
                "price": price,
                "active": active,
                "finallyPaired": finally_paired,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        order_id = d.pop("orderId")

        contract_id = d.pop("contractId")

        timestamp = isoparse(d.pop("timestamp"))

        trade_date = TradeDate.from_dict(d.pop("tradeDate"))

        action = FillAction(d.pop("action"))

        qty = d.pop("qty")

        price = d.pop("price")

        active = d.pop("active")

        finally_paired = d.pop("finallyPaired")

        id = d.pop("id", UNSET)

        fill = cls(
            order_id=order_id,
            contract_id=contract_id,
            timestamp=timestamp,
            trade_date=trade_date,
            action=action,
            qty=qty,
            price=price,
            active=active,
            finally_paired=finally_paired,
            id=id,
        )

        fill.additional_properties = d
        return fill

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
