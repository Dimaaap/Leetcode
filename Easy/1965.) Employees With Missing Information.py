import pandas as pd


def find_employees(employees: pd.DataFrame, salaries: pd.DataFrame) -> pd.DataFrame:
    df = employees.merge(salaries, how='left', on='employee_id')
    df2 = salaries.merge(employees, how='left', on='employee_id')
    total = pd.concat([df, df2])
    null_values = (
        total
        .loc[total["name"].isnull() | total["salary"].isnull(), "employee_id"]
    )
    return null_values.to_frame().sort_values("employee_id")



data = [[2, 'Crew'], [4, 'Haven'], [5, 'Kristian']]
employees_df = pd.DataFrame(data, columns=['employee_id', 'name']).astype({'employee_id':'Int64', 'name':'object'})
data = [[5, 76071], [1, 22517], [4, 63539]]
salaries_df = pd.DataFrame(data, columns=['employee_id', 'salary']).astype({'employee_id':'Int64', 'salary':'Int64'})

print(find_employees(employees_df, salaries_df))