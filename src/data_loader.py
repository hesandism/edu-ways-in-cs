import pandas as pd
import os

REQUIRED_COLUMNS = [
    "EdLevel", "LearnCode", "YearsCodePro",
    "ConvertedCompYearly", "DevType", "Country"
]

def load_and_merge_data(data_path):
    all_dfs = []

    for file in os.listdir(data_path):
        if file.endswith(".csv"):
            year = file.split("_")[0]  # adjust based on naming
            df = pd.read_csv(os.path.join(data_path, file), low_memory=False)

            df = df[REQUIRED_COLUMNS]
            df["SurveyYear"] = int(year)

            all_dfs.append(df)

    combined_df = pd.concat(all_dfs, ignore_index=True)
    return combined_df