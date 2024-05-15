import numpy as np
import pandas as pd

ipl_matches = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRy2DUdUbaKx_Co9F0FSnIlyS-8kp4aKv_I0-qzNeghiZHAI_hw94gKG22XTxNJHMFnFVKsO4xWOdIs/pub?gid=1655759976&single=true&output=csv"
matches = pd.read_csv(ipl_matches)

players_df=pd.read_csv('E:/excel/players.csv')

def player_list():
    player=list(players_df['Name'])
    player_dict={
        'players_list':player
    }
    return player_dict
def player_info(player):
    player += " "
    valid_name = list(players_df['Name'])
    if player in valid_name:
        info = {
            'Name': players_df.loc[players_df['Name'] == player, 'Name'].values[0],
            'Span': players_df.loc[players_df['Name'] == player, 'Span'].values[0],
            'Matches': players_df.loc[players_df['Name'] == player, 'Matches'].values[0],
            'Innings': players_df.loc[players_df['Name'] == player, 'Innings'].values[0],
            'Not_Out': players_df.loc[players_df['Name'] == player, 'Not_Out'].values[0],
            'Runs': players_df.loc[players_df['Name'] == player, 'Runs'].values[0],
            'Highest Score': players_df.loc[players_df['Name'] == player, 'Highest Score'].values[0],
            'Average': players_df.loc[players_df['Name'] == player, 'Average'].values[0],
            'Balls Faced': players_df.loc[players_df['Name'] == player, 'Balls Faced'].values[0],
            'Strike Rate': players_df.loc[players_df['Name'] == player, 'Strike Rate'].values[0],
            'Centuries': players_df.loc[players_df['Name'] == player, 'Centuries'].values[0],
            'Fifties': players_df.loc[players_df['Name'] == player, 'Fifties'].values[0],
            'Ducks': players_df.loc[players_df['Name'] == player, 'Ducks'].values[0],
            'Fours': players_df.loc[players_df['Name'] == player, 'Fours'].values[0],
            'Sixes': players_df.loc[players_df['Name'] == player, 'Sixes'].values[0],
            'Balls per Boundaries': players_df.loc[players_df['Name'] == player, 'Balls per Boundaries'].values[0]
        }
        return {key: str(value) if not isinstance(value, str) else value for key, value in info.items()}

    else:
        return {'message': 'invalid  player name'}

def teamAPI():
    teams= list(set(list(matches['Team1']) + list(matches['Team2'])))
    teams_dict={
        'teams':teams
    }
    return teams_dict

def teamVteamAPI(team1,team2):

    valid_teams = list(set(list(matches['Team1']) + list(matches['Team2'])))

    if team1 in valid_teams and team2 in valid_teams:

        temp_df = matches[(matches['Team1'] == team1) & (matches['Team2'] == team2) | (matches['Team1'] == team2) & (matches['Team2'] == team1)]
        total_matches = temp_df.shape[0]

        matches_won_team1 = temp_df['WinningTeam'].value_counts()[team1]
        matches_won_team2 = temp_df['WinningTeam'].value_counts()[team2]

        draws = total_matches - (matches_won_team1 + matches_won_team2)

        response = {
              'total_matches': str(total_matches),
              team1: str(matches_won_team1),
              team2: str(matches_won_team2),
              'draws': str(draws)
          }

        return response
    else:
        return {'message':'invalid team name'}