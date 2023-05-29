import pandas as pd
import hashlib
from functions import df, balance
from faucet import get_faucet


def start():
  username = input("Enter your username: ")
  df = pd.read_csv("players.csv")

  # Checking if the username is already there. 
  usernames = df['Username']
  username_exists = False

  for i in usernames:
    if username == i:
      # Username is already there, log in.
      login(username)
      username_exists = True
      break

  if username_exists == False:
      # Register the user
      print("Welcome! Seems like your username isn't registered.")
      pw = input("Enter a new password to sign up: ")

      # Using the broken and vulnerable md5 hash for demonstration purposes only. 
      hashed_pw = hashlib.md5(pw.encode())
      hashed_pw = hashed_pw.hexdigest()

      # Add a row in the dataframe

      df.loc[len(df),:] = [username, hashed_pw, 100, 0, 0]
      df.to_csv("players.csv", index = False)

      print("You have been successfully registered!\n")

      login(username)

def login(uname):
  pw = input("Enter your password to login: ")

  hashed_pw = hashlib.md5(pw.encode())
  hashed_pw = hashed_pw.hexdigest()

  dataframe = pd.read_csv("players.csv")
  usernames = dataframe["Username"]

  # Find the user's index number
  n = -1
  for x in usernames:
    n += 1
    if x == uname:
      # User's index number has been found. 
      index_number = n
      break
    
  # Check if his password is entered correctly. 
  real_pass = dataframe.loc[index_number,"Password"]
  if real_pass == hashed_pw:
    print("You've logged in successfully!\n")
    menu(index_number)
  else:
    print("You've entered the wrong password. Try again.")
    login(uname)


def menu(index):
    menu_choice = ""

    # This loop always runs until broken. 
    while true:
        if menu_choice == "1":
            import coinflip
            house_edge_percent = 5
            coinflip.main(balance(index), house_edge_percent, index)

        if menu_choice == "2":
            import roulette
            roulette.main(index)
        if menu_choice == "3":
            print("\n")
            print(get_faucet(index))
            input("Type anything to continue: ")
        if menu_choice == "4":
            print("\nLoading statistics...")
            import statistics
            break
        if menu_choice == "5":
            print("\nGame exited.")
            break
        else: 
            # Means menu_choice is neither 1, 2, 3, 4 nor 5
            print("Welcome to GameOfLuck! :) " + "Your balance is", balance(index),"coins.\n")

            print("Choose which game you'd like to play:-")
            print("1: CoinFlip")
            print("2: Roullete")
            print("3: Faucet (if you're low on balance :))")
            print("4: Show Statistics")
            print("5: Exit the program\n")


            menu_choice = input("Enter  1, 2, 3, 4 or 5: ")

start()