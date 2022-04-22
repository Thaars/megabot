import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="MarginSnapshot")


@attr.s(auto_attribs=True)
class MarginSnapshot:
    """
    Attributes:
        timestamp (datetime.datetime):
        risk_time_period_id (int):
        initial_margin (float):
        maintenance_margin (float):
        total_used_margin (float):
        full_initial_margin (float):
        id (Union[Unset, int]):
        auto_liq_level (Union[Unset, float]):
        liq_only_level (Union[Unset, float]):
    """

    timestamp: datetime.datetime
    risk_time_period_id: int
    initial_margin: float
    maintenance_margin: float
    total_used_margin: float
    full_initial_margin: float
    id: Union[Unset, int] = UNSET
    auto_liq_level: Union[Unset, float] = UNSET
    liq_only_level: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        timestamp = self.timestamp.isoformat()

        risk_time_period_id = self.risk_time_period_id
        initial_margin = self.initial_margin
        maintenance_margin = self.maintenance_margin
        total_used_margin = self.total_used_margin
        full_initial_margin = self.full_initial_margin
        id = self.id
        auto_liq_level = self.auto_liq_level
        liq_only_level = self.liq_only_level

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
                "riskTimePeriodId": risk_time_period_id,
                "initialMargin": initial_margin,
                "maintenanceMargin": maintenance_margin,
                "totalUsedMargin": total_used_margin,
                "fullInitialMargin": full_initial_margin,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if auto_liq_level is not UNSET:
            field_dict["autoLiqLevel"] = auto_liq_level
        if liq_only_level is not UNSET:
            field_dict["liqOnlyLevel"] = liq_only_level

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        timestamp = isoparse(d.pop("timestamp"))

        risk_time_period_id = d.pop("riskTimePeriodId")

        initial_margin = d.pop("initialMargin")

        maintenance_margin = d.pop("maintenanceMargin")

        total_used_margin = d.pop("totalUsedMargin")

        full_initial_margin = d.pop("fullInitialMargin")

        id = d.pop("id", UNSET)

        auto_liq_level = d.pop("autoLiqLevel", UNSET)

        liq_only_level = d.pop("liqOnlyLevel", UNSET)

        margin_snapshot = cls(
            timestamp=timestamp,
            risk_time_period_id=risk_time_period_id,
            initial_margin=initial_margin,
            maintenance_margin=maintenance_margin,
            total_used_margin=total_used_margin,
            full_initial_margin=full_initial_margin,
            id=id,
            auto_liq_level=auto_liq_level,
            liq_only_level=liq_only_level,
        )

        margin_snapshot.additional_properties = d
        return margin_snapshot

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
