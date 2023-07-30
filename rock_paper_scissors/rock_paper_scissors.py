import random

scores = [0,0]
options = {"rock":"scissors","paper":"rock","scissors":"paper"}


while(True):
    print("Enter q for quit")
    computer_choice = random.choice([key for key in options.keys()])
    user_choice = input("Choose rock, paper, scissors : ")
    if user_choice.lower() == "q" :
        print(f"Your score is {scores[0]} and the computer score is {scores[1]}")
        break
    
    if options[user_choice] == computer_choice:
        print(f"The computer had chosen {computer_choice}. You won one score ! ")
        scores[0] += 1
    elif options[computer_choice] == user_choice:
        print(f"The computer had chosen {computer_choice}. Computer won one score !")
        scores[1] += 1      
    else:
        print("No one won score")
    print("-----------------------------\n")