import numpy as np
from dynamic_stop_loss import quarterly_procurement
from tqdm import trange
import pandas as pd


def cost_benchmark(trend, df, procurement_results):
    if df.empty or not procurement_results:
        raise ValueError("Empty dataframe or procurement results")
    
    procurement_price = [
        result["procurement_price"] for result in procurement_results.values()
    ]
    
    volumn_per_quarter = 534*1000/4
    procurement_amounts = np.full_like(procurement_price, volumn_per_quarter)
    total_procurement_cost = np.round(np.dot(procurement_price, procurement_amounts), 2)
    average_procurement_price = total_procurement_cost/(volumn_per_quarter*4)
    
    average_price = np.round(df["Price"].mean(), 2)
    total_average_cost = np.round(average_price * 534 * 1000, 2)
    
    savings = np.round( total_average_cost -total_procurement_cost, 2)
    
    # print(f"{trend} - Averge_price: {average_price}, Average_procurement_price: {average_procurement_price}, Average Cost: {total_average_cost}, Procurement_cost: {total_procurement_cost}, Savings: {savings}")
    
    return average_price, average_procurement_price, total_average_cost, total_procurement_cost, savings

def calculate_savings_expectations(trend,df_simulations, simulations, spread):
    """
    Calculates average savings and counts positive savings from Monte Carlo simulations.

    Parameters:
        df_simulations (pd.DataFrame): DataFrame containing the simulated price paths.
        simulations (int): Number of simulations.
        spread (float): The spread used in the procurement process.

    Returns:
        average_savings (float): Average of all savings.
        count_positive (int): Number of positive savings, indicating beating the average price.
    """
    all_saving_stats = []
    
    for i in trange(simulations, desc=f"Calculating savings for {trend}"):
        df_single = pd.DataFrame({
            "Price": df_simulations.iloc[:, i]
        })
        df_single.index.name = "Dates"  
        df_single.reset_index(inplace=True)
        
        # Assuming quarterly_procurement and cost_benchmark are defined elsewhere
        procurement = quarterly_procurement(df_single, spread)
        average_price, average_procurement_price, total_average_cost, total_procurement_cost, savings = cost_benchmark("single simulation", df_single, procurement)
        
        all_saving_stats.append(savings)

    # Calculate average savings and count positive savings
    average_savings = np.mean(all_saving_stats)
    count_positive = sum(1 for s in all_saving_stats if s > 0)
    
    print(f"Results for {trend}")
    print(f"Average Savings: {average_savings}")
    print(f"Number of positive savings: {count_positive}")
    
    return average_savings, count_positive