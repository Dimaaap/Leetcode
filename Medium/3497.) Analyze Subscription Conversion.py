import pandas as pd


def analyze_subscription_conversion(user_activity: pd.DataFrame) -> pd.DataFrame:
    df = user_activity[user_activity["activity_type"] != "cancelled"]

    grouped = (
        df.groupby(["user_id", "activity_type"])["activity_duration"].mean().reset_index()
    )

    grouped["activity_duration"] = (
        grouped["activity_duration"].
        apply(lambda x: x + 0.0001, 2)
    )

    trial = grouped[grouped["activity_type"] == "free_trial"][["user_id", "activity_duration"]]
    trial = trial.rename(columns={"activity_duration": "trial_avg_duration"})

    paid = grouped[grouped["activity_type"] == "paid"][["user_id", "activity_duration"]]
    paid = paid.rename(columns={"activity_duration": "paid_avg_duration"})

    result = pd.merge(trial, paid, on="user_id", how="inner")
    result = result.sort_values("user_id").reset_index(drop=True)
    return result

data = [
    [1, '2023-01-01', 'free_trial', 45], [1, '2023-01-02', 'free_trial', 30], [1, '2023-01-05', 'free_trial', 60],
    [1, '2023-01-10', 'paid', 75], [1, '2023-01-12', 'paid', 90], [1, '2023-01-15', 'paid', 65],
    [2, '2023-02-01', 'free_trial', 55], [2, '2023-02-03', 'free_trial', 25], [2, '2023-02-07', 'free_trial', 50],
    [2, '2023-02-10', 'cancelled', 0], [3, '2023-03-05', 'free_trial', 70], [3, '2023-03-06', 'free_trial', 60],
    [3, '2023-03-08', 'free_trial', 80], [3, '2023-03-12', 'paid', 50], [3, '2023-03-15', 'paid', 55],
    [3, '2023-03-20', 'paid', 85], [4, '2023-04-01', 'free_trial', 40], [4, '2023-04-03', 'free_trial', 35],
    [4, '2023-04-05', 'paid', 45], [4, '2023-04-07', 'cancelled', 0]
]
columns = ['user_id', 'activity_date', 'activity_type', 'activity_duration']
user_activity_frame = pd.DataFrame(data, columns=columns)

print(analyze_subscription_conversion(user_activity_frame))