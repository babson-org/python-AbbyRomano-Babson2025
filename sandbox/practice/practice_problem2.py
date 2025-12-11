#Treasure doors game 
import random

def treasure_doors(strategy):
    doors = [ 'X', 'X', 'X']
    treasure = random.randint(0,2)
    doors[treasure] = 'T'

    player_choice = random.randint(0,2)

    host_reveal = None
    for i in range(3):
        if i != player_choice and doors[i] == 'X':
            host_reveal = i
            break
    
    if strategy == 'switch':
        for i in range(3):
            if i != player_choice and i != host_reveal:
                player_choice = i
                break
    
    return doors[player_choice] == 'T'


print(treasure_doors('switch'))



#test it
def run_experiment(num_games):
    stay_wins = 0
    switch_wins = 0

    for _ in range(num_games):
        if treasure_doors('stay'):
            stay_wins += 1
        if treasure_doors('switch'):
            switch_wins += 1
    
    print(f'Stay strategy win percentage: {stay_wins / num_games * 100}%')
    print(f'Switch strategy win percentage: {switch_wins / num_games * 100}%')

run_experiment(1000)

   
   
    



        



        