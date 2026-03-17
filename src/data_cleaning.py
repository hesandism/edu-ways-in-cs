import pandas as pd
import numpy as np

def clean_data(df):
    df = df.copy()

    # Drop missing critical values
    df = df.dropna(subset=["EdLevel", "YearsCodePro", "ConvertedCompYearly"])

    # Convert YearsCodePro
    df["YearsCodePro"] = df["YearsCodePro"].replace({
        "Less than 1 year": 0,
        "More than 50 years": 50
    })

    df["YearsCodePro"] = pd.to_numeric(df["YearsCodePro"], errors='coerce')

    # Remove salary outliers
    df = df[(df["ConvertedCompYearly"] > 1000) & 
            (df["ConvertedCompYearly"] < 500000)]

    return df