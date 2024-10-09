import numpy as np
from typing import List, Union

# simulation for one path
def price_path_simulation(
    trend: float,
    initial_price: float,
    volatility: float,
    days: int
) -> np.ndarray:
    """
    Simulate a single price path using geometric Brownian motion.

    Args:
        trend (float): The drift parameter (daily expected return).
        initial_price (float): The starting price.
        volatility (float): The volatility parameter (standard deviation of daily returns).
        days (int): The number of days to simulate.

    Returns:
        np.ndarray: An array of simulated daily prices.
    """
    prices = np.zeros(days)
    prices[0] = initial_price

    # Generate all random returns at once
    daily_returns = np.random.normal(trend, volatility, days - 1)
    
    # Calculate cumulative returns
    cumulative_returns = np.cumsum(daily_returns)
    
    # Calculate all prices at once
    prices[1:] = initial_price * np.exp(cumulative_returns)

    return prices

# Monte Carlo simulation for multiple price paths
def monte_carlo_simulation(
    initial_price: float,
    mu: float,
    sigma: float,
    days: int,
    simulations: int
) -> np.ndarray:
    """
    Perform Monte Carlo simulation for multiple price paths.

    Args:
        initial_price (float): The starting price.
        mu (float): The drift parameter (daily expected return).
        sigma (float): The volatility parameter (standard deviation of daily returns).
        days (int): The number of days to simulate.
        simulations (int): The number of simulation paths to generate.

    Returns:
        np.ndarray: A 2D array of simulated prices, shape (simulations, days).
    """
    # Generate all random returns at once
    random_returns = np.random.normal(mu, sigma, (simulations, days - 1))
    
    # Calculate cumulative returns
    cumulative_returns = np.cumsum(random_returns, axis=1)
    
    # Initialize price matrix
    price_matrix = np.zeros((simulations, days))
    price_matrix[:, 0] = initial_price
    
    # Calculate all prices at once
    price_matrix[:, 1:] = initial_price * np.exp(cumulative_returns)
    
    return price_matrix
