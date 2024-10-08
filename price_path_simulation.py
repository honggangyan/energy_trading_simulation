import numpy as np

def price_path_simulation(trend, initial_price, volatility, days):
    # initialize the price data
    prices = np.zeros(days)
    prices[0] = initial_price

    for t in range(1, days):
        # simulate the price
        daily_return = np.random.normal(trend, volatility)
        prices[t] = prices[t - 1] * np.exp(daily_return)

    return prices
