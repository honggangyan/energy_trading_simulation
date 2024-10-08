import numpy as np

# simulation for one path
def price_path_simulation(trend, initial_price, volatility, days):
    # initialize the price data
    prices = np.zeros(days)
    prices[0] = initial_price

    for t in range(1, days):
        # simulate the price
        daily_return = np.random.normal(trend, volatility)
        prices[t] = prices[t - 1] * np.exp(daily_return)

    return prices

# Monte Carlo simulation for multiple price paths
def monte_carlo_simulation(initial_price, mu, sigma, days, simulations):
    price_matrix = np.zeros((simulations, days))
    price_matrix[:, 0] = initial_price

    for t in range(1, days):
        # Generate daily returns based on normal distribution (drift + volatility)
        random_returns = np.random.normal(mu, sigma, simulations)
        price_matrix[:, t] = price_matrix[:, t - 1] * np.exp(random_returns)
    
    return price_matrix