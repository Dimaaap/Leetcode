import pandas as pd


def get_dataframe_size(players: pd.DataFrame) -> list[int]:
    rows, cols = players.shape
    return [rows, cols]


