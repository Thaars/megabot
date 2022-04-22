from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.trade_date import TradeDate
from ..models.tradovate_subscription_plan_duration_units import TradovateSubscriptionPlanDurationUnits
from ..types import UNSET, Unset

T = TypeVar("T", bound="TradovateSubscriptionPlan")


@attr.s(auto_attribs=True)
class TradovateSubscriptionPlan:
    """
    Attributes:
        name (str):
        title (str):
        price (float):
        category (str):
        trial (bool):
        duration (int):
        duration_units (TradovateSubscriptionPlanDurationUnits): Month, Quarter, Week, Year
        id (Union[Unset, int]):
        start_date (Union[Unset, TradeDate]):
        discontinued_date (Union[Unset, TradeDate]):
        risk_category_id (Union[Unset, int]):
        multiple_accounts (Union[Unset, bool]):
        organization_id (Union[Unset, int]):
        replay_sessions (Union[Unset, int]):
        footnote (Union[Unset, str]):
        sim_only (Union[Unset, bool]):
    """

    name: str
    title: str
    price: float
    category: str
    trial: bool
    duration: int
    duration_units: TradovateSubscriptionPlanDurationUnits
    id: Union[Unset, int] = UNSET
    start_date: Union[Unset, TradeDate] = UNSET
    discontinued_date: Union[Unset, TradeDate] = UNSET
    risk_category_id: Union[Unset, int] = UNSET
    multiple_accounts: Union[Unset, bool] = UNSET
    organization_id: Union[Unset, int] = UNSET
    replay_sessions: Union[Unset, int] = UNSET
    footnote: Union[Unset, str] = UNSET
    sim_only: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        title = self.title
        price = self.price
        category = self.category
        trial = self.trial
        duration = self.duration
        duration_units = self.duration_units.value

        id = self.id
        start_date: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.to_dict()

        discontinued_date: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.discontinued_date, Unset):
            discontinued_date = self.discontinued_date.to_dict()

        risk_category_id = self.risk_category_id
        multiple_accounts = self.multiple_accounts
        organization_id = self.organization_id
        replay_sessions = self.replay_sessions
        footnote = self.footnote
        sim_only = self.sim_only

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "title": title,
                "price": price,
                "category": category,
                "trial": trial,
                "duration": duration,
                "durationUnits": duration_units,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if discontinued_date is not UNSET:
            field_dict["discontinuedDate"] = discontinued_date
        if risk_category_id is not UNSET:
            field_dict["riskCategoryId"] = risk_category_id
        if multiple_accounts is not UNSET:
            field_dict["multipleAccounts"] = multiple_accounts
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if replay_sessions is not UNSET:
            field_dict["replaySessions"] = replay_sessions
        if footnote is not UNSET:
            field_dict["footnote"] = footnote
        if sim_only is not UNSET:
            field_dict["simOnly"] = sim_only

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        title = d.pop("title")

        price = d.pop("price")

        category = d.pop("category")

        trial = d.pop("trial")

        duration = d.pop("duration")

        duration_units = TradovateSubscriptionPlanDurationUnits(d.pop("durationUnits"))

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

        risk_category_id = d.pop("riskCategoryId", UNSET)

        multiple_accounts = d.pop("multipleAccounts", UNSET)

        organization_id = d.pop("organizationId", UNSET)

        replay_sessions = d.pop("replaySessions", UNSET)

        footnote = d.pop("footnote", UNSET)

        sim_only = d.pop("simOnly", UNSET)

        tradovate_subscription_plan = cls(
            name=name,
            title=title,
            price=price,
            category=category,
            trial=trial,
            duration=duration,
            duration_units=duration_units,
            id=id,
            start_date=start_date,
            discontinued_date=discontinued_date,
            risk_category_id=risk_category_id,
            multiple_accounts=multiple_accounts,
            organization_id=organization_id,
            replay_sessions=replay_sessions,
            footnote=footnote,
            sim_only=sim_only,
        )

        tradovate_subscription_plan.additional_properties = d
        return tradovate_subscription_plan

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
