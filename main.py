import pandas as pd

csv_path = 'data/nba_player_stats_2026.csv'

df = pd.read_csv(csv_path)

print("NBA 2025-26 SEASON\n")

def end_program():
    return True

def view_features():
    print("Features Menu:")

    for key, value in FEATURES.items():
        feature_name = value[0]

        print(f"{key}: {feature_name}")
    
    return False

def rank_column():
    print("E")
    return False

def longevity():
    print("E")
    return False

def ft_merchant():
    print("E")
    return False

FEATURES = {
    "1" : ("Rank Column", rank_column),
    "2" : ("Longevity", longevity),
    "3" : ("Free Throw Merchant", ft_merchant),
    "4" : ("View Features Menu", view_features),
    "5" : ("Exit", end_program),
}

view_features()

while True:
    chosen_input = input("\nEnter a number: ")

    chosen_feature = FEATURES.get(chosen_input)

    if chosen_feature != None:
        break_loop = chosen_feature[1]()

        if break_loop == True:
            break
