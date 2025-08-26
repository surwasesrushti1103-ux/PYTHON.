import random

l = ["rock", "paper", "scissor"]

while True:
    ccount = 0
    ucount = 0
    uc = int(input(''' 
Game Start...
1 YES
2 NO | EXIT
'''))

    if uc == 1:
        for a in range(1, 6):
            userInput = int(input('''
1 Rock
2 Paper 
3 Scissor
'''))
            if userInput == 1:
                uchoice = "rock"
            elif userInput == 2:
                uchoice = "paper"
            elif userInput == 3:
                uchoice = "scissor"
            else:
                print("Invalid choice, try again.")
                continue

            Cchoice = random.choice(l)

            print("Computer Value:", Cchoice)
            print("Your Value:", uchoice)

            if Cchoice == uchoice:
                print("Game Draw")
                ucount=ucount+1
                ccount=ccount+1
            elif (uchoice == "rock" and Cchoice == "scissor") or \
                 (uchoice == "paper" and Cchoice == "rock") or \
                 (uchoice == "scissor" and Cchoice == "paper"):
                print("You win this round!")
                ucount += 1
            else:
                print("Computer wins this round!")
                ccount += 1

        print("\nFinal Score:")
        print("Your Score:", ucount)
        print("Computer Score:", ccount)

        if ucount > ccount:
            print("🎉 You are the final winner!")
        elif ccount > ucount:
            print("💻 Computer is the final winner!")
        else:
            print("😅 The match is a draw!")

    else:
        break
