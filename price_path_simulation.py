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

def calculate_confidence_interval(
    price_paths: np.ndarray,
    confidence_level: float = 0.95
) -> List[Union[float, np.ndarray]]:
    """
    Calculate confidence interval for the simulated price paths.

    Args:
        price_paths (np.ndarray): The simulated price paths.
        confidence_level (float): The desired confidence level (default: 0.95).

    Returns:
        List[Union[float, np.ndarray]]: Lower bound, mean, and upper bound of the confidence interval.
    """
    mean_prices = np.mean(price_paths, axis=0)
    std_prices = np.std(price_paths, axis=0)
    
    z_score = np.abs(np.percentile(np.random.standard_normal(10000), (1 - confidence_level) / 2 * 100))
    
    lower_bound = mean_prices - z_score * std_prices / np.sqrt(price_paths.shape[0])
    upper_bound = mean_prices + z_score * std_prices / np.sqrt(price_paths.shape[0])
    
    return [lower_bound, mean_prices, upper_bound]

if __name__ == "__main__":
    # Example usage
    initial_price = 100
    mu = 0.0002  # Approximately 5% annual return
    sigma = 0.01  # 1% daily volatility
    days = 252  # One trading year
    simulations = 10000

    price_paths = monte_carlo_simulation(initial_price, mu, sigma, days, simulations)
    confidence_interval = calculate_confidence_interval(price_paths)

    print(f"Final price 95% confidence interval: ({confidence_interval[0][-1]:.2f}, {confidence_interval[2][-1]:.2f})")
    print(f"Expected final price: {confidence_interval[1][-1]:.2f}")