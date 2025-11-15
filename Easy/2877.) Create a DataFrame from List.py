import pandas as pd


def create_data_frame(student_data: list[list[int]]) -> pd.DataFrame:
    df = pd.DataFrame(student_data, columns=["student_id", "age"])
    return df


print(create_data_frame(student_data=[[1,15],[2,11],[3,11],[4,20]]))

