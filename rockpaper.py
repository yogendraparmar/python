'''
Workflow of project:
1. input from user (Rock, paper, scissor)
2. Computer choice(computer will choose rendomely)
3. Result print

Cases:
A - Rock
Rock - Rock = tie
Rock - Paper = paper win
Rock - Scissor = Rock win

B- Paaper
Paper - Papeer = tie
Paper - Rock = paper win
paper - scissor = scissor win

C- Scissor
Scissor - Scissor = Tie
Scissor - Rock = Rock wind
Scissor - Paper = Scissor win

'''
import random
item_list= ["Rock", "Paper", "Scissor"]
user_choice= input("Enter your move = Rock, Paper, Scissor=")
comp_choice = random.choice(item_list)

print(f"user choice={user_choice}, computer_choic={comp_choice}")
if user_choice == comp_choice:
    print("Both choose same:= Match Tie")
elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper cover rock = computer win")
    else:
        print("Rock smashes sissor = you win ")
elif user_choice=="Paper":
    if comp_choice == "Scissor":
        print("Scissor cut paper, computer win")
    else:
        print("Paper cover rocks, you win")
elif user_choice == "Scissor":
    if comp_choice =="Paper":
        print("Scissor cutss paper , you win")
    else:
        print("Rock smashes scissor, computer win")
        
