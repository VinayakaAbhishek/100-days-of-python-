# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import art
print(art.logo)

def find_highest_bidder(bidding_dictionary):
    winner=""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount=bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid=bid_amount
            winner=bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}")

bidding = {}
continue_bidding= True
while continue_bidding == True:
        name = input("Enter your name: ")
        price = int(input("Enter your bid: $"))
        bidding[name] = price
        new_bid = input('''Are there any other inputs ? Type "yes" or "no" : ''')
        if new_bid == "yes":
            continue_bidding = True
            print("\n"*20)
        else:
            continue_bidding = False
            find_highest_bidder(bidding)


