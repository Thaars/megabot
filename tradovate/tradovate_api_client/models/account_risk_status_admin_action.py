from enum import Enum


class AccountRiskStatusAdminAction(str, Enum):
    AGREEDONLIQONLYMODEBYAUTOLIQ = "AgreedOnLiqOnlyModeByAutoLiq"
    AGREEDONLIQUIDATIONBYAUTOLIQ = "AgreedOnLiquidationByAutoLiq"
    DISABLEAUTOLIQ = "DisableAutoLiq"
    LIQUIDATEIMMEDIATELY = "LiquidateImmediately"
    LIQUIDATEONLYMODEIMMEDIATELY = "LiquidateOnlyModeImmediately"
    LOCKTRADINGIMMEDIATELY = "LockTradingImmediately"
    NORMAL = "Normal"
    PLACEAUTOLIQONHOLD = "PlaceAutoLiqOnHold"

    def __str__(self) -> str:
        return str(self.value)
