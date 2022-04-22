from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="FillPair")


@attr.s(auto_attribs=True)
class FillPair:
    """
    Attributes:
        position_id (int):
        buy_fill_id (int):
        sell_fill_id (int):
        qty (int):
        buy_price (float):
        sell_price (float):
        active (bool):
        id (Union[Unset, int]):
    """

    position_id: int
    buy_fill_id: int
    sell_fill_id: int
    qty: int
    buy_price: float
    sell_price: float
    active: bool
    id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        position_id = self.position_id
        buy_fill_id = self.buy_fill_id
        sell_fill_id = self.sell_fill_id
        qty = self.qty
        buy_price = self.buy_price
        sell_price = self.sell_price
        active = self.active
        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "positionId": position_id,
                "buyFillId": buy_fill_id,
                "sellFillId": sell_fill_id,
                "qty": qty,
                "buyPrice": buy_price,
                "sellPrice": sell_price,
                "active": active,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        position_id = d.pop("positionId")

        buy_fill_id = d.pop("buyFillId")

        sell_fill_id = d.pop("sellFillId")

        qty = d.pop("qty")

        buy_price = d.pop("buyPrice")

        sell_price = d.pop("sellPrice")

        active = d.pop("active")

        id = d.pop("id", UNSET)

        fill_pair = cls(
            position_id=position_id,
            buy_fill_id=buy_fill_id,
            sell_fill_id=sell_fill_id,
            qty=qty,
            buy_price=buy_price,
            sell_price=sell_price,
            active=active,
            id=id,
        )

        fill_pair.additional_properties = d
        return fill_pair

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
