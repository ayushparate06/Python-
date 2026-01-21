vendor_name = input("Enter Vendor Name: ")
year_of_association = int(input("Enter Year of Association: "))
contact_number = input("Enter Contact Number: ")
email_id = input("Enter Email ID: ")

monthly_purchases = []
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

print("\nEnter Monthly Purchase Amounts:")
for month in months:
    amount = float(input(f"{month}: "))
    monthly_purchases.append(amount)

annual_total = sum(monthly_purchases)

print("\n" + "=" * 40)
print("        ANNUAL PURCHASE REPORT")
print("=" * 40)
print(f"Vendor Name        : {vendor_name}")
print(f"Year of Association: {year_of_association}")
print(f"Contact Number     : {contact_number}")
print(f"Email ID           : {email_id}")

print("\nMonthly Purchases:")
for i in range(12):
    print(f"{months[i]:<10} : ₹{monthly_purchases[i]:.2f}")

print("\n----------------------------------------")
print(f"Total Annual Purchase: ₹{annual_total:.2f}")
print("=" * 40)
