import pandas as pd
import matplotlib.pyplot as plt

user_data = pd.read_csv("user_sessions.csv")
weekly_activity = user_data.groupby("day_of_week")["session_duration"].mean()

plt.figure(figsize=(10, 6))
weekly_activity.plot(kind="bar")
plt.title("Средняя продолжительность сессий по дням недели")
plt.ylabel("Минуты")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.savefig("weekly_activity_report.png")
