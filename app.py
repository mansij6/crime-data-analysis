import streamlit as st
import pandas as pd
import numpy as np

# --------------------------
# Load Data
# --------------------------
import os

file_path = os.path.join(os.path.dirname(__file__), "Crime_dats_2025.csv")
data = pd.read_csv(file_path)


# --------------------------
# Sidebar - Selection
# --------------------------
st.sidebar.header("Crime Data Analysis")
state_selected = st.sidebar.selectbox("Select State/UT", sorted(data["State/UT"].unique()))
year_selected = st.sidebar.selectbox("Select Year", ['2020','2021','2022','2023','2024','2025'])


# --------------------------
# State-wise Table
# --------------------------
st.title("🕵️ Crime Data Analysis & Visualization")
st.header(f"Crime Data for {state_selected}")

state_data = data[data['State/UT'] == state_selected]
st.dataframe(state_data)

# Highlight the max crime year for this state
max_year_value = state_data[['2020','2021','2022','2023','2024','2025']].max(axis=1).values[0]
max_year = state_data[['2020','2021','2022','2023','2024','2025']].idxmax(axis=1).values[0]
st.success(f"📌 Highest crime in {state_selected} was in **{max_year}** with **{max_year_value} cases**.")

# --------------------------
# Year-wise Trend Line Chart with arrows
# --------------------------
st.subheader(f"Year-wise Crime Trend for {state_selected}")
state_trend = state_data.melt(
    id_vars=['State/UT'], 
    value_vars=['2020','2021','2022','2023','2024','2025'],
    var_name='Year', value_name='Total_Crimes'
)

# Calculate year-to-year changes
state_trend['Change'] = state_trend['Total_Crimes'].diff().fillna(0)
state_trend['Arrow'] = state_trend['Change'].apply(lambda x: "🔺" if x>0 else ("🔻" if x<0 else "➡️"))

# Display line chart
st.line_chart(state_trend.set_index('Year')['Total_Crimes'])

# Show trend arrows
trend_text = ""
for idx, row in state_trend.iterrows():
    trend_text += f"{row['Year']}: {row['Total_Crimes']} {row['Arrow']}  \n"
st.markdown(f"**Year-to-Year Change:**  \n{trend_text}")

# --------------------------
# Location-based Trend - Top 5 Crime-prone States
# --------------------------
st.subheader(f"Top 5 Crime-prone States in {year_selected}")
top_states = data[['State/UT', year_selected]].sort_values(by=year_selected, ascending=False).head(5)

# Color high/low values
def color_crime(val):
    if val > top_states[year_selected].mean():
        color = 'background-color: #ff9999'  # redish for high crime
    else:
        color = 'background-color: #99ff99'  # greenish for low crime
    return color

st.dataframe(top_states.style.applymap(color_crime, subset=[year_selected]))
st.bar_chart(top_states.set_index('State/UT'))

# --------------------------
# Full table for all states for selected year
# --------------------------
st.subheader(f"Crime Data for All States in {year_selected}")
all_states = data[['State/UT', year_selected]].sort_values(by=year_selected, ascending=False)
st.dataframe(all_states.style.applymap(color_crime, subset=[year_selected]))
