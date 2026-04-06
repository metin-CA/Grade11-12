from art import logo
print(logo)

def get_highest_bid(bids):
    highest_bid = 0
    winner = ""
    for bid in bids:
        bid_amount = bids[bid]
        if bid_amount > highest_bid:
            highest_bid = bids[bid]
            winner = bid

    print(f"The highest bid is {highest_bid} by {winner}")

list_of_bids = {}
is_game_on = True
while is_game_on:
    name = input("What is your name?: ").lower()
    price = int(input("What is your bid?: $"))
    other_bids = input("Are there any other bids?:  Type \"yes\" or \"no\"").lower()
    list_of_bids[name] = price

    if other_bids == "no":
        is_game_on = False
        get_highest_bid(list_of_bids)
    elif other_bids == "yes":
        print("\n" * 20)
    else:
        print("Please enter either yes or no!")