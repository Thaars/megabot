from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AccessTokenRequest")


@attr.s(auto_attribs=True)
class AccessTokenRequest:
    """
    Attributes:
        name (str):
        password (str):
        app_id (Union[Unset, str]):
        app_version (Union[Unset, str]):
        device_id (Union[Unset, str]):
        cid (Union[Unset, str]):
        sec (Union[Unset, str]):
    """

    name: str
    password: str
    app_id: Union[Unset, str] = UNSET
    app_version: Union[Unset, str] = UNSET
    device_id: Union[Unset, str] = UNSET
    cid: Union[Unset, str] = UNSET
    sec: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        password = self.password
        app_id = self.app_id
        app_version = self.app_version
        device_id = self.device_id
        cid = self.cid
        sec = self.sec

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "password": password,
            }
        )
        if app_id is not UNSET:
            field_dict["appId"] = app_id
        if app_version is not UNSET:
            field_dict["appVersion"] = app_version
        if device_id is not UNSET:
            field_dict["deviceId"] = device_id
        if cid is not UNSET:
            field_dict["cid"] = cid
        if sec is not UNSET:
            field_dict["sec"] = sec

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        password = d.pop("password")

        app_id = d.pop("appId", UNSET)

        app_version = d.pop("appVersion", UNSET)

        device_id = d.pop("deviceId", UNSET)

        cid = d.pop("cid", UNSET)

        sec = d.pop("sec", UNSET)

        access_token_request = cls(
            name=name,
            password=password,
            app_id=app_id,
            app_version=app_version,
            device_id=device_id,
            cid=cid,
            sec=sec,
        )

        access_token_request.additional_properties = d
        return access_token_request

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
