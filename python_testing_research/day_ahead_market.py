import numpy as np
import pandas as pd

from datetime import date

class DayAheadMarket:
    def __init__(self,
                 price_data: pd.Series,):
        self.cleared_trades = pd.Series(dtype=float, index=pd.DatetimeIndex([], freq=None))
        self._tomorrows_trades = np.zeros(24)
        self.time = None
        self.price_data = price_data

        if not is_price_data_valid(self.price_data):
            raise ValueError('Price data has at least one too extreme price.')

    def reset(self) -> None:
        self.time = self.price_data.index[0]

    def step(self) -> None:
        """
        This function is called from outside in order to step through time. It clears the market if time is 12:00
        during the day.
        """
        if self.time is None:
            raise ValueError('call reset() before step()')
        self.time += pd.Timedelta(hours=1)
        if self.time.hour == 12:
            self._clear()

    def send_day_ahead_trades(self, trades: np.ndarray) -> None:
        assert len(trades) == 24
        self._tomorrows_trades = trades

    def get_cleared_trades(self, date: date) -> pd.Series:
        ts = pd.Timestamp(date)

        day_data = self.cleared_trades[
            self.cleared_trades.index.normalize() == ts
            ]

        return day_data

    def _clear(self) -> None:
        tomorrow = (self.time + pd.Timedelta(days=1)).normalize()
        hourly_index = pd.date_range(
            start=tomorrow,
            periods=24,
            freq="h",
        )
        new_trades = pd.Series(self._tomorrows_trades, index=hourly_index, dtype=float)
        self.cleared_trades = pd.concat([self.cleared_trades, new_trades])
        self._tomorrows_trades = np.zeros(24)

    def calculate_revenue(self) -> float:
        # ToDo: implement and test
        pass


def is_price_data_valid(price_data: pd.Series) -> bool:
    # Price data is only valid if all prices are less than 1000
    # It is a complicated statement which is hard to trust without tests
    return not (price_data > 1000).any()