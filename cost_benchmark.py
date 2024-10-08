import numpy as np


def cost_benchmark(trend, df, procurement_results):
    
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
    
    print(f"{trend} - Averge_price: {average_price}, Average_procurement_price: {average_procurement_price}, Average Cost: {total_average_cost}, Procurement_cost: {total_procurement_cost}, Savings: {savings}")
    
    return average_price, average_procurement_price, total_average_cost, total_procurement_cost, savings
