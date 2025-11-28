#q1
#WAP to read the text from a file poems.txt and find out whether it contains word twinkle

'''
with open("file\poems.txt","r") as f:
    content = f.read().lower()
    if ("twinkle" in content):
        print("yes word is present")
    else:
        print("not present")
'''
#q2
#The game fucntion in a program lets user play a game and returns the socre as an integer. you need to read a file hiscore.txt which is either blank or contains the prev hiscore . pdate highscore whenever yous see new high score
'''import random
def game():
    score = random.randint(1,1000)
    with open("file/hiscore.txt") as f:
        high_score =f.read() 
        if (high_score != ""):
               high_score =  int(high_score)
        else:
                  high_score = 0
    
    print(f"Your score {score}")

    if(score > high_score):
        with open("file/hiscore.txt", "w") as f:
         f.write(str(score))
    return score
                  
game()'''

#tables for a 13 y old kiddo

def generate_table():
    for i in range(2,21):
        str =""
        with open(f"file/tables/table_of_{i}.txt","w") as f:
             for j in range(1,11):
                str = str + f"{i} * {j} = {i*j} \n"
             f.write(str)
             

generate_table()
