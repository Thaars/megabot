import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserSession")


@attr.s(auto_attribs=True)
class UserSession:
    """
    Attributes:
        user_id (int):
        start_time (datetime.datetime):
        client_app_id (int):
        id (Union[Unset, int]):
        end_time (Union[Unset, datetime.datetime]):
        ip_address (Union[Unset, str]):
        app_id (Union[Unset, str]):
        app_version (Union[Unset, str]):
    """

    user_id: int
    start_time: datetime.datetime
    client_app_id: int
    id: Union[Unset, int] = UNSET
    end_time: Union[Unset, datetime.datetime] = UNSET
    ip_address: Union[Unset, str] = UNSET
    app_id: Union[Unset, str] = UNSET
    app_version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_id = self.user_id
        start_time = self.start_time.isoformat()

        client_app_id = self.client_app_id
        id = self.id
        end_time: Union[Unset, str] = UNSET
        if not isinstance(self.end_time, Unset):
            end_time = self.end_time.isoformat()

        ip_address = self.ip_address
        app_id = self.app_id
        app_version = self.app_version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userId": user_id,
                "startTime": start_time,
                "clientAppId": client_app_id,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if ip_address is not UNSET:
            field_dict["ipAddress"] = ip_address
        if app_id is not UNSET:
            field_dict["appId"] = app_id
        if app_version is not UNSET:
            field_dict["appVersion"] = app_version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_id = d.pop("userId")

        start_time = isoparse(d.pop("startTime"))

        client_app_id = d.pop("clientAppId")

        id = d.pop("id", UNSET)

        _end_time = d.pop("endTime", UNSET)
        end_time: Union[Unset, datetime.datetime]
        if isinstance(_end_time, Unset):
            end_time = UNSET
        else:
            end_time = isoparse(_end_time)

        ip_address = d.pop("ipAddress", UNSET)

        app_id = d.pop("appId", UNSET)

        app_version = d.pop("appVersion", UNSET)

        user_session = cls(
            user_id=user_id,
            start_time=start_time,
            client_app_id=client_app_id,
            id=id,
            end_time=end_time,
            ip_address=ip_address,
            app_id=app_id,
            app_version=app_version,
        )

        user_session.additional_properties = d
        return user_session

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
