bid = {}

still_bidding = False

while not still_bidding:
    name = input("Name of the bidder: ")
    amount = int(input("Bidding amount= "))
    bid[name] = amount

    more = input("Are there more bidders? Enter y or n: ")
    if more == "n":
        still_bidding = True

max_name = max(bid, key=bid.get)
print(max_name)