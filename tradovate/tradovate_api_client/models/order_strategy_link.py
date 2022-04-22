from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrderStrategyLink")


@attr.s(auto_attribs=True)
class OrderStrategyLink:
    """
    Attributes:
        order_strategy_id (int):
        order_id (int):
        label (str):
        id (Union[Unset, int]):
    """

    order_strategy_id: int
    order_id: int
    label: str
    id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        order_strategy_id = self.order_strategy_id
        order_id = self.order_id
        label = self.label
        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "orderStrategyId": order_strategy_id,
                "orderId": order_id,
                "label": label,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        order_strategy_id = d.pop("orderStrategyId")

        order_id = d.pop("orderId")

        label = d.pop("label")

        id = d.pop("id", UNSET)

        order_strategy_link = cls(
            order_strategy_id=order_strategy_id,
            order_id=order_id,
            label=label,
            id=id,
        )

        order_strategy_link.additional_properties = d
        return order_strategy_link

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
