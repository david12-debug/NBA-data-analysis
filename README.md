# NBA-data-analysis

Data based on the NBA 25-26 SZN

Features:
1.  Rank Column: Finds the top five and bottom five players in chosen column in CSV (except for PLAYER_ID, PLAYER, TEAM_ID, and TEAM)
2.  Longevity: Finds the top five and bottom five players in total minutes played over total games played
3.  Free Throw Merchant: Finds the top five (free throw merchant) and bottom five (ethical hooper) players. Calculated by finding two metrics: Free Throw Rate (FTR) (free throws attempted over field goals attempted), and Free Throws Attempted per Thirty-Six Minutes (free throws attempted over total minutes played, times thirty-six). Players who played less than 58 games or have less than 1,000 minutes are excluded.