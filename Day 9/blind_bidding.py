bidders = {}
flag = "yes"

print("WELCOME TO THE SILENT BIDDING")
while flag == "yes":
    name = input("What is your name?\n")
    bidding_value = int(input("What is your bidding amount? $"))
    bidders[name] = bidding_value
    flag = input("Would anyone else like to bid? (yes/no)\n")

bid_values = list(bidders.values())
max_bid = max(bid_values)
name_list = list(bidders.keys())
winner_name = name_list[bid_values.index(max_bid)]
print(f"The winner is {winner_name} with a bid of {max_bid}$")

