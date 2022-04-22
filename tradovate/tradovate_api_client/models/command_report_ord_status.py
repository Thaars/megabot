from enum import Enum


class CommandReportOrdStatus(str, Enum):
    CANCELED = "Canceled"
    COMPLETED = "Completed"
    EXPIRED = "Expired"
    FILLED = "Filled"
    PENDINGCANCEL = "PendingCancel"
    PENDINGNEW = "PendingNew"
    PENDINGREPLACE = "PendingReplace"
    REJECTED = "Rejected"
    SUSPENDED = "Suspended"
    UNKNOWN = "Unknown"
    WORKING = "Working"

    def __str__(self) -> str:
        return str(self.value)
