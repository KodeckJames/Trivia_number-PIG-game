# HOW THIS GAME WORKS:
# This game involves a maximum of 4 players. Each player gets a chance to roll the dice containing from no 1-6.A player chooses the number of times to roll the dice. If a player gets any number other than 1, they  get points. When a player gets a 1 in the numberof times they chose to roll the dice, all points are deducted and reduced to 0, and the next player plays...



import random

def roll():
    min_value=1
    max_value=6
    roll=random.randint(min_value, max_value)

    return roll

while True:
    players=input("Enter the number of players (2-4): ")
    if players.isdigit():
        players =int(players)
        if 2<= players <= 4:
            break
        else:
            print("Must be between 2-4 players.")
    else:
        print("Invalid, try again.")

max_score=50
player_scores=[0 for _ in range(players)]

while max(player_scores) < max_score:

    for player_idx in range(players):
        print(f"\nPlayer number {player_idx+1} turn has just started")
        print(f"Your total score is: {player_scores[player_idx]}\n")
        current_score=0
        
        while True:
            should_roll=input("Would you like to roll (y) ? ")
            if should_roll.lower() != "y":
                break
            value=roll()
            if value==1:
                print("You rolled a 1! Turn done!")
                current_score=0
                break
            else:
                current_score+=value
                print(f"You rolled a: {value}")

            print(f"Your score is: {current_score}")
        player_scores[player_idx]+=current_score
        print(f"Your total score is: {player_scores[player_idx]}")

max_score=max(player_scores)
winning_idx=player_scores.index(max_score)
print(f"Player number {winning_idx+1} is the winner with a score of : {max_score}")