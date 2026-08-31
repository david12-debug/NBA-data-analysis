import pandas as pd

csv_path = 'data/nba_player_stats_2026.csv'

df = pd.read_csv(csv_path)

print("NBA 2025-26 SEASON")

print("Top 5 in total points scored:")

df_total_pts = df.sort_values(by="PTS", ascending=False)

for i in range(0, 5):
    player_name = df_total_pts["PLAYER"].iloc[i]

    points_scored = df_total_pts["PTS"].iloc[i]

    print(f"{i + 1}: {player_name} scored a total of {points_scored} points")
