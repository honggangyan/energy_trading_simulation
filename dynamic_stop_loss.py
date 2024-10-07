import pandas as pd
from plot import plot_procurement,plot_all_procurement

def dynamic_stop_loss(df, start_date, end_date, spread):
    current_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date) 
    current_price = df.loc[df["Dates"]==current_date, "Price"].values[0]
    limit_price = current_price + spread
    
    while current_date < end_date:
        next_date = current_date + pd.Timedelta(days = 1)
        next_date_price = df.loc[df["Dates"] == next_date, "Price"].values[0]
        
        if next_date_price <= limit_price:
            if next_date_price <= current_price:
                current_price = next_date_price
                limit_price = current_price + spread

            current_date = next_date
        else:
            procurement_date = next_date
            procurement_price = next_date_price  
            plot_procurement(df,start_date,end_date,procurement_date)
            
            return procurement_date, procurement_price    
    
    procurement_date = end_date
    procurement_price = df.loc[df["Dates"]==procurement_date, "Price"].values[0]       
    
    return procurement_date, procurement_price

def quarterly_procurement(df,spread):
    quarters = {
        "Q1":{"start_date":"2024-01-01","end_date": "2024-03-31"},
        "Q2":{"start_date":"2024-04-01","end_date": "2024-06-30"},
        "Q3":{"start_date":"2024-07-01","end_date": "2024-09-30"},
        "Q4":{"start_date":"2024-10-01","end_date": "2024-12-31"}
        }

    procurement_results = {}

    #For every quarter, use dynamic_stop_loss
    for quarter, dates in quarters.items():
        start_date = dates["start_date"]
        end_date = dates["end_date"]
        
        # 调用 dynamic_stop_loss 函数
        procurement_date, procurement_price = dynamic_stop_loss(df, start_date, end_date, spread)
        
        # 存储结果
        procurement_results[quarter] = {
            "procurement_date": procurement_date,
            "procurement_price": procurement_price
        }
    # 输出每个季度的结果
    for quarter, result in procurement_results.items():
        print(f"{quarter}: Procurement Date - {result['procurement_date']}, Procurement Price - {result['procurement_price']}")
    # plot the whole year price path and all the procurement points
    plot_all_procurement(df, procurement_results)    
    return  procurement_results