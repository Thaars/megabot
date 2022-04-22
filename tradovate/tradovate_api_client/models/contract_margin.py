import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContractMargin")


@attr.s(auto_attribs=True)
class ContractMargin:
    """
    Attributes:
        initial_margin (float):
        maintenance_margin (float):
        timestamp (datetime.datetime):
        id (Union[Unset, int]):
    """

    initial_margin: float
    maintenance_margin: float
    timestamp: datetime.datetime
    id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        initial_margin = self.initial_margin
        maintenance_margin = self.maintenance_margin
        timestamp = self.timestamp.isoformat()

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "initialMargin": initial_margin,
                "maintenanceMargin": maintenance_margin,
                "timestamp": timestamp,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        initial_margin = d.pop("initialMargin")

        maintenance_margin = d.pop("maintenanceMargin")

        timestamp = isoparse(d.pop("timestamp"))

        id = d.pop("id", UNSET)

        contract_margin = cls(
            initial_margin=initial_margin,
            maintenance_margin=maintenance_margin,
            timestamp=timestamp,
            id=id,
        )

        contract_margin.additional_properties = d
        return contract_margin

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
