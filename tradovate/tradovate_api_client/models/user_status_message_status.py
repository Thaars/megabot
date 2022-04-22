from enum import Enum


class UserStatusMessageStatus(str, Enum):
    ACTIVE = "Active"
    CLOSED = "Closed"
    INITIATED = "Initiated"
    TEMPORARYLOCKED = "TemporaryLocked"
    UNCONFIRMEDEMAIL = "UnconfirmedEmail"

    def __str__(self) -> str:
        return str(self.value)
