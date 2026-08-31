import pandas as pd

csv_path = 'data/nba_player_stats_2026.csv'

df = pd.read_csv(csv_path)

print(df.head())
