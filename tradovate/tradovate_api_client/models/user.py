import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.user_status import UserStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="User")


@attr.s(auto_attribs=True)
class User:
    """
    Attributes:
        name (str):
        timestamp (datetime.datetime):
        email (str):
        status (UserStatus): Active, Closed, Initiated, TemporaryLocked, UnconfirmedEmail
        professional (bool):
        id (Union[Unset, int]):
        organization_id (Union[Unset, int]):
        linked_user_id (Union[Unset, int]): Linked Live
        foreign_introducing_broker_id (Union[Unset, int]):
    """

    name: str
    timestamp: datetime.datetime
    email: str
    status: UserStatus
    professional: bool
    id: Union[Unset, int] = UNSET
    organization_id: Union[Unset, int] = UNSET
    linked_user_id: Union[Unset, int] = UNSET
    foreign_introducing_broker_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        timestamp = self.timestamp.isoformat()

        email = self.email
        status = self.status.value

        professional = self.professional
        id = self.id
        organization_id = self.organization_id
        linked_user_id = self.linked_user_id
        foreign_introducing_broker_id = self.foreign_introducing_broker_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "timestamp": timestamp,
                "email": email,
                "status": status,
                "professional": professional,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if linked_user_id is not UNSET:
            field_dict["linkedUserId"] = linked_user_id
        if foreign_introducing_broker_id is not UNSET:
            field_dict["foreignIntroducingBrokerId"] = foreign_introducing_broker_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        timestamp = isoparse(d.pop("timestamp"))

        email = d.pop("email")

        status = UserStatus(d.pop("status"))

        professional = d.pop("professional")

        id = d.pop("id", UNSET)

        organization_id = d.pop("organizationId", UNSET)

        linked_user_id = d.pop("linkedUserId", UNSET)

        foreign_introducing_broker_id = d.pop("foreignIntroducingBrokerId", UNSET)

        user = cls(
            name=name,
            timestamp=timestamp,
            email=email,
            status=status,
            professional=professional,
            id=id,
            organization_id=organization_id,
            linked_user_id=linked_user_id,
            foreign_introducing_broker_id=foreign_introducing_broker_id,
        )

        user.additional_properties = d
        return user

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
