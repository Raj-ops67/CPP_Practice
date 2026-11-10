# Electricity Billing System

def calculate_bill(units):
    bill = 0

    if units <= 100:
        bill = units * 1.50
    elif units <= 200:
        bill = 100 * 1.50 + (units - 100) * 2.50
    elif units <= 500:
        bill = (100 * 1.50) + (100 * 2.50) + (units - 200) * 4.00
    else:
        bill = (100 * 1.50) + (100 * 2.50) + (300 * 4.00) + (units - 500) * 6.00

    return bill


n = int(input("Enter number of customers: "))

for i in range(1, n + 1):
    print(f"\nCustomer {i}")

    name = input("Enter customer name: ")
    units = float(input("Enter units consumed: "))

    bill = calculate_bill(units)

    print("Customer Name :", name)
    print("Units :", units)
    print("Bill Amount : Rs.", round(bill, 2))