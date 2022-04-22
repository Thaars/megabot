import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.trade_date import TradeDate
from ..types import UNSET, Unset

T = TypeVar("T", bound="Position")


@attr.s(auto_attribs=True)
class Position:
    """
    Attributes:
        account_id (int):
        contract_id (int):
        timestamp (datetime.datetime):
        trade_date (TradeDate):
        net_pos (int):
        bought (int):
        bought_value (float):
        sold (int):
        sold_value (float):
        prev_pos (int):
        id (Union[Unset, int]):
        net_price (Union[Unset, float]):
        prev_price (Union[Unset, float]):
    """

    account_id: int
    contract_id: int
    timestamp: datetime.datetime
    trade_date: TradeDate
    net_pos: int
    bought: int
    bought_value: float
    sold: int
    sold_value: float
    prev_pos: int
    id: Union[Unset, int] = UNSET
    net_price: Union[Unset, float] = UNSET
    prev_price: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_id = self.account_id
        contract_id = self.contract_id
        timestamp = self.timestamp.isoformat()

        trade_date = self.trade_date.to_dict()

        net_pos = self.net_pos
        bought = self.bought
        bought_value = self.bought_value
        sold = self.sold
        sold_value = self.sold_value
        prev_pos = self.prev_pos
        id = self.id
        net_price = self.net_price
        prev_price = self.prev_price

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountId": account_id,
                "contractId": contract_id,
                "timestamp": timestamp,
                "tradeDate": trade_date,
                "netPos": net_pos,
                "bought": bought,
                "boughtValue": bought_value,
                "sold": sold,
                "soldValue": sold_value,
                "prevPos": prev_pos,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if net_price is not UNSET:
            field_dict["netPrice"] = net_price
        if prev_price is not UNSET:
            field_dict["prevPrice"] = prev_price

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        account_id = d.pop("accountId")

        contract_id = d.pop("contractId")

        timestamp = isoparse(d.pop("timestamp"))

        trade_date = TradeDate.from_dict(d.pop("tradeDate"))

        net_pos = d.pop("netPos")

        bought = d.pop("bought")

        bought_value = d.pop("boughtValue")

        sold = d.pop("sold")

        sold_value = d.pop("soldValue")

        prev_pos = d.pop("prevPos")

        id = d.pop("id", UNSET)

        net_price = d.pop("netPrice", UNSET)

        prev_price = d.pop("prevPrice", UNSET)

        position = cls(
            account_id=account_id,
            contract_id=contract_id,
            timestamp=timestamp,
            trade_date=trade_date,
            net_pos=net_pos,
            bought=bought,
            bought_value=bought_value,
            sold=sold,
            sold_value=sold_value,
            prev_pos=prev_pos,
            id=id,
            net_price=net_price,
            prev_price=prev_price,
        )

        position.additional_properties = d
        return position

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
