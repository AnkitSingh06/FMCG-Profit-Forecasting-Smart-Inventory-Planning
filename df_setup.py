import pandas as pd

def load_df(csv_path=r'C:\Users\Ankit Kumar Singh\Downloads\extended_fmcg_demand_forecasting.csv'):
    """
    Loads, cleans, and prepares the FMCG dataset.
    Returns a DataFrame with calculated Profit.
    """
    # Load dataset
    df = pd.read_csv(csv_path)

    # Preview
    print(df.head())
    print(df.info())
    print(df.describe())

    # Handle missing values
    df['Sales_Volume'] = df['Sales_Volume'].fillna(0)
    for col in df.select_dtypes(include=['float64', 'int64']).columns:
        if col != 'Sales_Volume':
            df[col] = df[col].fillna(df[col].median())

    # Convert Date to datetime
    df['Date'] = pd.to_datetime(df['Date'])

    # Sort and remove duplicates
    df = df.sort_values(by=['Product_Category', 'Store_Location', 'Date']).drop_duplicates()

    # Calculate Profit
    df['Profit'] = (df['Price'] - df['Supplier_Cost']) * df['Sales_Volume']

    return df
