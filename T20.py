import pandas as pd
import os
import json
folder_path = r'C:\Users\engga\OneDrive\Documents\Porkodi_guvi\Guvi_project\Streamlit\cricket\T20'
flattened_data = []
for filename in os.listdir(folder_path):
    if filename.endswith('.json'):  
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            
            info = data.get('info', {})            
            match_id = filename.split('.')[0]  
            city = info.get('city', None)
            date = info.get('dates', [None])[0]  
            season = info.get('season', None)
            match_type = info.get('match_type', None)
            gender = info.get('gender', None)
            overs = info.get('overs', None)            
            teams = info.get('teams', [None, None])
            team1 = teams[0]
            team2 = teams[1]
            venue = info.get('venue', None)            
            umpires = info.get('officials', {}).get('umpires', [None, None])
            umpire1 = umpires[0]
            umpire2 = umpires[1]
            match_referee = info.get('officials', {}).get('match_referees', [None])[0]            
            toss_winner = info.get('toss', {}).get('winner', None)
            toss_decision = info.get('toss', {}).get('decision', None)           
            winner = info.get('outcome', {}).get('winner', None)
            win_by_runs = info.get('outcome', {}).get('by', {}).get('runs', None)
            win_by_wickets = info.get('outcome', {}).get('by', {}).get('wickets', None)
            player_of_match = info.get('player_of_match', [None])[0]

            
            innings_data = data.get('innings', [])
            for inning in innings_data:
                batting_team = inning.get('team', None)
                total_runs = 0
                total_wickets = 0
                total_overs = len(inning.get('overs', []))
                player_scores = {}
                bowler_stats = {}
                for over in inning.get('overs', []):
                    for delivery in over.get('deliveries', []):
                        batter = delivery.get('batter', None)
                        bowler = delivery.get('bowler', None)
                        runs = delivery.get('runs', {}).get('batter', 0)
                        total_runs += delivery.get('runs', {}).get('total', 0)                        
                        if 'wicket' in delivery:
                            total_wickets += 1                        
                        if batter:
                            if batter not in player_scores:
                                player_scores[batter] = {'runs': 0, 'balls': 0}
                            player_scores[batter]['runs'] += runs
                            player_scores[batter]['balls'] += 1                        
                        if bowler:
                            if bowler not in bowler_stats:
                                bowler_stats[bowler] = {'runs_conceded': 0, 'balls_bowled': 0, 'wickets': 0}
                            bowler_stats[bowler]['runs_conceded'] += delivery.get('runs', {}).get('total', 0)
                            bowler_stats[bowler]['balls_bowled'] += 1
                            if 'wicket' in delivery:
                                bowler_stats[bowler]['wickets'] += 1                
                for player, stats in player_scores.items():
                    flattened_data.append({
                        'match_id': match_id,
                        'city': city,
                        'date': date,
                        'season': season,
                        'match_type': match_type,
                        'gender': gender,
                        'overs': overs,
                        'team1': team1,
                        'team2': team2,
                        'venue': venue,
                        'umpire1': umpire1,
                        'umpire2': umpire2,
                        'match_referee': match_referee,
                        'toss_winner': toss_winner,
                        'toss_decision': toss_decision,
                        'winner': winner,
                        'win_by_runs': win_by_runs,
                        'win_by_wickets': win_by_wickets,
                        'player_of_match': player_of_match,
                        'batting_team': batting_team,
                        'total_runs': total_runs,
                        'total_wickets': total_wickets,
                        'total_overs': total_overs,
                        'batter': player,
                        'runs_scored': stats['runs'],
                        'balls_faced': stats['balls'],
                        'bowler': None,
                        'runs_conceded': None,
                        'balls_bowled': None,
                        'wickets_taken': None,
                        'economy_rate': None
                    })
                for bowler, stats in bowler_stats.items():
                    overs_bowled = stats['balls_bowled'] // 6 + (stats['balls_bowled'] % 6) / 10
                    economy_rate = (stats['runs_conceded'] / overs_bowled) if overs_bowled > 0 else 0
                    flattened_data.append({
                        'match_id': match_id,
                        'city': city,
                        'date': date,
                        'season': season,
                        'match_type': match_type,
                        'gender': gender,
                        'overs': overs,
                        'team1': team1,
                        'team2': team2,
                        'venue': venue,
                        'umpire1': umpire1,
                        'umpire2': umpire2,
                        'match_referee': match_referee,
                        'toss_winner': toss_winner,
                        'toss_decision': toss_decision,
                        'winner': winner,
                        'win_by_runs': win_by_runs,
                        'win_by_wickets': win_by_wickets,
                        'player_of_match': player_of_match,
                        'batting_team': batting_team,
                        'total_runs': total_runs,
                        'total_wickets': total_wickets,
                        'total_overs': total_overs,
                        'batter': None,
                        'runs_scored': None,
                        'balls_faced': None,
                        'bowler': bowler,
                        'runs_conceded': stats['runs_conceded'],
                        'balls_bowled': stats['balls_bowled'],
                        'wickets_taken': stats['wickets'],
                        'economy_rate': round(economy_rate, 2)
                    })
final_df = pd.DataFrame(flattened_data)
output_path = r'C:\Users\engga\OneDrive\Documents\Porkodi_guvi\Guvi_project\Streamlit\cricket\T20.csv'
final_df.to_csv(output_path, index=False)
print(f" CSV file 'T20.csv' created at: {output_path}")
