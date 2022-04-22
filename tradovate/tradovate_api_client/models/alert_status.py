from enum import Enum


class AlertStatus(str, Enum):
    ACTIVE = "Active"
    EXPIRED = "Expired"
    FAILED = "Failed"
    INACTIVE = "Inactive"
    TRIGGEREDOUT = "TriggeredOut"

    def __str__(self) -> str:
        return str(self.value)
