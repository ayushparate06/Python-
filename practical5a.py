# Take input from user
numbers = tuple(map(int, input("Enter integers separated by space: ").split()))

# a) Print total number of items
print("\nTotal number of items in the tuple:", len(numbers))

# b) Print last item
if len(numbers) > 0:
    print("Last item in the tuple:", numbers[-1])
else:
    print("Tuple is empty.")

# c) Print tuple in reverse order
print("Tuple elements in reverse order:", numbers[::-1])

# d) Check if 5 is present
if 5 in numbers:
    print("Yes")
else:
    print("No")

# e) Remove first and last items, sort remaining, and print result
if len(numbers) > 2:
    remaining = numbers[1:-1]      # Remove first and last
    sorted_remaining = tuple(sorted(remaining))
    print("Sorted tuple after removing first and last items:", sorted_remaining)
else:
    print("Not enough elements to remove first and last items.")