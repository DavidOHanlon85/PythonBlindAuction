from art import logo

print(logo)
print("Welcome to the secret auction program")

still_bidder = True
bidders = {}

def find_highest_bidder(dictonary):
    max_value = 0
    name_of_max_bidder = ""
    for bidder in bidders:
        if bidders[bidder] > max_value:
            max_value = bidders[bidder]
            name_of_max_bidder = bidder

    print(f"\nThe winner is {name_of_max_bidder} with a bid of ${max_value}")

while still_bidder:

    name = input("What is your name?\n")
    bid = int(input("What's your bid? $\n"))
    bidders[name] = bid

    more_bidders = input("Are there any other bidders. Type 'yes' or 'no'\n").lower()

    if more_bidders == 'no':
        still_bidder = False
        find_highest_bidder(bidders)
    else:
        print("\n" * 20)





