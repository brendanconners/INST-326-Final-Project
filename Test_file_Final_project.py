from argparse import ArgumentParser
import Player_class_final_project as pc
import sys
import pandas as pd

all_args = sys.argv[1:]


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('--player1', required=True, help='name of first player')
    parser.add_argument('--player2',required=True, help = 'name of second player')
    args = parser.parse_args()
    return args

def main(player1, player2):
    print(f"trying to compare {player1} and {player2} with eachother? ")
    player1info = fant_football[fant_football["Player"] == player1]
    player2info = fant_football[fant_football["Player"] == player2]
    comparasin = pd.concat([player1info,player2info], axis = 0,ignore_index=True)
    print(comparasin)


def parse_args2():
    parser = ArgumentParser()
    parser.add_argument('--player', required=True, help='Name of player')
    parser.add_argument('--position', required=True, help='Position of player')
    args = parser.parse_args()
    return args
def calc_fantasy_points_and_usage(newplayer, player_pos):
    selected_row = fant_football.loc[fant_football["Player"] == player_name]
    for index, row in selected_row.iterrows():
        print(f"your player {player_name} had " + str(row["FantPt"])  + " fantasy points this season! ")      
    right_df = []
    RB_df['Use / Game'] = (RB_df['RushingAtt'] + RB_df['Y/A']) / RB_df['G']
    QB_df['Use / Game'] = (QB_df['PassingAtt'] + QB_df['PassingAtt']) / QB_df['G']
    WR_df['Use / Game'] = (WR_df['Rec'] + WR_df['Y/R']) / WR_df['G']
    TE_df['Use / Game'] = (TE_df['RushingAtt'] + TE_df['Y/R'] + TE_df['Y/A']) / TE_df['G']
    if player_pos == "RB":
        right_df = RB_df
    elif player_pos == "QB":
        right_df = QB_df
    elif player_pos == "WR":
        right_df = WR_df
    elif player_pos == "TE":
        right_df = TE_df
    else:
        print("sorry! are you sure thats the right name / number? if so call the function again.")
        pass
    correct_row = right_df.loc[right_df["Player"] == player_name]
    for index, row in correct_row.iterrows():
            print(f"your player {player_name} had a usage rating of " + str(row["Use / Game"]))




if __name__ == "__main__":
    args = parse_args()
    main(args.player1,args.player2)
    args2 = parse_args2()
    calc_fantasy_points_and_usage(args2.newplayer, args2.player_pos)
    #python INST326_Final_project.py --player "Player Name" --position "Position"
