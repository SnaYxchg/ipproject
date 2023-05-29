from random import randint
from functions import balance,update_balance,bet_increase,wager_increase

def roll(ch,amt,bet,index):
    no=randint(0,37)
    if ch=='red':
        if no in red:
          print('You Won!')
          amt+=bet
          print('New balance:',amt)
        else:
          print('You Lost')
          amt-=bet
          print('New balance:',amt)

          # Increasing total wagered and total bets
          bet_increase(index)
          wager_increase(bet,index)

    elif ch=='black':
        if no in black:
          print('You Won!')
          amt+=bet
          print('New balance:',amt)
        else:
          print('You Lost')
          amt-=bet
          print('New balance:',amt)

          # Increasing total wagered and total bets
          bet_increase(index)
          wager_increase(bet,index)

    elif ch=='green':
        if no in green:
          print('You Won!')
          amt+=bet*17
          print('New balance:',amt)
        else:
          print('You Lost')
          amt-=bet
          print('New balance:',amt)

          # Increasing total wagered and total bets
          bet_increase(index)
          wager_increase(bet,index)

    else:
      print("Invalid colour choice. Try Again.")
    
    # Updating the balance
    update_balance(amt,index)
    

red=(1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35)
black=(2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36)
green=(0,37)

print("Welcome to American Roullete Wheel! The House Edge is 5.26%")
print("-- Landing on Red or Black will have a 47.37% Chance each and yield a 2x payout")
print("----- Landing on Green has a 5.26% Chance and will yield a payout of 18x.")

def main(index):
    continue_game = True

    while continue_game == True:
      amt = balance(index)

      if amt != 0:
        play = input('Type B to bet or S to stop playing: ')

        if play == "s" or play == "S":
            continue_game = False
            print("Thank you for stepping by to play :)")
            input("Type anything to continue: ")
            break
        elif play == "b" or play == "B":
            bet=int(input('ENTER THE AMOUNT TO BET: '))
            ch=input('ENTER THE COLOUR (red, black or green): ')
            if bet<=amt:
                roll(ch,amt,bet,index)
            else:
              print("Invalid Bet. Your bet amount can't exceed your balance of " + str(amt) + ", Try Again.")
        else:
          print("Wrong input. Try again. ")
          main(index)
      else:
        print("You have ran out of balance. Thanks for stepping by to play!")
        continue_game = False
        input("Type anything to continue: ")