import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.restrained_order_version_action import RestrainedOrderVersionAction
from ..models.restrained_order_version_order_type import RestrainedOrderVersionOrderType
from ..models.restrained_order_version_time_in_force import RestrainedOrderVersionTimeInForce
from ..types import UNSET, Unset

T = TypeVar("T", bound="RestrainedOrderVersion")


@attr.s(auto_attribs=True)
class RestrainedOrderVersion:
    """
    Attributes:
        action (RestrainedOrderVersionAction): Buy, Sell
        order_type (RestrainedOrderVersionOrderType): Limit, MIT, Market, QTS, Stop, StopLimit, TrailingStop,
            TrailingStopLimit
        cl_ord_id (Union[Unset, str]):
        price (Union[Unset, float]):
        stop_price (Union[Unset, float]):
        max_show (Union[Unset, int]):
        peg_difference (Union[Unset, float]):
        time_in_force (Union[Unset, RestrainedOrderVersionTimeInForce]): Day, FOK, GTC, GTD, IOC
        expire_time (Union[Unset, datetime.datetime]):
        text (Union[Unset, str]):
    """

    action: RestrainedOrderVersionAction
    order_type: RestrainedOrderVersionOrderType
    cl_ord_id: Union[Unset, str] = UNSET
    price: Union[Unset, float] = UNSET
    stop_price: Union[Unset, float] = UNSET
    max_show: Union[Unset, int] = UNSET
    peg_difference: Union[Unset, float] = UNSET
    time_in_force: Union[Unset, RestrainedOrderVersionTimeInForce] = UNSET
    expire_time: Union[Unset, datetime.datetime] = UNSET
    text: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        action = self.action.value

        order_type = self.order_type.value

        cl_ord_id = self.cl_ord_id
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
                "action": action,
                "orderType": order_type,
            }
        )
        if cl_ord_id is not UNSET:
            field_dict["clOrdId"] = cl_ord_id
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
        action = RestrainedOrderVersionAction(d.pop("action"))

        order_type = RestrainedOrderVersionOrderType(d.pop("orderType"))

        cl_ord_id = d.pop("clOrdId", UNSET)

        price = d.pop("price", UNSET)

        stop_price = d.pop("stopPrice", UNSET)

        max_show = d.pop("maxShow", UNSET)

        peg_difference = d.pop("pegDifference", UNSET)

        _time_in_force = d.pop("timeInForce", UNSET)
        time_in_force: Union[Unset, RestrainedOrderVersionTimeInForce]
        if isinstance(_time_in_force, Unset):
            time_in_force = UNSET
        else:
            time_in_force = RestrainedOrderVersionTimeInForce(_time_in_force)

        _expire_time = d.pop("expireTime", UNSET)
        expire_time: Union[Unset, datetime.datetime]
        if isinstance(_expire_time, Unset):
            expire_time = UNSET
        else:
            expire_time = isoparse(_expire_time)

        text = d.pop("text", UNSET)

        restrained_order_version = cls(
            action=action,
            order_type=order_type,
            cl_ord_id=cl_ord_id,
            price=price,
            stop_price=stop_price,
            max_show=max_show,
            peg_difference=peg_difference,
            time_in_force=time_in_force,
            expire_time=expire_time,
            text=text,
        )

        restrained_order_version.additional_properties = d
        return restrained_order_version

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
