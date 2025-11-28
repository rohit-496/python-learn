'''
rock: 1
paper: 0
scissors: -1
'''

print("please choose r for rock, p for paper and s for scissors ")
player1 = input("Enter your choice: ")
player2 = input("Enter your choice: ")

game_dict = {"s": 1 , "r": 0 , "p": -1}
game_dict2 = {"s": "snake" , "r": "rock" , "p": "paper"}

print(f"player1 chose {game_dict2[player1]} and player 2 chose {game_dict2[player2]}")

player_1 = game_dict[player1]
player_2 = game_dict.get(player2)


if (player_1 == player_2):
    print("draw")
else:
    if(player_1 == 1 and player_2 == 0):
        print("player2 wins")
    elif(player_1 == 1 and player_2 == -1):
        print("player1 wins")
    elif(player_1 == 0 and player_2 == 1):
        print("player1 wins")
    elif(player_1 == 0 and player_2 == -1):
        print("player2 wins")
    elif(player_1 == -1 and player_2 == 1):
        print("player2 wins")
    elif(player_1 == -1 and player_2 == 0):
        print("player1 wins")
    




