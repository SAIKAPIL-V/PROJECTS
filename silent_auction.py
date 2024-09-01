import os 
print("****** Welcome to the Silent Auction Program *******")

def find_highest_bidder(bidders):
    highest_bid = 0
    winner = ""
    for bidder in bidders:
        bid_amount = bidders[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(bidders)
    print(f"The winner is {winner} with a bid of {highest_bid}")

auction_data = {}
bidding_ongoing = True

while bidding_ongoing:
    bidder_name = input("What is your name? ")
    bid_price = int(input("What is your bid? "))
    auction_data[bidder_name] = bid_price
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if more_bidders=='no':
        bidding_ongoing =False
        find_highest_bidder(auction_data)
    elif more_bidders == "yes":
        os.system("cls")  
