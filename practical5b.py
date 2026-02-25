# Take input from user
prices = tuple(map(float, input("Enter prices of sold items separated by space: ").split()))

# a) Total number of items sold
print("\nTotal number of items sold:", len(prices))

# Check if tuple is not empty
if len(prices) > 0:
    
    # b) Cheapest item price
    print("Price of cheapest item sold:", min(prices))
    
    # c) Costliest item price
    max_price = max(prices)
    print("Price of costliest item sold:", max_price)
    
    # d) Price list in ascending order
    print("Price list in ascending order:", tuple(sorted(prices)))
    
    # e) Number of costliest items sold
    print("Number of costliest items sold:", prices.count(max_price))

else:
    print("No items sold.")