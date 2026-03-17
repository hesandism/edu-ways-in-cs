def categorize_education(ed):
    if "Bachelor" in ed or "Master" in ed or "PhD" in ed:
        return "Formal"
    elif "bootcamp" in ed.lower():
        return "Bootcamp"
    else:
        return "Self-Taught"

def process_features(df):
    df = df.copy()

    df["EducationType"] = df["EdLevel"].apply(categorize_education)

    # Simplify DevType
    df["DevType"] = df["DevType"].str.split(";").str[0]

    return df