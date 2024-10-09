any_bidders = True
dictionary = {}

while any_bidders:
    name = input("What is your name?: ")
    bid = input("What's your bid?: ")
    dictionary[name] = bid
    any_bidders = input("Are there any other bidders ('Yes/No'):\n").lower()

    if any_bidders == "no":
        any_bidders = False

print(f"The winner is {max(dictionary,key=dictionary.get)} with a bid of ${max(dictionary.values())}")
