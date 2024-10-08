import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import MultipleLocator
import pandas as pd
import numpy as np
from scipy.stats import norm

def plot_normal_distribution(trend, volatility):
    """
    :param trend: mean
    :param volatility: std
    """
    mean = trend  
    std_dev = volatility  

    # X
    x = np.linspace(mean - 4 * std_dev, mean + 4 * std_dev, 1000)
    # Y
    y = norm.pdf(x, mean, std_dev)

    # plot
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label='Normal Distribution', color='blue')
    plt.title('Normal Distribution with Trend and Volatility')
    plt.xlabel('Value')
    plt.ylabel('Probability Density')
    plt.axvline(mean, color='red', linestyle='--', label='Mean (Trend)')
    plt.axvline(mean + std_dev, color='green', linestyle='--', label='1 Std Dev')
    plt.axvline(mean - std_dev, color='green', linestyle='--')
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_procurement(df, start_date, end_date, procurement_date):
    # Convert input dates to datetime if they are not already
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)
    procurement_date = pd.to_datetime(procurement_date)

    # Filter the DataFrame for the given date range
    df_filtered = df[(df["Dates"] >= start_date) & (df["Dates"] <= end_date)]

    # Plot the price data
    plt.figure(figsize=(10, 6))
    plt.plot(df_filtered["Dates"], df_filtered["Price"], label="Price", color="blue")

    # Highlight the procurement point
    procurement_price = df.loc[df["Dates"] == procurement_date, "Price"].values[0]
    plt.scatter(
        procurement_date,
        procurement_price,
        color="red",
        label=f"Procurement Date {procurement_date.date()} \nPrice: {np.round(procurement_price,2)}EUR/MWh",
        zorder=5,
    )

    # Adding labels and title
    plt.title("Electricity Prices (EUR/MWh)")
    plt.xlabel("Date")
    plt.ylabel("Price (EUR/MWh)")
    plt.legend()

    # Adding a grid
    plt.grid(True)

    # Format x-axis for major and minor ticks
    ax = plt.gca()  # Get current axis

    # Set major ticks as months
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))

    # Set minor ticks as days (without labels)
    ax.xaxis.set_minor_locator(mdates.DayLocator())

    # Rotate the major tick labels for better readability
    plt.xticks(rotation=45)

    plt.margins(0)

    # Adjust y-ticks
    plt.yticks(
        np.arange(
            int(df_filtered["Price"].min()), int(df_filtered["Price"].max()) + 2, 1
        )
    )

    ax.yaxis.set_minor_locator(MultipleLocator(1))

    # Enable grid for minor ticks (y-axis)
    ax.grid(True, which="minor")

    # Hide minor y-tick labels
    ax.tick_params(axis="y", which="minor", labelleft=False, direction="in")

    ax.tick_params(axis="x", which="minor", labelleft=False, direction="in")

    # Tight layout for better spacing
    plt.tight_layout()

    # Show the plot
    plt.show()


def plot_all_procurement(df, procurement_results):
    plt.figure(figsize=(20, 8))

    # Plot the whole year price path
    plt.plot(df["Dates"], df["Price"], label="Price Data", color="blue")

    # Create a single scatter plot for all procurement points
    procurement_dates = [result["procurement_date"] for result in procurement_results.values()]
    procurement_prices = [result["procurement_price"] for result in procurement_results.values()]

    # Scatter plot for procurement points with a single label
    plt.scatter(
        procurement_dates,
        procurement_prices,
        label="Procurement Point",
        color="red",
        zorder=5,
    )

    # Add text labels for procurement points
    for procurement_date, procurement_price in zip(
        procurement_dates, procurement_prices
    ):
        plt.text(
            procurement_date,
            procurement_price + 0.5,
            f"{procurement_date.date()}\n{procurement_price:.2f}",
            fontsize=9,
            verticalalignment="bottom",
            horizontalalignment="center",
        )

    # Add title and labels
    plt.title("Electricity Prices and Procurement Points for 2025")
    plt.xlabel("Date")
    plt.ylabel("Price (EUR/MWh)")
    plt.legend()
    plt.grid(True)
    plt.margins(0)

    # Show the plot
    plt.tight_layout()
    plt.show()

def plot_simulations(df_simulations, simulations):
    """
    Plots the Monte Carlo simulated electricity price paths.
    
    Parameters:
        df_simulations (pd.DataFrame): DataFrame containing the simulated price paths.
        simulations (int): The number of simulations to display.
    """
    # Create the plot
    plt.figure(figsize=(20, 6))
    
    # Plot each simulation
    for i in range(simulations):
        plt.plot(df_simulations.index, df_simulations.iloc[:, i], lw=1)
        
    # Set plot title and labels
    plt.title(f'Monte Carlo Simulated Electricity Price Paths ({simulations} Simulations)')
    plt.xlabel('Date')
    plt.ylabel('Price (EUR/MWh)')
    plt.grid(True)
    
    # Show the plot
    plt.show()