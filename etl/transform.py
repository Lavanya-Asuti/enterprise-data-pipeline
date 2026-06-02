import pandas as pd
def transform(df):

    # Remove null values
    df = df.dropna()

    # Convert timestamp
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Feature engineering
    df['is_high_value'] = df['amount'] > 50000

    print("Data transformed")
    return df