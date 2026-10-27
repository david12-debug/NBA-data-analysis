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

def handle_input():
    chosen_input = input("\nEnter a column name: ").strip()

    low_cols = {col.lower(): col for col in df.columns}

    chosen_col = low_cols.get(chosen_input.lower())

    return chosen_col

def rank_column():
    chosen_col = handle_input()

    if chosen_col != None:
        print("\nTop 5:\n")

        descending_df = df.sort_values(by=chosen_col, ascending=False).reset_index(drop=True)

        top_five_list = descending_df[chosen_col].head(5).tolist()

        for i, v in enumerate(top_five_list):
            player_name = descending_df.at[i, "PLAYER"]
            print(f"{i + 1}) {player_name}: {v}")


        print("\nBottom 5:\n")

        ascending_df = df.sort_values(by=chosen_col, ascending=True).reset_index(drop=True)

        bottom_five_list = ascending_df[chosen_col].head(5).tolist()

        for i, v in enumerate(bottom_five_list):
            player_name = ascending_df.at[i, "PLAYER"]
            print(f"{i + 1}) {player_name}: {v}")
    else:
        print("\nInvalid column name")
    
    return False

def longevity():
    # Finds the top five and bottom five players in total minutes played over total games played
    print("\nTop 5:\n")

    temp_df = df.copy()

    temp_df['Longevity'] = temp_df['MIN'] / temp_df['GP']

    sorted_df = temp_df.sort_values(by='Longevity', ascending=False).reset_index(drop=True)

    print("\nTop 5:\n")

    top_five = sorted_df.head(5)

    for i, row in top_five.iterrows():
        player_name = row["PLAYER"]
        longevityValue = row['Longevity']

        print(f"{i + 1}) {player_name}: {longevityValue:.2f}")

    
    print("\nBottom 5:\n")

    bottom_five = sorted_df.tail(5)

    for i, row in bottom_five.iterrows():
        player_name = row["PLAYER"]
        longevityValue = row['Longevity']

        print(f"{i + 1}) {player_name}: {longevityValue:.2f}")

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
