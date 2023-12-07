import art
print(art.logo)

print("Welcome to Secret Auction Program!")

def finding_highest_bidder(bidding_list):
  highest_bid=0
  winner=""
  for bidders in bidding_list:
    price=bidding_list[bidders]
    if price>highest_bid:
      highest_bid=price
      winner=bidders
  print(f"The highest bidder is {winner} with a bid of ${highest_bid}")

bidding_list={}
to_continue=True
while to_continue:
  name = input("Enter your name: ")
  bid = int(input("Enter your bid amount $"))
  bidding_list[name]=bid
  run=input("Are there any other bidders? Type 'yes' or 'no' ")
  if run=="no":
    to_continue=False
    finding_highest_bidder(bidding_list)

