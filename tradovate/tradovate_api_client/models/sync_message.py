from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.account import Account
from ..models.account_risk_status import AccountRiskStatus
from ..models.cash_balance import CashBalance
from ..models.command import Command
from ..models.command_report import CommandReport
from ..models.contract import Contract
from ..models.contract_group import ContractGroup
from ..models.contract_maturity import ContractMaturity
from ..models.currency import Currency
from ..models.exchange import Exchange
from ..models.execution_report import ExecutionReport
from ..models.fill import Fill
from ..models.fill_pair import FillPair
from ..models.margin_snapshot import MarginSnapshot
from ..models.order import Order
from ..models.order_strategy import OrderStrategy
from ..models.order_strategy_link import OrderStrategyLink
from ..models.order_strategy_type import OrderStrategyType
from ..models.order_version import OrderVersion
from ..models.position import Position
from ..models.product import Product
from ..models.property_ import Property
from ..models.spread_definition import SpreadDefinition
from ..models.user import User
from ..models.user_account_auto_liq import UserAccountAutoLiq
from ..models.user_plugin import UserPlugin
from ..models.user_property import UserProperty
from ..types import UNSET, Unset

T = TypeVar("T", bound="SyncMessage")


@attr.s(auto_attribs=True)
class SyncMessage:
    """
    Attributes:
        users (List[User]):
        contract_groups (List[ContractGroup]):
        accounts (Union[Unset, List[Account]]):
        account_risk_statuses (Union[Unset, List[AccountRiskStatus]]):
        margin_snapshots (Union[Unset, List[MarginSnapshot]]):
        user_account_auto_liqs (Union[Unset, List[UserAccountAutoLiq]]):
        cash_balances (Union[Unset, List[CashBalance]]):
        currencies (Union[Unset, List[Currency]]):
        positions (Union[Unset, List[Position]]):
        fill_pairs (Union[Unset, List[FillPair]]):
        orders (Union[Unset, List[Order]]):
        contracts (Union[Unset, List[Contract]]):
        contract_maturities (Union[Unset, List[ContractMaturity]]):
        products (Union[Unset, List[Product]]):
        exchanges (Union[Unset, List[Exchange]]):
        spread_definitions (Union[Unset, List[SpreadDefinition]]):
        commands (Union[Unset, List[Command]]):
        command_reports (Union[Unset, List[CommandReport]]):
        execution_reports (Union[Unset, List[ExecutionReport]]):
        order_versions (Union[Unset, List[OrderVersion]]):
        fills (Union[Unset, List[Fill]]):
        order_strategies (Union[Unset, List[OrderStrategy]]):
        order_strategy_links (Union[Unset, List[OrderStrategyLink]]):
        user_properties (Union[Unset, List[UserProperty]]):
        properties (Union[Unset, List[Property]]):
        user_plugins (Union[Unset, List[UserPlugin]]):
        order_strategy_types (Union[Unset, List[OrderStrategyType]]):
    """

    users: List[User]
    contract_groups: List[ContractGroup]
    accounts: Union[Unset, List[Account]] = UNSET
    account_risk_statuses: Union[Unset, List[AccountRiskStatus]] = UNSET
    margin_snapshots: Union[Unset, List[MarginSnapshot]] = UNSET
    user_account_auto_liqs: Union[Unset, List[UserAccountAutoLiq]] = UNSET
    cash_balances: Union[Unset, List[CashBalance]] = UNSET
    currencies: Union[Unset, List[Currency]] = UNSET
    positions: Union[Unset, List[Position]] = UNSET
    fill_pairs: Union[Unset, List[FillPair]] = UNSET
    orders: Union[Unset, List[Order]] = UNSET
    contracts: Union[Unset, List[Contract]] = UNSET
    contract_maturities: Union[Unset, List[ContractMaturity]] = UNSET
    products: Union[Unset, List[Product]] = UNSET
    exchanges: Union[Unset, List[Exchange]] = UNSET
    spread_definitions: Union[Unset, List[SpreadDefinition]] = UNSET
    commands: Union[Unset, List[Command]] = UNSET
    command_reports: Union[Unset, List[CommandReport]] = UNSET
    execution_reports: Union[Unset, List[ExecutionReport]] = UNSET
    order_versions: Union[Unset, List[OrderVersion]] = UNSET
    fills: Union[Unset, List[Fill]] = UNSET
    order_strategies: Union[Unset, List[OrderStrategy]] = UNSET
    order_strategy_links: Union[Unset, List[OrderStrategyLink]] = UNSET
    user_properties: Union[Unset, List[UserProperty]] = UNSET
    properties: Union[Unset, List[Property]] = UNSET
    user_plugins: Union[Unset, List[UserPlugin]] = UNSET
    order_strategy_types: Union[Unset, List[OrderStrategyType]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        users = []
        for users_item_data in self.users:
            users_item = users_item_data.to_dict()

            users.append(users_item)

        contract_groups = []
        for contract_groups_item_data in self.contract_groups:
            contract_groups_item = contract_groups_item_data.to_dict()

            contract_groups.append(contract_groups_item)

        accounts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.accounts, Unset):
            accounts = []
            for accounts_item_data in self.accounts:
                accounts_item = accounts_item_data.to_dict()

                accounts.append(accounts_item)

        account_risk_statuses: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.account_risk_statuses, Unset):
            account_risk_statuses = []
            for account_risk_statuses_item_data in self.account_risk_statuses:
                account_risk_statuses_item = account_risk_statuses_item_data.to_dict()

                account_risk_statuses.append(account_risk_statuses_item)

        margin_snapshots: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.margin_snapshots, Unset):
            margin_snapshots = []
            for margin_snapshots_item_data in self.margin_snapshots:
                margin_snapshots_item = margin_snapshots_item_data.to_dict()

                margin_snapshots.append(margin_snapshots_item)

        user_account_auto_liqs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.user_account_auto_liqs, Unset):
            user_account_auto_liqs = []
            for user_account_auto_liqs_item_data in self.user_account_auto_liqs:
                user_account_auto_liqs_item = user_account_auto_liqs_item_data.to_dict()

                user_account_auto_liqs.append(user_account_auto_liqs_item)

        cash_balances: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.cash_balances, Unset):
            cash_balances = []
            for cash_balances_item_data in self.cash_balances:
                cash_balances_item = cash_balances_item_data.to_dict()

                cash_balances.append(cash_balances_item)

        currencies: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.currencies, Unset):
            currencies = []
            for currencies_item_data in self.currencies:
                currencies_item = currencies_item_data.to_dict()

                currencies.append(currencies_item)

        positions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.positions, Unset):
            positions = []
            for positions_item_data in self.positions:
                positions_item = positions_item_data.to_dict()

                positions.append(positions_item)

        fill_pairs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.fill_pairs, Unset):
            fill_pairs = []
            for fill_pairs_item_data in self.fill_pairs:
                fill_pairs_item = fill_pairs_item_data.to_dict()

                fill_pairs.append(fill_pairs_item)

        orders: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.orders, Unset):
            orders = []
            for orders_item_data in self.orders:
                orders_item = orders_item_data.to_dict()

                orders.append(orders_item)

        contracts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.contracts, Unset):
            contracts = []
            for contracts_item_data in self.contracts:
                contracts_item = contracts_item_data.to_dict()

                contracts.append(contracts_item)

        contract_maturities: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.contract_maturities, Unset):
            contract_maturities = []
            for contract_maturities_item_data in self.contract_maturities:
                contract_maturities_item = contract_maturities_item_data.to_dict()

                contract_maturities.append(contract_maturities_item)

        products: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.products, Unset):
            products = []
            for products_item_data in self.products:
                products_item = products_item_data.to_dict()

                products.append(products_item)

        exchanges: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.exchanges, Unset):
            exchanges = []
            for exchanges_item_data in self.exchanges:
                exchanges_item = exchanges_item_data.to_dict()

                exchanges.append(exchanges_item)

        spread_definitions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.spread_definitions, Unset):
            spread_definitions = []
            for spread_definitions_item_data in self.spread_definitions:
                spread_definitions_item = spread_definitions_item_data.to_dict()

                spread_definitions.append(spread_definitions_item)

        commands: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.commands, Unset):
            commands = []
            for commands_item_data in self.commands:
                commands_item = commands_item_data.to_dict()

                commands.append(commands_item)

        command_reports: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.command_reports, Unset):
            command_reports = []
            for command_reports_item_data in self.command_reports:
                command_reports_item = command_reports_item_data.to_dict()

                command_reports.append(command_reports_item)

        execution_reports: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.execution_reports, Unset):
            execution_reports = []
            for execution_reports_item_data in self.execution_reports:
                execution_reports_item = execution_reports_item_data.to_dict()

                execution_reports.append(execution_reports_item)

        order_versions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.order_versions, Unset):
            order_versions = []
            for order_versions_item_data in self.order_versions:
                order_versions_item = order_versions_item_data.to_dict()

                order_versions.append(order_versions_item)

        fills: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.fills, Unset):
            fills = []
            for fills_item_data in self.fills:
                fills_item = fills_item_data.to_dict()

                fills.append(fills_item)

        order_strategies: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.order_strategies, Unset):
            order_strategies = []
            for order_strategies_item_data in self.order_strategies:
                order_strategies_item = order_strategies_item_data.to_dict()

                order_strategies.append(order_strategies_item)

        order_strategy_links: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.order_strategy_links, Unset):
            order_strategy_links = []
            for order_strategy_links_item_data in self.order_strategy_links:
                order_strategy_links_item = order_strategy_links_item_data.to_dict()

                order_strategy_links.append(order_strategy_links_item)

        user_properties: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.user_properties, Unset):
            user_properties = []
            for user_properties_item_data in self.user_properties:
                user_properties_item = user_properties_item_data.to_dict()

                user_properties.append(user_properties_item)

        properties: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.properties, Unset):
            properties = []
            for properties_item_data in self.properties:
                properties_item = properties_item_data.to_dict()

                properties.append(properties_item)

        user_plugins: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.user_plugins, Unset):
            user_plugins = []
            for user_plugins_item_data in self.user_plugins:
                user_plugins_item = user_plugins_item_data.to_dict()

                user_plugins.append(user_plugins_item)

        order_strategy_types: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.order_strategy_types, Unset):
            order_strategy_types = []
            for order_strategy_types_item_data in self.order_strategy_types:
                order_strategy_types_item = order_strategy_types_item_data.to_dict()

                order_strategy_types.append(order_strategy_types_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "users": users,
                "contractGroups": contract_groups,
            }
        )
        if accounts is not UNSET:
            field_dict["accounts"] = accounts
        if account_risk_statuses is not UNSET:
            field_dict["accountRiskStatuses"] = account_risk_statuses
        if margin_snapshots is not UNSET:
            field_dict["marginSnapshots"] = margin_snapshots
        if user_account_auto_liqs is not UNSET:
            field_dict["userAccountAutoLiqs"] = user_account_auto_liqs
        if cash_balances is not UNSET:
            field_dict["cashBalances"] = cash_balances
        if currencies is not UNSET:
            field_dict["currencies"] = currencies
        if positions is not UNSET:
            field_dict["positions"] = positions
        if fill_pairs is not UNSET:
            field_dict["fillPairs"] = fill_pairs
        if orders is not UNSET:
            field_dict["orders"] = orders
        if contracts is not UNSET:
            field_dict["contracts"] = contracts
        if contract_maturities is not UNSET:
            field_dict["contractMaturities"] = contract_maturities
        if products is not UNSET:
            field_dict["products"] = products
        if exchanges is not UNSET:
            field_dict["exchanges"] = exchanges
        if spread_definitions is not UNSET:
            field_dict["spreadDefinitions"] = spread_definitions
        if commands is not UNSET:
            field_dict["commands"] = commands
        if command_reports is not UNSET:
            field_dict["commandReports"] = command_reports
        if execution_reports is not UNSET:
            field_dict["executionReports"] = execution_reports
        if order_versions is not UNSET:
            field_dict["orderVersions"] = order_versions
        if fills is not UNSET:
            field_dict["fills"] = fills
        if order_strategies is not UNSET:
            field_dict["orderStrategies"] = order_strategies
        if order_strategy_links is not UNSET:
            field_dict["orderStrategyLinks"] = order_strategy_links
        if user_properties is not UNSET:
            field_dict["userProperties"] = user_properties
        if properties is not UNSET:
            field_dict["properties"] = properties
        if user_plugins is not UNSET:
            field_dict["userPlugins"] = user_plugins
        if order_strategy_types is not UNSET:
            field_dict["orderStrategyTypes"] = order_strategy_types

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        users = []
        _users = d.pop("users")
        for users_item_data in _users:
            users_item = User.from_dict(users_item_data)

            users.append(users_item)

        contract_groups = []
        _contract_groups = d.pop("contractGroups")
        for contract_groups_item_data in _contract_groups:
            contract_groups_item = ContractGroup.from_dict(contract_groups_item_data)

            contract_groups.append(contract_groups_item)

        accounts = []
        _accounts = d.pop("accounts", UNSET)
        for accounts_item_data in _accounts or []:
            accounts_item = Account.from_dict(accounts_item_data)

            accounts.append(accounts_item)

        account_risk_statuses = []
        _account_risk_statuses = d.pop("accountRiskStatuses", UNSET)
        for account_risk_statuses_item_data in _account_risk_statuses or []:
            account_risk_statuses_item = AccountRiskStatus.from_dict(account_risk_statuses_item_data)

            account_risk_statuses.append(account_risk_statuses_item)

        margin_snapshots = []
        _margin_snapshots = d.pop("marginSnapshots", UNSET)
        for margin_snapshots_item_data in _margin_snapshots or []:
            margin_snapshots_item = MarginSnapshot.from_dict(margin_snapshots_item_data)

            margin_snapshots.append(margin_snapshots_item)

        user_account_auto_liqs = []
        _user_account_auto_liqs = d.pop("userAccountAutoLiqs", UNSET)
        for user_account_auto_liqs_item_data in _user_account_auto_liqs or []:
            user_account_auto_liqs_item = UserAccountAutoLiq.from_dict(user_account_auto_liqs_item_data)

            user_account_auto_liqs.append(user_account_auto_liqs_item)

        cash_balances = []
        _cash_balances = d.pop("cashBalances", UNSET)
        for cash_balances_item_data in _cash_balances or []:
            cash_balances_item = CashBalance.from_dict(cash_balances_item_data)

            cash_balances.append(cash_balances_item)

        currencies = []
        _currencies = d.pop("currencies", UNSET)
        for currencies_item_data in _currencies or []:
            currencies_item = Currency.from_dict(currencies_item_data)

            currencies.append(currencies_item)

        positions = []
        _positions = d.pop("positions", UNSET)
        for positions_item_data in _positions or []:
            positions_item = Position.from_dict(positions_item_data)

            positions.append(positions_item)

        fill_pairs = []
        _fill_pairs = d.pop("fillPairs", UNSET)
        for fill_pairs_item_data in _fill_pairs or []:
            fill_pairs_item = FillPair.from_dict(fill_pairs_item_data)

            fill_pairs.append(fill_pairs_item)

        orders = []
        _orders = d.pop("orders", UNSET)
        for orders_item_data in _orders or []:
            orders_item = Order.from_dict(orders_item_data)

            orders.append(orders_item)

        contracts = []
        _contracts = d.pop("contracts", UNSET)
        for contracts_item_data in _contracts or []:
            contracts_item = Contract.from_dict(contracts_item_data)

            contracts.append(contracts_item)

        contract_maturities = []
        _contract_maturities = d.pop("contractMaturities", UNSET)
        for contract_maturities_item_data in _contract_maturities or []:
            contract_maturities_item = ContractMaturity.from_dict(contract_maturities_item_data)

            contract_maturities.append(contract_maturities_item)

        products = []
        _products = d.pop("products", UNSET)
        for products_item_data in _products or []:
            products_item = Product.from_dict(products_item_data)

            products.append(products_item)

        exchanges = []
        _exchanges = d.pop("exchanges", UNSET)
        for exchanges_item_data in _exchanges or []:
            exchanges_item = Exchange.from_dict(exchanges_item_data)

            exchanges.append(exchanges_item)

        spread_definitions = []
        _spread_definitions = d.pop("spreadDefinitions", UNSET)
        for spread_definitions_item_data in _spread_definitions or []:
            spread_definitions_item = SpreadDefinition.from_dict(spread_definitions_item_data)

            spread_definitions.append(spread_definitions_item)

        commands = []
        _commands = d.pop("commands", UNSET)
        for commands_item_data in _commands or []:
            commands_item = Command.from_dict(commands_item_data)

            commands.append(commands_item)

        command_reports = []
        _command_reports = d.pop("commandReports", UNSET)
        for command_reports_item_data in _command_reports or []:
            command_reports_item = CommandReport.from_dict(command_reports_item_data)

            command_reports.append(command_reports_item)

        execution_reports = []
        _execution_reports = d.pop("executionReports", UNSET)
        for execution_reports_item_data in _execution_reports or []:
            execution_reports_item = ExecutionReport.from_dict(execution_reports_item_data)

            execution_reports.append(execution_reports_item)

        order_versions = []
        _order_versions = d.pop("orderVersions", UNSET)
        for order_versions_item_data in _order_versions or []:
            order_versions_item = OrderVersion.from_dict(order_versions_item_data)

            order_versions.append(order_versions_item)

        fills = []
        _fills = d.pop("fills", UNSET)
        for fills_item_data in _fills or []:
            fills_item = Fill.from_dict(fills_item_data)

            fills.append(fills_item)

        order_strategies = []
        _order_strategies = d.pop("orderStrategies", UNSET)
        for order_strategies_item_data in _order_strategies or []:
            order_strategies_item = OrderStrategy.from_dict(order_strategies_item_data)

            order_strategies.append(order_strategies_item)

        order_strategy_links = []
        _order_strategy_links = d.pop("orderStrategyLinks", UNSET)
        for order_strategy_links_item_data in _order_strategy_links or []:
            order_strategy_links_item = OrderStrategyLink.from_dict(order_strategy_links_item_data)

            order_strategy_links.append(order_strategy_links_item)

        user_properties = []
        _user_properties = d.pop("userProperties", UNSET)
        for user_properties_item_data in _user_properties or []:
            user_properties_item = UserProperty.from_dict(user_properties_item_data)

            user_properties.append(user_properties_item)

        properties = []
        _properties = d.pop("properties", UNSET)
        for properties_item_data in _properties or []:
            properties_item = Property.from_dict(properties_item_data)

            properties.append(properties_item)

        user_plugins = []
        _user_plugins = d.pop("userPlugins", UNSET)
        for user_plugins_item_data in _user_plugins or []:
            user_plugins_item = UserPlugin.from_dict(user_plugins_item_data)

            user_plugins.append(user_plugins_item)

        order_strategy_types = []
        _order_strategy_types = d.pop("orderStrategyTypes", UNSET)
        for order_strategy_types_item_data in _order_strategy_types or []:
            order_strategy_types_item = OrderStrategyType.from_dict(order_strategy_types_item_data)

            order_strategy_types.append(order_strategy_types_item)

        sync_message = cls(
            users=users,
            contract_groups=contract_groups,
            accounts=accounts,
            account_risk_statuses=account_risk_statuses,
            margin_snapshots=margin_snapshots,
            user_account_auto_liqs=user_account_auto_liqs,
            cash_balances=cash_balances,
            currencies=currencies,
            positions=positions,
            fill_pairs=fill_pairs,
            orders=orders,
            contracts=contracts,
            contract_maturities=contract_maturities,
            products=products,
            exchanges=exchanges,
            spread_definitions=spread_definitions,
            commands=commands,
            command_reports=command_reports,
            execution_reports=execution_reports,
            order_versions=order_versions,
            fills=fills,
            order_strategies=order_strategies,
            order_strategy_links=order_strategy_links,
            user_properties=user_properties,
            properties=properties,
            user_plugins=user_plugins,
            order_strategy_types=order_strategy_types,
        )

        sync_message.additional_properties = d
        return sync_message

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
