# Energy Trading Simulation

An simulation for optimizing electricity procurement strategies in utility companies.

## Overview

This project simulates electricity procurement for a utility company, aiming to analyze the dynamic stop loss strategies for different price trends.

## Key Features

1. **Price Path Simulation** (`price_path_simulation.py`):
   - Generates price path using random sampling (geometric Brownian motion)
   - Supports various market trends (rising, falling, no trend)

2. **Procurement Strategy** (`dynamic_stop_loss.py`):
   - Implements a dynamic stop-loss approach
   - Divides the year into four quarters for targeted procurement

3. **Cost Benchmarking** (`cost_benchmark.py`):
   - Compares strategy performance against average market prices
   - Calculates potential savings or losses

4. **Visualization** (`plot.py`):
   - Tools for visualizing price paths and procurement points

5. **Monte Carlo Analysis** (`Monte_Carlo_expectations.ipynb`):
   - Performs Monte Carlo simulations of the procurement strategy
   - Analyzes strategy performance under different market scenarios

## Project Structure

- `price_path_simulation.py`: Price path generation functions
- `dynamic_stop_loss.py`: Stop-loss strategy implementation
- `cost_benchmark.py`: Cost comparison functions
- `plot.py`: Data visualization tools
- `Procurement_experiments.ipynb`: Single price path experiment notebook
- `Monte_Carlo_expectations.ipynb`: Monte Carlo simulation and the expections of the performance on each trend.
- `.gitignore`: Git ignore rules

## Usage

1. Run `Procurement_experiments.ipynb` for basic experiments
2. Use `Monte_Carlo_expectations.ipynb` for monte carlo simulations and analysis

## Key Concepts

- **Geometric Brownian Motion**: Models random price fluctuations
- **Dynamic Stop-Loss**: Triggers purchases based on price movements
- **Monte Carlo Simulation**: Enables multiple scenario analyses

