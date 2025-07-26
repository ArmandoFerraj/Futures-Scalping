import yfinance as yf
import pandas as pd
import data_formatter

path_to_logs = r"C:\Users\aferr\Projects\futures-scalping\data\logs\data_logs.txt"
path_to_master_file = r"C:\Users\aferr\Projects\futures-scalping\data\raw\master_data.csv"
master_df = pd.read_csv(path_to_master_file)
master_initial_length = len(master_df)

raw_data = yf.download("MES=F NQ=F ^VIX GC=F SI=F CL=F 6E=F ZC=F NG=F ZS=F 6B=F 6J=F", interval="1m", period="7d")
flat_data = data_formatter.flatten_headers(raw_data)
data_formatter.append_to_master_csv(flat_data, master_df, path_to_master_file)

updated_master_df = pd.read_csv(path_to_master_file) #re read CSV to get updated length
data_formatter.logger(master_initial_length, updated_master_df, path_to_logs)