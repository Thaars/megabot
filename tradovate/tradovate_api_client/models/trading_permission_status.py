from enum import Enum


class TradingPermissionStatus(str, Enum):
    ACCEPTED = "Accepted"
    APPROVED = "Approved"
    DECLINED = "Declined"
    REQUESTED = "Requested"
    REVOKED = "Revoked"

    def __str__(self) -> str:
        return str(self.value)
