import numpy as np
import pandas as pd

from python_testing_research.day_ahead_market import DayAheadMarket


def create_dummy_price_series(start="2026-01-01") -> pd.Series:
    periods = 24 * 365

    index = pd.date_range(start=start, periods=periods, freq="h")

    pattern = np.array([1, 2, 3, 4])
    values = np.tile(pattern, periods // len(pattern))

    return pd.Series(values, index=index)


if __name__ == '__main__':
    dummy_price_data = create_dummy_price_series()
    market = DayAheadMarket(dummy_price_data)
    market.reset()

    # Simulation Loop
    for i in range(100):
        # Place a trade at 11, so it can be cleared at 12
        if market.time.hour == 11:
            # Ouyes, we have a very good trader here...
            trades = np.random.randint(-100, 101, size=24)
            market.send_day_ahead_trades(trades)
        market.step()
