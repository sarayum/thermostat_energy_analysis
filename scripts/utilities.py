# coding: utf-8

import pandas as pd
import matplotlib.pyplot as plt

# Utility functions for quick profiling and inspection of DataFrames

# General Data Inspection

def profile_dataframe_overview(df: pd.DataFrame, preview_rows: int = 5, include_info: bool = True) -> None:
    """
    Provides an initial overview of the DataFrame including its structure,
    null values, value distribution, and sample data.

    Args:
        df (pd.DataFrame): The input DataFrame to examine.
        preview_rows (int): Number of rows to display from top and bottom. Default is 5.
        include_info (bool): If True, prints DataFrame info summary. Default is True.

    Returns:
        None
    """

    print("\n Basic Structure")
    print("-" * 40)
    print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
    print(f"Column Names: {list(df.columns)}")

    print("\n Data Types")
    print("-" * 40)
    print(df.dtypes)

    if include_info:
        print("\n DataFrame Summary Info")
        print("-" * 40)
        df.info()

    print("\n Missing Data Overview (%)")
    print("-" * 40)
    null_percent = df.isnull().mean().mul(100).round(2)
    has_nulls = null_percent[null_percent > 0]
    if has_nulls.empty:
        print("No missing values.")
    else:
        print(has_nulls.sort_values(ascending=False))

    print("\n Unique Values per Column")
    print("-" * 40)
    print(df.nunique().sort_values(ascending=False))

    print(f"\n Preview: First {preview_rows} Rows")
    print("-" * 40)
    print(df.head(preview_rows))

    print(f"\n Preview: Last {preview_rows} Rows")
    print("-" * 40)
    print(df.tail(preview_rows))


# Summary Stats

def summary_stats(df: pd.DataFrame) -> pd.DataFrame:
    print("\n Summary Statistics:")
    return df.describe().T.round(2)
