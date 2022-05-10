import argparse
import random as rd

FILE = 'players.txt'
players = []
team_a = []
team_b = []

parser = argparse.ArgumentParser(description='Generate teams to futsal game!')
parser.add_argument('-action', help='Choose if pretend that teams are generated manual or random (e.g. "-action manual" | "-action random" | "-action players")')
args = parser.parse_args()

with open(FILE) as file:
    for line in file:
        line = line. strip()
        players.append(line)
        team_b.append(line)

if len(players) != 10:
    print('\nPlease put 10 players in file: "players.txt".')
    exit()

def teams(team_a, team_b):
    print('\n\t\tTEAM 1 (white):')
    for n in team_a:
        team_b.remove(n)
        print(n,end="  ")
    print('\n\n\t\tTEAM 2 (black):')
    for n in team_b:
        print(n,end="  ") 
    print('\n\nScript is complete!!!')

if args.action == "players":
    print('Players:')
    for n in players:
        print(f'\t- {n}')

if args.action == "random":
    team_a = rd.sample(players,5)
    teams(team_a, team_b)
    
if args.action == "manual":
    group = {}
    for i in range(1, 5):
        for n in players:
            print(f'\t- {n}')
        print('(From the list above, choose the name of two players you want to separate)\n')
        x = input('Player 1: ' )
        y = input('Player 2: ' )
        group[i] = [x, y]
        players.remove(x)
        players.remove(y)
        print('\n')
    group[5] = players
    
    for n in range(1,6):
        team_a.append(rd.sample(group[n],1)[0])
    
    teams(team_a, team_b)