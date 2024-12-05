# Energy Trading Simulation

Simulations for optimizing electricity procurement strategies in utility companies.

## Overview

This project simulates electricity procurement for a utility company, aiming to analyze the dynamic stop-loss strategy for different price trends.

## Key Features

1. **Price Path Simulation** (`price_path_simulation.py`):
   - Generates price path using random sampling (geometric Brownian motion)
   - Supports various market trends (rising, falling, no trend)

2. **Procurement Strategy** (`dynamic_stop_loss.py`):
   - Implements a dynamic stop-loss approach
   - Divides the year into four quarters for targeted procurement

3. **Procurement_experiments** (`Procurement_experiments.ipynb`): 
   - Test single price path experiment

4. **Monte Carlo Analysis** (`Monte_Carlo_expectations.ipynb`):
   - Performs Monte Carlo simulations of the procurement strategy
   - Analyzes strategy performance under different market scenarios

5. **Cost Benchmarking** (`cost_benchmark.py`):
   - Compares strategy performance against average market prices
   - Calculates potential savings or losses

6. **Visualization** (`plot.py`):
   - Tools for visualizing price paths and procurement points

## Usage

1. Run `Procurement_experiments.ipynb` for basic experiments
2. Use `Monte_Carlo_expectations.ipynb` for Monte Carlo simulations and analysis

## Key Concepts

- **Geometric Brownian Motion**: Models random price fluctuations
- **Dynamic Stop-Loss**: Triggers purchases based on price movements to minimize potential losses. This strategy automatically adjusts the stop-loss threshold in response to market conditions, allowing for more flexible and responsive procurement decisions. 
- **Monte Carlo Simulation**: Enables simulations for the uncertainty and variability in price movements
