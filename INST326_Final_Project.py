import pandas as pd
import random

"""
according to the website :https://www.profootballnetwork.com/how-fantasy-football-scoring-systems-work/
this website tells us how to convert stats into points using fantasy football scoring
"""

fant_football = pd.read_csv("2019 final_project.csv")

fant_football.drop(['2PM','2PP','DKPt','FDPt','VBD','PPR', 'Fmb','GS'], 
axis = 1,
inplace = True)
fant_football.rename({'Rk': 'Rank',
            'TD':'PassingTD',
           'TD.1':'RushingTD',
           'TD.2':'ReceivingTD',
           'TD.3':'TotalTD',
           'Yds':'PassingYDs',
           'Yds.1':'RushingYDs',
           'Yds.2':'ReceivingYDs',
           'Att':'PassingAtt',
           'Att.1':'RushingAtt' },axis = 1, inplace = True)

"""
this line of code is an anonymous lambda function, that is used so I dont have to
create a whole new function to fix the name formatting of the CSV file syntax
the names came out as Christian McCaffrey*\McCach01 
"""
fant_football["Player"] = fant_football["Player"].apply(lambda x: x.split('*')[0]).apply(lambda x: x.split("\\")[0])


QB_df = fant_football[fant_football["FantPos"] == "QB"]

RB_df = fant_football[fant_football["FantPos"] == "RB"]

WR_df =fant_football[fant_football["FantPos"] == "WR"]
 
TE_df = fant_football[fant_football["FantPos"] == "TE"]



def calculating_fantasypoints(player_name):
            selected_row = fant_football.loc[fant_football["Player"] == player_name]
            for index, row in selected_row.iterrows():
                print(f"your player {player_name} had " + str(row["FantPt"])  + " fantasy points this season! ")
                



def usage_per_game(player_name,player_pos):
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

def compare_players(player1,player2):
    print(f"So you want to compare {player1} and {player2} to eachother? ")
    player1info = fant_football[fant_football["Player"] == player1]

    player2info = fant_football[fant_football["Player"] == player2]
    comparasin = pd.concat([player1info,player2info], axis = 0,ignore_index=True)
    print(comparasin)





if __name__ == "__main__":
    def snake_draft(num_of_team,csvdataframe):
        teamlist = []
        playerteam = []
        
        user_team = input("What do you want your team to be named? ")
        num_of_team -= 1
        teamlist.append(user_team)
        while num_of_team != 0:
            team_name = input("What do you want the next team to be named? ")
            teamlist.append(team_name)
            print(teamlist)
            num_of_team -= 1
        draft_order = random.shuffle(teamlist)
        draft_order_str = ", ".join(teamlist)
        print(f"So you want a Snake draft with {len(teamlist)} teams including yourself?")
        print(f"the draft order goes {draft_order_str}")
        draft_list = list(draft_order_str.split(", "))
        num_of_rounds = int(input("How Many Rounds do you want to Draft For? "))
        original_num_of_rounds = num_of_rounds
        draft_order_list = []
        player_rank = csvdataframe["Rank"]
        selected_players =  []
        
        




#iterate through each round of the draft
        for round in range(0,num_of_rounds - 1,1):
#easiest way to make a snake draft is to use even / odd for # of rounds
            if num_of_rounds % 2 == 1: # if its an odd number
                draft_order_list += draft_list
            else: #if even number
                draft_order_list += reversed(draft_list)
            for team in draft_order_list:
                if team == user_team:
                    pick = input ("Which player do you want to pick?")
                    ranking = int(input("Just so we know who you want, what is his ranking?"))
                    if ranking not in selected_players:
                        print(f"Okay! it looks like you got {pick}")
                        selected_players.append(ranking)
                        playerteam.append(pick)


                    else:
                        print("sorry, he is already on team, try again!")
                        pick = input ("Which player do you want to pick?")
                        ranking = int(input("Just so we know who you want, what is his ranking?"))
                        if ranking not in selected_players:
                            print(f"Okay! it looks like you got {pick}")
                            playerteam.append(pick)
                            selected_players.append(ranking)

                        else:
                            print("sorry they are already picked! your just going to get a random teammate ")
                            randomint = random.randint(0,200)
                            while randomint in selected_players:
                                randomint = random.randint(0,200)
                                if randomint not in selected_players:
                                    break
                            selected_row = csvdataframe.loc[csvdataframe["Rank"] == randomint]
                            selected_players.append(randomint)
                            for index,row in selected_row.iterrows():
                                player_name = str(row["Player"])
                            print(f'you ended up getting {player_name}!')
                            playerteam.append(player_name)
                            selected_players.append(randomint)
                        continue

            
                
                else:
                    randomint = random.randint(0,200)
                    while randomint in selected_players:
                        randomint = random.randint(0,200)
                        if randomint not in selected_players:
                            break

                    print(f"The team {team} is drafting next: ")
                    selected_row = csvdataframe.loc[csvdataframe["Rank"] == randomint]
                    selected_players.append(randomint)
                    for index,row in selected_row.iterrows():
                        player_name = str(row["Player"])
                    print(f"with team {team}s pick they choose {player_name}")


                    print(f"this is your drafted team: {playerteam}")
    question = input("Would you like to have a simulated fantasy Draft?")
    if question == "Yes " or "yes"or "y":
        amount_of_teams = int(input("How many different drafting teams do you want (including yourself)? "))
        snake_draft(amount_of_teams,fant_football)
        comarasin_of_players = input("do you want to compare 2 players (stats / things like that) to see whos better?")
        while comarasin_of_players != "No" or "n" or "no":
            player1 = input("Who is the first players name: (Please spell correctly): ")
            player2 = input("Who is the second players name: (Please spell correctly): ")
            compare_players(player1,player2)
        usage_question = input("would you like to know someone on your teams usage per game? ")
        while usage_question != "No" or "n" or "no":
            name_q = input("What is his name? be specific please!")
            pos_q = input ("What Position is he? (QB/RB/TE/WR)")
            usage_per_game(name_q,pos_q)
        print(" now that you have had a simulated draft and have seen skill players stats and usage during the\n 2019 season, go have fun!")
    else:
        print("Alright! have a fantastic day!")








        
    