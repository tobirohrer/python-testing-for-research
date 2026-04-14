import numpy as np
import pandas as pd
import pytest

from python_testing_research.day_ahead_market import DayAheadMarket, is_price_data_valid

@pytest.mark.parametrize('dummy_price_data, expected',
                         [
                             (pd.Series([1, 2, 3]), True),
                             (pd.Series([1, 2, 1001]), False),
                          ])
def test_is_price_data_valid(dummy_price_data, expected):
    assert is_price_data_valid(dummy_price_data) == expected

def test_market_simulates_without_failing():
    # Smoke test
    dummy_price_data = pd.Series(index=pd.date_range(start='2021-01-01 10:00', periods=100, freq='900s'),
                           data=1)
    market = DayAheadMarket(dummy_price_data)
    market.reset()
    for i in range(len(dummy_price_data)):
        market.step()
        if i % 50:
            market.send_day_ahead_trades(np.ones(24))
    assert True

def test_market_handles_trading_correctly():
    # Loop though time (use `step()`); Send trades to the market: Check if it clears and if the trade data is stored in
    # the market

    # arrange
    dummy_price_data = pd.Series(index=pd.date_range(start='2021-01-01 10:00', periods=100, freq='900s'),
                                 data=1)
    market = DayAheadMarket(dummy_price_data)
    market.reset()
    trades = np.ones(24)
    market.send_day_ahead_trades(trades)

    # act
    for _ in range(12):
        market.step()

    # assert
    # Check if trades sent to market have been cleared and equal to the trades we sent to the market
    cleared_trades_day_ahead = market.get_cleared_trades(pd.Timestamp('2021-01-02 00:00').date())
    assert (cleared_trades_day_ahead == trades).all()
    # Check if for today there are no trades, these should be represented as 0s.
    cleared_trades_day_ahead = market.get_cleared_trades(pd.Timestamp('2021-01-01 00:00').date())
    assert (cleared_trades_day_ahead == 0).all()