cost = float(input(" Enter the actual price of the product: "))
sale = float(input(" Enter the sales price of the product: "))

if sale>cost:
    amount = sale-cost
    print("Total profit = ", amount)
else:
    print ("No profit :(")