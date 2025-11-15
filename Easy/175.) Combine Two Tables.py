import pandas as pd
import numpy as np


def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    merged_df = (pd.merge(person, address, on="personId", how="left")
                 .drop("personId", axis=1).drop("addressId", axis=1))
    merged_df.replace(np.nan, None, inplace=True)
    return merged_df


data = [[1, 'Wang', 'Allen'], [2, 'Alice', 'Bob']]
person_df = pd.DataFrame(data, columns=['personId', 'firstName', 'lastName']).astype({'personId':'Int64', 'firstName':'object', 'lastName':'object'})
data = [[1, 2, 'New York City', 'New York'], [2, 3, 'Leetcode', 'California']]
address_df = pd.DataFrame(data, columns=['addressId', 'personId', 'city', 'state']).astype({'addressId':'Int64', 'personId':'Int64', 'city':'object', 'state':'object'})

print(combine_two_tables(person_df, address_df))