from enum import Enum


class PropertyPropertyType(str, Enum):
    BOOLEAN = "Boolean"
    ENUM = "Enum"
    INTEGER = "Integer"
    STRING = "String"

    def __str__(self) -> str:
        return str(self.value)
