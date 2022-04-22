from enum import Enum


class CommandCommandType(str, Enum):
    CANCEL = "Cancel"
    MODIFY = "Modify"
    NEW = "New"

    def __str__(self) -> str:
        return str(self.value)
