import pandas as pd

def mapper():
    file_path = "./Temperature_And_Precipitation_Cities_IN/Mumbai_1990_2022_Santacruz.csv"
    
    df = pd.read_csv(file_path, parse_dates=["time"], dayfirst=True)  # Parse date
    df["year"] = df["time"].dt.year  # Extract year
    df = df[["year", "tavg"]].dropna()  # Keep only year and tavg, remove NaNs

    
    return df

