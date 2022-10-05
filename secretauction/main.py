from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)

print("Welcome to the secret auction program.")

bid_collector = {}
bid_option = False

def find_highest_bidder(bid_recoreder):
    bit_value = 0
    winner = ""
    for bidder in bid_recoreder:
        bid_amount = bid_recoreder[bidder]
        if bid_amount > bit_value:
            bit_value = bid_amount
            winner = bidder
    clear()
    print(f"The winner is {winner} with a bid of ${bit_value}.")

while not bid_option:
    name = input("What is your name?:")
    bid_amount = int(input("What's your bid?: $"))
    bid_collector[name] = bid_amount
    adder = input("Are there any other bidders? Type 'Yes' or 'no'\n").lower()
    if adder == "no":
        bid_option = True
        find_highest_bidder(bid_collector)     
    else:
        clear()
