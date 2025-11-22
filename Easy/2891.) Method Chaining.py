import pandas as pd


def find_heavy_animals(animals: pd.DataFrame) -> pd.DataFrame:
    df = animals.sort_values(by="weight", ascending=False).loc[animals["weight"] > 100, "name"].to_frame()
    return df


