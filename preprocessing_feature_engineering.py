
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Simulated dataset
np.random.seed(42)
df = pd.DataFrame({
    "Age": np.random.randint(18, 65, 200),
    "Income": np.random.normal(7000, 3000, 200),
    "Balance": np.random.normal(15000, 5000, 200),
    "Gender": np.random.choice(["Male", "Female"], 200),
    "Satisfaction": np.random.choice(["Low", "Medium", "High"], 200)
})

# Introduce missing values
df.loc[np.random.choice(df.index, 10), "Income"] = np.nan
df.loc[np.random.choice(df.index, 8), "Gender"] = np.nan

# Missing value handling
df["Income"].fillna(df["Income"].median(), inplace=True)
df["Gender"].fillna(df["Gender"].mode()[0], inplace=True)

# One-Hot Encoding
df_encoded = pd.get_dummies(df, drop_first=True)

# Outlier handling using IQR
for col in ["Income", "Balance"]:
    Q1 = df_encoded[col].quantile(0.25)
    Q3 = df_encoded[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    df_encoded[col] = np.clip(df_encoded[col], lower, upper)

# Scaling
scaler = StandardScaler()
scaled_cols = ["Age", "Income", "Balance"]
df_encoded[scaled_cols] = scaler.fit_transform(df_encoded[scaled_cols])

# Save final dataset
df_encoded.to_csv("preprocessed_dataset.csv", index=False)
