import numpy as np
import pandas as pd

# ---------------------------------------------------------
# 1. DATA GATHERING / CREATION
# ---------------------------------------------------------
data = {
    "Customer_ID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Age": ["25", "30", "UNKNOWN", "45", "22", "35", "120", "28"],
    "Income": [50000, 60000, np.nan, 80000, 45000, 120000, 300000, 52000],
    "Purchased": ["Yes", "No", "Yes", "No", "Yes", "Yes", "No", "Yes"],
    "Join_Date": [
        "2023-01-15",
        "2023-02-20",
        "2023-03-12",
        "2023/04/05",
        "2023-05-01",
        "InvalidDate",
        "2023-07-19",
        "2023-08-22",
    ],
}

df = pd.DataFrame(data)

# ---------------------------------------------------------
# 2. INITIAL EXPLORATION & CLEANING
# ---------------------------------------------------------
# Standardize column names
df.columns = df.columns.str.strip().str.lower()

# Convert data types safely
df["age"] = pd.to_numeric(df["age"], errors="coerce")
df["join_date"] = pd.to_datetime(df["join_date"], errors="coerce")

# ---------------------------------------------------------
# 3. HANDLING MISSING VALUES & OUTLIERS
# ---------------------------------------------------------
# Impute numeric missing values with median
df["age"] = df["age"].fillna(df["age"].median())
df["income"] = df["income"].fillna(df["income"].median())

# Handle missing date values using forward fill
df["join_date"] = df["join_date"].ffill()

# Cap age outliers
df["age"] = df["age"].clip(upper=80)

# Cap income outliers using the Interquartile Range (IQR) method
q1 = df["income"].quantile(0.25)
q3 = df["income"].quantile(0.75)
iqr = q3 - q1
upper_bound = q3 + (1.5 * iqr)

df["income"] = df["income"].clip(upper=upper_bound)

# ---------------------------------------------------------
# 4. ENCODING & SCALING
# ---------------------------------------------------------
# Binary categorical encoding
df["purchased"] = df["purchased"].map({"Yes": 1, "No": 0})

# Min-Max Normalization on 'income'
income_min = df["income"].min()
income_max = df["income"].max()
df["income_normalized"] = (df["income"] - income_min) / (income_max - income_min)

# ---------------------------------------------------------
# 5. OUTPUT & SAVE
# ---------------------------------------------------------
print("--- Final Processed Data ---")
print(df)

# Export cleaned data
df.to_csv("cleaned_dataset.csv", index=False)