import numpy as np


def procurement_cost(df, procurement_results):
    procurement_price = [result['procurement_price'] for result in procurement_results.values()]
    procurement_amount = [534/4 * 1000, 534/4* 1000, 534/4* 1000, 534/4* 1000] 
    procurement_cost = np.round( np.dot( procurement_price, procurement_amount ), 2)
    average_price = np.round(df['Price'].mean(),2)
    average_cost = average_price * 534*1000
    savings = np.round( average_cost - procurement_cost, 2)
    return procurement_cost, average_cost, savings