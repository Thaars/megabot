from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.market_data_subscription_plan_data_type import MarketDataSubscriptionPlanDataType
from ..models.market_data_subscription_plan_professional import MarketDataSubscriptionPlanProfessional
from ..models.trade_date import TradeDate
from ..types import UNSET, Unset

T = TypeVar("T", bound="MarketDataSubscriptionPlan")


@attr.s(auto_attribs=True)
class MarketDataSubscriptionPlan:
    """
    Attributes:
        name (str):
        title (str):
        price (float):
        exchange_scope_id (int):
        data_type (MarketDataSubscriptionPlanDataType): DOM, Top
        professional (MarketDataSubscriptionPlanProfessional): Either, NonProfessional, Professional
        id (Union[Unset, int]):
        start_date (Union[Unset, TradeDate]):
        discontinued_date (Union[Unset, TradeDate]):
        tooltip (Union[Unset, str]):
    """

    name: str
    title: str
    price: float
    exchange_scope_id: int
    data_type: MarketDataSubscriptionPlanDataType
    professional: MarketDataSubscriptionPlanProfessional
    id: Union[Unset, int] = UNSET
    start_date: Union[Unset, TradeDate] = UNSET
    discontinued_date: Union[Unset, TradeDate] = UNSET
    tooltip: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        title = self.title
        price = self.price
        exchange_scope_id = self.exchange_scope_id
        data_type = self.data_type.value

        professional = self.professional.value

        id = self.id
        start_date: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.to_dict()

        discontinued_date: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.discontinued_date, Unset):
            discontinued_date = self.discontinued_date.to_dict()

        tooltip = self.tooltip

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "title": title,
                "price": price,
                "exchangeScopeId": exchange_scope_id,
                "dataType": data_type,
                "professional": professional,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if discontinued_date is not UNSET:
            field_dict["discontinuedDate"] = discontinued_date
        if tooltip is not UNSET:
            field_dict["tooltip"] = tooltip

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        title = d.pop("title")

        price = d.pop("price")

        exchange_scope_id = d.pop("exchangeScopeId")

        data_type = MarketDataSubscriptionPlanDataType(d.pop("dataType"))

        professional = MarketDataSubscriptionPlanProfessional(d.pop("professional"))

        id = d.pop("id", UNSET)

        _start_date = d.pop("startDate", UNSET)
        start_date: Union[Unset, TradeDate]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = TradeDate.from_dict(_start_date)

        _discontinued_date = d.pop("discontinuedDate", UNSET)
        discontinued_date: Union[Unset, TradeDate]
        if isinstance(_discontinued_date, Unset):
            discontinued_date = UNSET
        else:
            discontinued_date = TradeDate.from_dict(_discontinued_date)

        tooltip = d.pop("tooltip", UNSET)

        market_data_subscription_plan = cls(
            name=name,
            title=title,
            price=price,
            exchange_scope_id=exchange_scope_id,
            data_type=data_type,
            professional=professional,
            id=id,
            start_date=start_date,
            discontinued_date=discontinued_date,
            tooltip=tooltip,
        )

        market_data_subscription_plan.additional_properties = d
        return market_data_subscription_plan

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
