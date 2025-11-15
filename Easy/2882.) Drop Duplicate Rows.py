import pandas as pd


def drop_duplicate_emails(customers: pd.DataFrame) -> pd.DataFrame:
    customers = customers.drop_duplicates(subset=["email"])
    return customers




