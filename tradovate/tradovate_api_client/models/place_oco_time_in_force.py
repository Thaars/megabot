from enum import Enum


class PlaceOCOTimeInForce(str, Enum):
    DAY = "Day"
    FOK = "FOK"
    GTC = "GTC"
    GTD = "GTD"
    IOC = "IOC"

    def __str__(self) -> str:
        return str(self.value)
