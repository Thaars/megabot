import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.order_version_order_type import OrderVersionOrderType
from ..models.order_version_time_in_force import OrderVersionTimeInForce
from ..types import UNSET, Unset

T = TypeVar("T", bound="OrderVersion")


@attr.s(auto_attribs=True)
class OrderVersion:
    """
    Attributes:
        order_id (int):
        order_qty (int):
        order_type (OrderVersionOrderType): Limit, MIT, Market, QTS, Stop, StopLimit, TrailingStop, TrailingStopLimit
        id (Union[Unset, int]):
        price (Union[Unset, float]):
        stop_price (Union[Unset, float]):
        max_show (Union[Unset, int]):
        peg_difference (Union[Unset, float]):
        time_in_force (Union[Unset, OrderVersionTimeInForce]): Day, FOK, GTC, GTD, IOC
        expire_time (Union[Unset, datetime.datetime]):
        text (Union[Unset, str]):
    """

    order_id: int
    order_qty: int
    order_type: OrderVersionOrderType
    id: Union[Unset, int] = UNSET
    price: Union[Unset, float] = UNSET
    stop_price: Union[Unset, float] = UNSET
    max_show: Union[Unset, int] = UNSET
    peg_difference: Union[Unset, float] = UNSET
    time_in_force: Union[Unset, OrderVersionTimeInForce] = UNSET
    expire_time: Union[Unset, datetime.datetime] = UNSET
    text: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        order_id = self.order_id
        order_qty = self.order_qty
        order_type = self.order_type.value

        id = self.id
        price = self.price
        stop_price = self.stop_price
        max_show = self.max_show
        peg_difference = self.peg_difference
        time_in_force: Union[Unset, str] = UNSET
        if not isinstance(self.time_in_force, Unset):
            time_in_force = self.time_in_force.value

        expire_time: Union[Unset, str] = UNSET
        if not isinstance(self.expire_time, Unset):
            expire_time = self.expire_time.isoformat()

        text = self.text

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "orderId": order_id,
                "orderQty": order_qty,
                "orderType": order_type,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if price is not UNSET:
            field_dict["price"] = price
        if stop_price is not UNSET:
            field_dict["stopPrice"] = stop_price
        if max_show is not UNSET:
            field_dict["maxShow"] = max_show
        if peg_difference is not UNSET:
            field_dict["pegDifference"] = peg_difference
        if time_in_force is not UNSET:
            field_dict["timeInForce"] = time_in_force
        if expire_time is not UNSET:
            field_dict["expireTime"] = expire_time
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        order_id = d.pop("orderId")

        order_qty = d.pop("orderQty")

        order_type = OrderVersionOrderType(d.pop("orderType"))

        id = d.pop("id", UNSET)

        price = d.pop("price", UNSET)

        stop_price = d.pop("stopPrice", UNSET)

        max_show = d.pop("maxShow", UNSET)

        peg_difference = d.pop("pegDifference", UNSET)

        _time_in_force = d.pop("timeInForce", UNSET)
        time_in_force: Union[Unset, OrderVersionTimeInForce]
        if isinstance(_time_in_force, Unset):
            time_in_force = UNSET
        else:
            time_in_force = OrderVersionTimeInForce(_time_in_force)

        _expire_time = d.pop("expireTime", UNSET)
        expire_time: Union[Unset, datetime.datetime]
        if isinstance(_expire_time, Unset):
            expire_time = UNSET
        else:
            expire_time = isoparse(_expire_time)

        text = d.pop("text", UNSET)

        order_version = cls(
            order_id=order_id,
            order_qty=order_qty,
            order_type=order_type,
            id=id,
            price=price,
            stop_price=stop_price,
            max_show=max_show,
            peg_difference=peg_difference,
            time_in_force=time_in_force,
            expire_time=expire_time,
            text=text,
        )

        order_version.additional_properties = d
        return order_version

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
