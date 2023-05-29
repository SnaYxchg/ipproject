import functions

def get_faucet(index):
  old_balance = functions.balance(index)
  if old_balance >= 10:
    return "You're not eligible for using the faucet. You must have 10 or less coins to claim faucet.\n"
  else:
    print("Claiming faucet...")
    faucet_amount = 100
    new_balance = old_balance + 100

    functions.update_balance(new_balance, index)
    return "Faucet successfully claimed!\n"