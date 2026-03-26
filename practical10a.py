import pandas as pd

# Read CSV file
df = pd.read_csv("books.csv")

# a) Print complete report in tabular form
def print_all_books():
    print("\n--- Complete Book Report ---")
    print(df)

# b) Print books of a given author
def books_by_author():
    author = input("Enter author name: ")
    result = df[df['Author'] == author]
    print("\n--- Books by Author ---")
    print(result)

# c) Print books of a given publishing house
def books_by_publisher():
    publisher = input("Enter publisher name: ")
    result = df[df['Publisher'] == publisher]
    print("\n--- Books by Publisher ---")
    print(result)

# d) Print cheapest and costliest book titles
def cheapest_and_costliest():
    cheapest = df.loc[df['Price'].idxmin()]
    costliest = df.loc[df['Price'].idxmax()]
    
    print("\n--- Cheapest Book ---")
    print(cheapest['Title'], "-", cheapest['Price'])
    
    print("\n--- Costliest Book ---")
    print(costliest['Title'], "-", costliest['Price'])

# e) Sort books by year of publication
def sort_by_year():
    sorted_df = df.sort_values(by='Year')
    print("\n--- Books Sorted by Year ---")
    print(sorted_df)

# Menu-driven program
while True:
    print("\n==== BOOK MANAGEMENT MENU ====")
    print("1. Show all books")
    print("2. Books by Author")
    print("3. Books by Publisher")
    print("4. Cheapest & Costliest Book")
    print("5. Sort by Year")
    print("6. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        print_all_books()
    elif choice == 2:
        books_by_author()
    elif choice == 3:
        books_by_publisher()
    elif choice == 4:
        cheapest_and_costliest()
    elif choice == 5:
        sort_by_year()
    elif choice == 6:
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.")