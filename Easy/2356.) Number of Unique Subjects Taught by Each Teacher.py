import pandas as pd


def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    new_teacher = teacher.groupby("teacher_id")["subject_id"].nunique().reset_index()

    new_teacher.columns = ["teacher_id", "cnt"]
    return new_teacher