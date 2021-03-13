import random
rpc = ["Rock", "Paper", "Scissors"]

player2 = rpc[random.randint(0, 2)]

player1 = False

while player1 == False:
    player1 = input("Enter you selection [Rock, Paper or Scissors] "
                    "?")
    if player1 == player2:
        print("Draw! {} vs {}".format(player1, player2))
    elif player1 == "Rock":
        if player2 == "Paper":
            print("You lose! {} vs {}".format(player1,player2))
        else:
            print("You win! {} vs {}".format(player1,player2))
    elif player1 == "Paper":
        if player2 == "Scissors":
            print("You lose! {} vs {}".format(player1,player2))
        else:
            print("You win! {} vs {}".format(player1,player2))
    elif player1 == "Scissors":
        if player2 == "Rock":
            print("You lose! {} vs {}".format(player1,player2))
        else:
            print("You win! {} vs {}".format(player1,player2))
    else:
        print("Please check your spellings!")

    yn = False

    while yn == False:
        yn = input("Try again? [yes | no]")
        if yn == "yes":
            player1 = False
            player2 = rpc[random.randint(0, 2)]
        elif yn == "no":
           print("Thankyou for playing! :)")
           yn = True
        else:
            yn = False
            print("Please check your spellings!")


