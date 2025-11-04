# -*- coding: utf-8 -*-
#setting up the preliminary variables, such as the user's initial shares, money and a random stock price to be used in the program
import random
money=1000
shares=0
stockprice=round(random.uniform(50,150),2)
change=float()
#used to determine how many shares the user would like to buy, creates a local variable "amount"
def buy(money,stockprice,shares):
  try:
    amount = int(input("How many shares would you like to buy?"))
  except ValueError:
    print("Needed to be an integer")
  while amount * stockprice > money:
    print("You don't have enough money to perform this transaction.")
    try:
      amount = int(input("How many shares would you like to buy?"))
    except ValueError:
      print("Needed to be an integer")
  money = money-(amount*stockprice)
  shares = shares + amount
  return money,shares
#used to determine how many shares the user would like to sell, creates a local variable "amount"
def sell(money,stockprice,shares):
  try:
    amount = int(input("How many shares would you like to sell?"))
  except ValueError:
    print("Needed to be an integer")
  while amount > shares:
    print("You don't have enough shares to perform this action")
    try:
      amount = int(input("How many shares would you like to sell?"))
    except ValueError:
      print("Needed to be an integer")
  money = money + (amount * stockprice)
  shares = shares - amount
  return money,shares

#main - for loop used to simulate 10 days of stock market activity
for i in range(10):
  print(f""">Current data<
Day: {i+1}
Money: {money}
Shares owned: {shares}
Shares price: {stockprice}""")
  choice=input("Buy, sell or hold?")
  while choice.lower() not in ["buy","sell","hold"]:
    choice=input("Enter buy, sell or hold: ")
  if choice.lower() == "buy":
    money,shares = buy(money,stockprice,shares)
    print(f""">Current data<
Day: {i+1}
Money: {money}
Shares owned: {shares}
Shares price: {stockprice}""")
  elif choice.lower() == "sell":
    money,shares = sell(money,stockprice,shares)
    print(f""">Current data<
Day: {i+1}
Money: {money}
Shares owned: {shares}
Shares price: {stockprice}""")
  elif choice.lower() == "hold":
    pass
  change=random.uniform(0.8,1.2)
  stockprice=stockprice*change
print(f"Profit = {money-1000}")
