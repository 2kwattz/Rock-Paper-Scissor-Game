import random
import pyfiglet

#About game
def aboutgame():
    print("Why is Rock Paper Scissors played?\n")
    print("This game is played by children and adults and is popular all over the world.\n")
    print("Apart from being a game played to pass time, the game is usually played in situations where something has to be chosen. It is similar in that way to other games like flipping the coin, throwing dice or drawing straws\n")
    print("There is no room for cheating or for knowing what the other person is going to do so the results are usually very satisfying with no room for fighting or error.\n")
    
gameoptions = ['r','p','s']
userpoints = 0
computerpoints = 0
rounds = 0

#Main interface

banner = pyfiglet.figlet_format("Rock Paper Scissor")
print(banner)
print("Press: 1. Play  2. Rules  3. About Game 4. Exit\nCode by : 2kwattz\n")
menueoptions = int(input())

if menueoptions == 1:
    print("Enter your name to continue")
    username = input()
    print(f"\nWelcome {username}, Lets Start !")
    while(rounds<10):
        rounds = rounds + 1
        print("\n Press: 1.Rock  2.Paper 3.Scissor")
        compinput = random.choice(gameoptions)
        userinput = int(input())
        if userinput == 1 and compinput == 'r':
            print(f"Round {rounds} : {username} chose Rock , Computer chose Rock\n")
            print(f"Its a Draw\t {username}'s Score : {userpoints} , Computer's Score : {computerpoints}")
        elif userinput == 1 and compinput == 'p':
            computerpoints = computerpoints + 1
            print(f"Round {rounds} : {username} chose Rock , Computer chose Paper\n")
            print(f"Computer won this round , {username}'s Score : {userpoints} , Computer's Score : {computerpoints}")
        elif userinput == 1 and compinput == 's':
            userpoints = userpoints + 1
            print(f"Round {rounds} : {username} chose Rock , Computer chose Paper\n")
            print(f"{username} won this round , {username}'s Score : {userpoints} , Computer's Score : {computerpoints}")
        elif userinput == 2 and compinput == 'r':
            userpoints = userpoints + 1
            print(f"Round {rounds} : {username} chose Paper , Computer chose Rock\n")
            print(f"{username} won this round , {username}'s Score : {userpoints} , Computer's Score : {computerpoints}")
        elif userinput == 2 and compinput == 'p':
            print(f"Round {rounds} : {username} chose Paper , Computer chose Paper\n")
            print(f"Its a Draw\t {username}'s Score : {userpoints} , Computer's Score : {computerpoints}")
        elif userinput == 2 and compinput == 's':
            computerpoints = computerpoints + 1
            print(f"Round {rounds} : {username} chose Paper , Computer chose Scissors\n")
            print(f"Computer won this Round , {username}'s Score : {userpoints} , Computer's Score : {computerpoints}")
        elif userinput == 3 and compinput == 'r':
            computerpoints = computerpoints + 1
            print(f"Round {rounds} : {username} chose Scissors , Computer chose Rock\n")
            print(f"Computer won this round , {username}'s Score : {userpoints} , Computer's Score : {computerpoints}")
        elif userinput == 3 and compinput == 'p':
            userpoints = userpoints + 1
            print(f"Round {rounds} : {username} chose Scissors , Computer chose Paper\n")
            print(f"{username} won this round , {username}'s Score : {userpoints} , Computer's Score : {computerpoints}")
        elif userinput == 3 and compinput == 's':
            print(f"Round {rounds} : {username} chose Scissor , Computer chose Scissor\n")
            print(f"Its a Draw\t {username}'s Score : {userpoints} , Computer's score : {computerpoints}")
        else:
            print("My Dear Sir . You have not entered a valid number. \nPlease enter '1' for Rock\n'2' for paper\n'3' for scissor\n")
elif menueoptions == 2:
    print("Rock wins against scissors.\nScissors win against paper.\nPaper wins against rock.\n")
elif menueoptions == 3:
    print(aboutgame())
