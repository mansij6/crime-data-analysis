import pandas as pd

# Load your current clean CSV
df = pd.read_csv("Crime_dats_clean.csv")

# Function to estimate next year crime based on average growth rate
def project_crime(row):
    # Calculate year-on-year growth rates
    growth_21 = (row['2021'] - row['2020']) / row['2020']
    growth_22 = (row['2022'] - row['2021']) / row['2021']
    avg_growth = (growth_21 + growth_22) / 2

    # Project next years
    row['2023'] = int(row['2022'] * (1 + avg_growth))
    row['2024'] = int(row['2023'] * (1 + avg_growth))
    row['2025'] = int(row['2024'] * (1 + avg_growth))
    return row

# Apply projection to each row
df_proj = df.apply(project_crime, axis=1)

# Save new CSV with projected years
df_proj.to_csv("Crime_dats_2025.csv", index=False)
print("New CSV with 2023-2025 projections created: Crime_dats_2025.csv")
