import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd
import folium

# Load dataset, skipping bad lines and handling potential UnicodeDecodeErrors
try:
    df = pd.read_csv('../data/raw/POCs/Network_supply_points_table_20250206234023.csv', on_bad_lines='skip', encoding='utf-8')  # Try utf-8 encoding first
except UnicodeDecodeError:
    df = pd.read_csv('../data/raw/POCs/Network_supply_points_table_20250206234023.csv', on_bad_lines='skip', encoding='latin-1') # Try latin-1 if utf-8 fails

# # Print columns to verify the load was successful
# print(df.columns)

# Filter for relevant columns (handling potential missing columns)
required_cols = ["POC code", "NZTM easting", "NZTM northing", "Network reporting region", "Island"]
available_cols = [col for col in required_cols if col in df.columns]
df_filtered = df[available_cols]

# Display data and info
pd.set_option('display.max_rows', None)  # Set globally
print(df_filtered)
pd.reset_option('display.max_rows') #Reset the option to its default value
