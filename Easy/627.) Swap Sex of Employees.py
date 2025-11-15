import pandas as pd


def swap_salary(salary: pd.DataFrame) -> pd.DataFrame:
    salary["sex"] = salary["sex"].map({"m": "f", "f": "m"})
    return salary

data = {
    'id': [1, 2, 3, 4],
    'name': ['A', 'B', 'C', 'D'],
    'sex': ['m', 'f', 'm', 'f'],
    'salary': [2500, 1500, 5500, 500]
}
df = pd.DataFrame(data)

print(swap_salary(df))