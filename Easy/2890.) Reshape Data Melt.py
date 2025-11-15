import pandas as pd


def melt_table(report: pd.DataFrame) -> pd.DataFrame:
    long_df = pd.melt(
        report,
        id_vars=["product"],
        var_name="quarter",
        value_name="sales"
    )

    return long_df

data = {
    'product': ['Umbrella', 'SleepingBag'],
    'quarter_1': [417, 800],
    'quarter_2': [224, 936],
    'quarter_3': [379, 93],
    'quarter_4': [611, 875]
}
report_df = pd.DataFrame(data)

reshaped = melt_table(report_df)
print(reshaped)
