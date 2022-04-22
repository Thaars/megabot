from enum import Enum


class CashBalanceLogCashChangeType(str, Enum):
    AUTOMATICRECONCILIATION = "AutomaticReconciliation"
    BROKERAGEFEE = "BrokerageFee"
    CANCELLEDPAIREDTRADE = "CancelledPairedTrade"
    CLEARINGFEE = "ClearingFee"
    COMMISSION = "Commission"
    DESKFEE = "DeskFee"
    ENTITLEMENTSUBSCRIPTION = "EntitlementSubscription"
    EXCHANGEFEE = "ExchangeFee"
    FUNDTRANSACTION = "FundTransaction"
    FUNDTRANSACTIONFEE = "FundTransactionFee"
    IPFEE = "IPFee"
    LIQUIDATIONFEE = "LiquidationFee"
    MANUALADJUSTMENT = "ManualAdjustment"
    MARKETDATASUBSCRIPTION = "MarketDataSubscription"
    NEWSESSION = "NewSession"
    NFAFEE = "NfaFee"
    OPTIONSTRADE = "OptionsTrade"
    ORDERROUTINGFEE = "OrderRoutingFee"
    TRADEPAIRED = "TradePaired"
    TRADOVATESUBSCRIPTION = "TradovateSubscription"

    def __str__(self) -> str:
        return str(self.value)
