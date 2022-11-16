import random

outcome = ["rock","paper","scissor"]
def roll():
    placeholder = random.choice(outcome)
    return(placeholder)

def again():
    u_v = input("Do you want to continue?(y/n): ")
    if u_v == 'y' or u_v == 'Y':
        main()
    else:
        exit()

def main():
    print("====="*4)
    print("Choose your calling: ")
    print("====="*4)
    print("1) Rock")
    print("2) Paper")
    print("3) Scissor")
    print("====="*4)
    user_input = int(input(">>> "))
    computer_outcome = roll()
    print("====="*4)
    print("Your hand: ",outcome[user_input-1])
    print("Computer:  ",computer_outcome)
    if (user_input == 1 and computer_outcome == "rock") or (user_input == 2 and computer_outcome == "paper") or (user_input == 3 and computer_outcome == "scissor"):
        print("====="*4)
        print(">>> No one wins.")
        print("====="*4)
        again()
    elif (user_input == 1 and computer_outcome == "paper") or (user_input == 2 and computer_outcome == "scissor") or (user_input == 3 and computer_outcome == "rock"):
        print("====="*4)
        print(">>> Computer wins!")
        print("====="*4)
        again()
    else:
        print("====="*4)
        print(">>> User wins!")
        print("====="*4)
        again()
        
    

    
main()
