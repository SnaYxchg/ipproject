from random import randint
from functions import balance,df,update_balance,bet_increase,wager_increase

house_edge_percent = 5

print("\nWelcome to the CoinFlip Game! The House Edge is " + str(house_edge_percent) + "%")

def main(bal, house_edge_percent, index):
    # Updating the balance
    update_balance(bal, index)

    if bal > 0:
        a = input("Type B to bet or S to stop playing: ")
        if a == "B" or a == "b":
            bet_amount = float(input("Choose amount to bet: "))
            # Check if balance can afford the bet.

            if bal >= bet_amount:
                choice = ""
                chance = input("Type H to choose heads or T to choose tails: ")

                if chance == "H" or chance == "h":
                    choice = 1
                elif chance == "T" or chance == "t":
                    choice = 2
                else:
                    print("Wrong choice, try again.")
                    main(bal, house_edge_percent, index)

                # If H, h, T or t isn't chosen, then this if statement is just ignored.

                if choice == 1 or choice == 2:
                    # Updating the total bets and total wager
                    bet_increase(index)
                    wager_increase(bet_amount, index)

                    bal -= bet_amount

                    # Define what the winning amount will be: 
                    payout_after_edge = 1-house_edge_percent/100

                    # Will be 1.9x on 5% house edge.
                    total_payout_after_edge = 2*payout_after_edge
                    
                    random_number = randint(1, 2)

                    if random_number == choice:
                        # Then payout 
                        result = bet_amount * total_payout_after_edge
                        bal += result

                        print("Congratulations, you win! Result: +" + str(result) + "! Your new balance: " + str(bal) + ".")

                        main(bal, house_edge_percent, index)
                    else:
                        # Lose
                        result = -bet_amount
                        print("You lost. Result: " + str(result) + ". Better luck next time. Your new balance: " + str(bal) + ".\n")

                        main(bal, house_edge_percent, index)
            else:
                print("Your bet amount is greater than your balance. Your balance is:",bal)
                main(bal, house_edge_percent, index)
        elif a == "S" or a == "s":
          print("Thank you for playing :)\n")
        else: 
            print("Wrong input, try again.")
            main(bal, house_edge_percent, index)
    else: 
        print("You have now ran out of balance. Thanks for stepping by to play!")
        input("Type anything to continue: ")