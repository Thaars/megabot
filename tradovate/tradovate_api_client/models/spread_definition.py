import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.spread_definition_spread_type import SpreadDefinitionSpreadType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SpreadDefinition")


@attr.s(auto_attribs=True)
class SpreadDefinition:
    """
    Attributes:
        timestamp (datetime.datetime):
        spread_type (SpreadDefinitionSpreadType): Bundle, BundleSpread, Butterfly, CalendarSpread, Condor, Crack,
            DoubleButterfly, General, IntercommoditySpread, LaggedIntercommoditySpread, Pack, PackButterfly, PackSpread,
            ReducedTickCalendarSpread, ReverseIntercommoditySpread, ReverseSpread, Strip, TreasuryIntercommoditySpread
        uds (bool):
        id (Union[Unset, int]):
    """

    timestamp: datetime.datetime
    spread_type: SpreadDefinitionSpreadType
    uds: bool
    id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        timestamp = self.timestamp.isoformat()

        spread_type = self.spread_type.value

        uds = self.uds
        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "timestamp": timestamp,
                "spreadType": spread_type,
                "uds": uds,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        timestamp = isoparse(d.pop("timestamp"))

        spread_type = SpreadDefinitionSpreadType(d.pop("spreadType"))

        uds = d.pop("uds")

        id = d.pop("id", UNSET)

        spread_definition = cls(
            timestamp=timestamp,
            spread_type=spread_type,
            uds=uds,
            id=id,
        )

        spread_definition.additional_properties = d
        return spread_definition

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
