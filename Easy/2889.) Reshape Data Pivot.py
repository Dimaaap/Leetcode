import pandas as pd


def pivot_table(weather: pd.DataFrame) -> pd.DataFrame:
    weather = weather.pivot(index="month", columns="city", values="temperature")

    return weather