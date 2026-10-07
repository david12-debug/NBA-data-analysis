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

column_names = df.columns.tolist()

def rank_column():
    chosen_input = input("\nEnter a column name: ").strip()

    low_cols = {col.lower(): col for col in df.columns}

    chosen_col = low_cols.get(chosen_input.lower())

    print("\nchosen_col: ", chosen_col)
    
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
    chosen_input = input("\nEnter a number: ").strip()

    chosen_feature = FEATURES.get(chosen_input)

    if chosen_feature != None:
        break_loop = chosen_feature[1]()

        if break_loop == True:
            print("\nEnded program")
            break
    else:
        print("\nInvalid number")
