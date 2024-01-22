from enum import Enum


class OrderVersionTimeInForce(str, Enum):
    DAY = "Day"
    FOK = "FOK"
    GTC = "GTC"
    GTD = "GTD"
    IOC = "IOC"

    def __str__(self) -> str:
        return str(self.value)