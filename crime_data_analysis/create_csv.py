import pandas as pd

# Create clean CSV with 2020-2022 crime data
data = {
    "State/UT": [
        "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa",
        "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala",
        "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland",
        "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura",
        "Uttar Pradesh", "Uttarakhand", "West Bengal", "Andaman and Nicobar Islands",
        "Chandigarh", "Dadra and Nagar Haveli and Daman and Diu", "Delhi", "Jammu and Kashmir",
        "Ladakh", "Lakshadweep", "Puducherry"
    ],
    "2020": [
        188997,2244,111558,194698,65216,3393,381849,103276,14803,51033,106350,149099,
        283881,394017,2349,2871,1787,1022,108533,49870,193279,504,891700,135885,4010,
        355110,13812,158060,482,2583,441,249192,25233,387,107,6725
    ],
    "2021": [
        179611,2626,119883,186006,70519,2099,273056,112720,13041,47684,115728,142643,
        304066,367218,2484,2672,2467,1033,124956,46454,214552,532,322852,146131,4133,
        357905,15704,157498,386,2401,490,291904,27447,519,89,3851
    ],
    "2022": [
        158547,2308,59315,211079,73822,2711,134600,125435,13231,48726,129461,235858,
        298578,374038,3029,2914,3587,1008,143414,43738,236090,549,193913,151849,3653,
        401787,16967,156503,460,2941,1184,300429,25915,439,64,3237
    ]
}

df = pd.DataFrame(data)

# Save CSV to the same folder as your app.py
df.to_csv("Crime_dats_clean.csv", index=False)
print("CSV created successfully: Crime_dats_clean.csv")
