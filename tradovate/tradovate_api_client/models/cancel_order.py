import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CancelOrder")


@attr.s(auto_attribs=True)
class CancelOrder:
    """
    Attributes:
        order_id (int):
        cl_ord_id (Union[Unset, str]):
        activation_time (Union[Unset, datetime.datetime]):
        custom_tag_50 (Union[Unset, str]):
        is_automated (Union[Unset, bool]):
    """

    order_id: int
    cl_ord_id: Union[Unset, str] = UNSET
    activation_time: Union[Unset, datetime.datetime] = UNSET
    custom_tag_50: Union[Unset, str] = UNSET
    is_automated: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        order_id = self.order_id
        cl_ord_id = self.cl_ord_id
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
            }
        )
        if cl_ord_id is not UNSET:
            field_dict["clOrdId"] = cl_ord_id
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

        cl_ord_id = d.pop("clOrdId", UNSET)

        _activation_time = d.pop("activationTime", UNSET)
        activation_time: Union[Unset, datetime.datetime]
        if isinstance(_activation_time, Unset):
            activation_time = UNSET
        else:
            activation_time = isoparse(_activation_time)

        custom_tag_50 = d.pop("customTag50", UNSET)

        is_automated = d.pop("isAutomated", UNSET)

        cancel_order = cls(
            order_id=order_id,
            cl_ord_id=cl_ord_id,
            activation_time=activation_time,
            custom_tag_50=custom_tag_50,
            is_automated=is_automated,
        )

        cancel_order.additional_properties = d
        return cancel_order

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
