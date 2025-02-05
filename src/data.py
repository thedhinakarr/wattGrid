import pandas as pd

# Load the CSV data into a DataFrame
csv_file_path = '../data/raw/2025/20250101_DispatchEnergyPrices.csv'  # Replace with your file path
df = pd.read_csv(csv_file_path)

print("\n*******************************")
# Display the first few rows of the data
print("\nFirst few rows of the dataset:\n")
print(df.head())  # Shows the first 5 rows by default
print("\n*******************************\n")
# Display summary information about the dataset
print("\nDataset Information:\n\n")
print(df.info())
print("\n*******************************\n")
