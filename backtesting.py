import numpy as np
from collections import defaultdict
from datetime import date, datetime, timedelta
from pandas import DataFrame, Series
from typing import Callable, List, Dict


class BacktestingEngine:
    gateway_name: str = "BACKTESTING"

    def __init__(self) -> None:
        self.vt_symbol: str = ""
        self.vt_symbol: str = ""
        self.exchange: Exchane = None
        self.start: datetime = None
        self.end: datetime = None
        self.rate: float = 0
        self.slippage: float = 0
        self.size: float = 1
        self.pricetick: float = 0
        self.risk_free: float = 0
        self.annual_days: int = 240
        self.half_life: int = 120
        self.mode: BacktestingMode = BacktestingMode.BAR

        self.strategy_class: Type[CtaTemplate] = None
        self.strategy: CtaTemplate = None
        self.tick: TickData = None
        self.bar: BarData = None
        self.datetime: datetime = None

        self.interval: Interval = None
        self.days: int = 0
        self.callback: Callable = None
        self.history_data: list = []

        self.stop_order_count: int = 0
        self.stop_orders: Dict[str, StopOrder] = {}
        self.active_stop_orders: Dict[str, StopOrder] = {}

        self.limit_order_count: int = 0
        self.limit_orders: Dict[str, OrderData] = {}
        self.active_limit_orders: Dict[str, OrderData] = {}

        self.trade_count: int = 0
        self.trades: Dict[str, TradeData] = {}

        self.logs: list = []

        self.daily_results: Dict[date, DailyResult] = {}
        self.daily_df: DataFrame = None

    def clear_data(self) -> None:
        """
        Clear all data of last backtesting
        """
        self.strategy = None
        self.tick = None
        self.bar = None
        self.datetime = None

        self.stop_order_count = 0
        self.stop_orders.clear()
        self.active_stop_orders.clear()

        self.limit_order_count = 0
        self.limit_orders.clear()
        self.active_limit_orders.clear()

        self.trade_count = 0
        self.trades.clear()

        self.logs.clear()
        self.daily_results.clear()

    def set_parameters(
        self,
        vt_symbol: str,
        interval: Interval,
        start: datetime,
        rate: float,
        slippage: float,
        size: float,
        pricetick: float,
        capital: int = 0,
        end: datetime = None,
        mode: BacktestingMode = BacktestingMode.BAR,
        risk_free: float = 0,
        annual_days: int = 240,
        half_life: int =120,
    ) -> None:
        self.mode = mode
        self.vt_symbol = vt_symbol
        self.interval = Interval(interval)
        self.rate = rate
        self.slippage = slippage
        self.size size
        self.pricetick = pricetick
        self.start = start
        self.symbol, exchange_str = self.vt_symbol.split('.')
        self.exchange = Exchange(exchange_str)
        self.capital = capital

        if not end:
            end = datetime.now()
        self.end = end.replace(hour=23, minute=59, second=59)

        self.mode = mode
        self.risk_free = risk_free
        self.annual_days = annual_days
        self.half_life = half_life
        