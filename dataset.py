import pandas as pd # type: ignore

# Creating a more comprehensive IPL matches dataset
data = {
    "match_id": range(1, 21),
    "batting_team": [
        "Sunrisers Hyderabad", "Mumbai Indians", "Royal Challengers Bangalore",
        "Kolkata Knight Riders", "Kings XI Punjab", "Chennai Super Kings",
        "Rajasthan Royals", "Delhi Capitals", "Sunrisers Hyderabad",
        "Mumbai Indians", "Royal Challengers Bangalore", "Kolkata Knight Riders",
        "Kings XI Punjab", "Chennai Super Kings", "Rajasthan Royals",
        "Delhi Capitals", "Sunrisers Hyderabad", "Mumbai Indians",
        "Royal Challengers Bangalore", "Kolkata Knight Riders"
    ],
    "bowling_team": [
        "Mumbai Indians", "Royal Challengers Bangalore", "Kolkata Knight Riders",
        "Kings XI Punjab", "Chennai Super Kings", "Rajasthan Royals",
        "Delhi Capitals", "Sunrisers Hyderabad", "Mumbai Indians",
        "Royal Challengers Bangalore", "Kolkata Knight Riders", "Kings XI Punjab",
        "Chennai Super Kings", "Rajasthan Royals", "Delhi Capitals",
        "Sunrisers Hyderabad", "Mumbai Indians", "Royal Challengers Bangalore",
        "Kolkata Knight Riders", "Kings XI Punjab"
    ],
    "city": [
        "Hyderabad", "Bangalore", "Mumbai", "Kolkata", "Delhi",
        "Chennai", "Jaipur", "Ahmedabad", "Hyderabad", "Mumbai",
        "Bangalore", "Kolkata", "Delhi", "Chennai", "Jaipur",
        "Ahmedabad", "Hyderabad", "Mumbai", "Bangalore", "Kolkata"
    ],
    "score": [
        150, 160, 180, 170, 150, 200, 160, 140, 175, 145,
        185, 160, 155, 190, 165, 170, 150, 180, 165, 175
    ],
    "target": [
        160, 170, 190, 180, 160, 210, 170, 150, 180, 160,
        190, 175, 165, 200, 175, 180, 160, 190, 175, 185
    ],
    "overs": [
        20, 20, 20, 20, 20, 20, 20, 20, 20, 20,
        20, 20, 20, 20, 20, 20, 20, 20, 20, 20
    ],
    "wickets": [
        8, 5, 6, 4, 7, 3, 6, 9, 4, 7,
        5, 6, 4, 3, 7, 5, 8, 4, 3, 5
    ],
    "result": [
        "Lose", "Win", "Win", "Win", "Lose", "Win",
        "Lose", "Win", "Win", "Lose",
        "Win", "Lose", "Win", "Win", "Lose",
        "Lose", "Win", "Win", "Lose", "Lose"
    ]
}

# Convert to DataFrame
ipl_matches_df = pd.DataFrame(data)

# Save to CSV
csv_file_path = 'ipl.csv'
ipl_matches_df.to_csv(csv_file_path, index=False)

csv_file_path
