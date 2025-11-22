import pandas as pd


def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    has_primary_department = employee.loc[employee["primary_flag"] == "Y", ["employee_id", "department_id"]]

    has_one_department = (
        employee.groupby("employee_id")
        .filter(lambda x: len(x) == 1)
        [["employee_id", "department_id"]]
    )

    result = pd.concat([has_primary_department, has_one_department]).sort_values("employee_id")
    return result


data = [
    ['1', '1', 'N'],
    ['2', '1', 'Y'],
    ['2', '2', 'N'],
    ['3', '3', 'N'],
    ['4', '2', 'N'],
    ['4', '3', 'Y'],
    ['4', '4', 'N']
]
employee_df = (pd.DataFrame(data, columns=['employee_id', 'department_id', 'primary_flag'])
            .astype({'employee_id':'Int64', 'department_id':'Int64', 'primary_flag':'object'}))

print(find_primary_department(employee_df))