import pandas as pd
from plot import plot_procurement, plot_all_procurement
import numpy as np


def dynamic_stop_loss(df, start_date, end_date, spread):
    # dynamic stop loss is to procure when the price exceed the limit_price(current + spread)
    # The limit price is downward dynamic and upward static

    current_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    current_price = df.loc[df["Dates"] == current_date, "Price"].values[0]
    limit_price = current_price + spread

    while current_date < end_date:
        next_date = current_date + pd.Timedelta(days=1)

        # check if the date exist
        if not (next_date in df["Dates"].values):
            print(f"Warning: {next_date} not found in data")
            break

        next_date_price = df.loc[df["Dates"] == next_date, "Price"].values[0]

        if next_date_price <= limit_price:
            if (
                next_date_price <= current_price
            ):  # when the new price is lower than the previous lowest,
                current_price = next_date_price
                limit_price = (
                    current_price + spread
                )  # the limit price is downward dynamic
            current_date = next_date
        else:
            procurement_date, procurement_price = next_date, next_date_price
            # plot_procurement(df, start_date, end_date, procurement_date)
            return procurement_date, procurement_price

    procurement_date = end_date
    procurement_price = df.loc[df["Dates"] == procurement_date, "Price"].values[0]

    return procurement_date, procurement_price


def quarterly_procurement(df, spread):
    quarters = {
        "Q1": {"start_date": "2024-01-01", "end_date": "2024-03-31"},
        "Q2": {"start_date": "2024-04-01", "end_date": "2024-06-30"},
        "Q3": {"start_date": "2024-07-01", "end_date": "2024-09-30"},
        "Q4": {"start_date": "2024-10-01", "end_date": "2024-12-31"},
    }

    procurement_results = {}

    # For every quarter, use dynamic_stop_loss
    for quarter, dates in quarters.items():
        start_date, end_date = dates["start_date"], dates["end_date"]

        # call dynamic_stop_loss function
        procurement_date, procurement_price = dynamic_stop_loss(
            df, start_date, end_date, spread
        )

        # store the procurement results in a dictionary
        procurement_results[quarter] = {
            "procurement_date": procurement_date,
            "procurement_price": np.round(procurement_price, 2),
        }

    # plot the whole year price path and all the procurement points

    # plot_all_procurement(df, procurement_results)

    # Print results for each quarter

    # for quarter, result in procurement_results.items():
    #     print(
    #         f"{quarter}: Procurement Date - {result['procurement_date'].date()}, Procurement Price - {result['procurement_price']}"
    #     )

    return procurement_results
