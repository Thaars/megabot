from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="InterruptOrderStrategy")


@attr.s(auto_attribs=True)
class InterruptOrderStrategy:
    """
    Attributes:
        order_strategy_id (int):
    """

    order_strategy_id: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        order_strategy_id = self.order_strategy_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "orderStrategyId": order_strategy_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        order_strategy_id = d.pop("orderStrategyId")

        interrupt_order_strategy = cls(
            order_strategy_id=order_strategy_id,
        )

        interrupt_order_strategy.additional_properties = d
        return interrupt_order_strategy

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
