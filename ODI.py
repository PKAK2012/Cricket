import pandas as pd
import os
import json

# Define the folder path where JSON files are stored
folder_path = r'C:\Users\engga\OneDrive\Documents\Porkodi_guvi\Guvi_project\Streamlit\cricket\ODI'

# List to store extracted data
flattened_data = []

# Loop through all JSON files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.json'):  
        file_path = os.path.join(folder_path, filename)

        # Open and load JSON file
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

            # Extract match information
            info = data.get('info', {})
            match_id = filename.split('.')[0]
            city = info.get('city', None)
            date = info.get('dates', [None])[0]
            match_type = info.get('match_type', None)
            gender = info.get('gender', None)
            teams = info.get('teams', [None, None])
            team1 = teams[0]
            team2 = teams[1]
            venue = info.get('venue', None)
            umpires = info.get('officials', {}).get('umpires', [None, None])
            umpire1 = umpires[0]
            umpire2 = umpires[1]
            player_of_match = info.get('player_of_match', [None])[0]
            toss_winner = info.get('toss', {}).get('winner', None)
            toss_decision = info.get('toss', {}).get('decision', None)

            # Outcome details
            outcome = info.get('outcome', {})
            winner = outcome.get('winner', None)
            win_by_runs = outcome.get('by', {}).get('runs', 0)
            win_by_wickets = outcome.get('by', {}).get('wickets', 0)

            # Initialize team scores
            team_scores = {team1: 0, team2: 0}

            # Extract innings details
            for inning in data.get('innings', []):
                inning_name = inning.get('team', None)
                overs = inning.get('overs', [])

                for over in overs:
                    over_number = over.get('over', None)
                    deliveries = over.get('deliveries', [])

                    for delivery in deliveries:
                        batter = delivery.get('batter', None)
                        bowler = delivery.get('bowler', None)
                        non_striker = delivery.get('non_striker', None)
                        runs_batter = delivery.get('runs', {}).get('batter', 0)
                        runs_extras = delivery.get('runs', {}).get('extras', 0)
                        runs_total = delivery.get('runs', {}).get('total', 0)
                        wickets = delivery.get('wickets', [])

                        # Track total team score
                        if inning_name in team_scores:
                            team_scores[inning_name] += runs_total

                        wicket_info = None
                        if wickets:
                            wicket_info = wickets[0].get('player_out', None)

                        # Append to the data list
                        flattened_data.append({
                            'match_id': match_id,
                            'city': city,
                            'date': date,
                            'match_type': match_type,
                            'gender': gender,
                            'team1': team1,
                            'team2': team2,
                            'venue': venue,
                            'umpire1': umpire1,
                            'umpire2': umpire2,
                            'player_of_match': player_of_match,
                            'winner': winner,
                            'toss_winner': toss_winner,
                            'toss_decision': toss_decision,
                            'inning': inning_name,
                            'over': over_number,
                            'batter': batter,
                            'bowler': bowler,
                            'non_striker': non_striker,
                            'runs_batter': runs_batter,
                            'runs_extras': runs_extras,
                            'runs_total': runs_total,
                            'wicket': wicket_info,
                            'win_by_runs': win_by_runs,
                            'win_by_wickets': win_by_wickets,
                            'team1_score': team_scores[team1],
                            'team2_score': team_scores[team2]
                        })

# Convert extracted data to DataFrame
final_df = pd.DataFrame(flattened_data)

# Save to CSV file
output_path = r'C:\Users\engga\OneDrive\Documents\Porkodi_guvi\Guvi_project\Streamlit\cricket\ODII.csv'
final_df.to_csv(output_path, index=False)

print(f"CSV file 'ODII.csv' created successfully at: {output_path}")
