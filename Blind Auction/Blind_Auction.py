
import art
print(art.logo)
print("Welcome to the secret auction program")
bidder_list=[]
def add_bidder(name, price):
  new_bidder={}
  new_bidder["name"]=name
  new_bidder["price"]=price
  bidder_list.append(new_bidder)


to_continue=True
while to_continue:
  name=input("What is your name? ")
  price= int(input("What's your bid? $"))
  again=input("Are there any other bidders? Type 'yes' or 'no': ")
  add_bidder(name, price)
  if again=="no":
    to_continue=False
highest_price=0
for bidders in bidder_list:
  price = bidders["price"]
  if price>highest_price:
    highest_price=price 
    highest_bidder=bidders["name"]
  
  
  
print(f"The highest bidder is {highest_bidder} with a bid of ${highest_price}")