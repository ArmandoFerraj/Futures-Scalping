import pandas as pd
import re
from datetime import datetime, timezone

def flatten_headers(df):
    new_columns = [re.sub(r'\^', '', f"{metric}_{ticker}") for metric, ticker in df.columns] # Create list of flattened column names, removing ^ from tickers
    df.columns = new_columns
    return df

def append_to_master_csv(df, master_df, csv_path):
    df = df.reset_index()
    if not df.columns.equals(master_df.columns):
        print("Columns do not match the master CSV")
        return None
    
    non_duplicates = df[~df['Datetime'].isin(master_df['Datetime'])]
    if non_duplicates.empty:
        print("No new data to append to master CSV")
        return
    
    updated_df = pd.concat([master_df, non_duplicates], ignore_index= True)
    updated_df.to_csv(csv_path, index=False)
    print(f"Appended {len(non_duplicates)} rows to {csv_path}")
    return 

def logger(initial_length, master_df, logs_path):
    new_length = len(master_df)
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    if new_length > initial_length:
        rows_added = new_length - initial_length
        log_entry = f"{timestamp} Added {rows_added} rows\n"
    else:
        print("Logger: no new data to append to master CSV")
    
    try:
        with open(logs_path, 'a') as f:
            f.write(log_entry)
        print(f"Logged to {logs_path}")
    except Exception as e:
        print(f"Failed to write to log: {e}")

