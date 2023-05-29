import pandas as pd

def df():
  df = pd.read_csv("players.csv")
  return df

def balance(index):
  d = df()
  bal = d.loc[index,"Balance"]
  return bal

def update_balance(new_bal, index):
  d = df()
  d.loc[index,"Balance"] = new_bal
  d.to_csv("players.csv", index = False)

def bet_increase(index):
  d = df()
  previous_bets = d.loc[index,"Total Bets"]
  new_total_bets = previous_bets + 1

  d.loc[index,"Total Bets"] = new_total_bets
  d.to_csv("players.csv", index = False)

def wager_increase(new_wager, index):
  d = df()
  previous_total_wager = d.loc[index,"Total Wagered"]
  new_total_wager = previous_total_wager + new_wager

  d.loc[index,"Total Wagered"] = new_total_wager
  d.to_csv("players.csv", index = False)