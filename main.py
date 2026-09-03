import pandas as pd

import sys

csv_path = 'data/nba_player_stats_2026.csv'

df = pd.read_csv(csv_path)

print("NBA 2025-26 SEASON")

def exitProgram():
    sys.exit()

FEATURES = {
    "1" : ("Rank Column", None),
    "2" : ("Longevity", None),
    "3" : ("Free Throw Merchant", None),
    "4" : ("Exit", exitProgram),
}

print("Features Menu:")

for key, value in FEATURES.items():
    featureName = value[0]

    print(f"{key}: {featureName}")
