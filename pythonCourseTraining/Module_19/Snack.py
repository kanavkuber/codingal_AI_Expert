def calculate_change(paid, price):
    return paid-price

price = 55

print(f"The price for the snakc is {price}. We accept 1, 5, 10 and 25 rs coins")

coin = int(input("Insert a coin (1/5/10/25 only): "))
total_inserted = 0
coin_inserted = 0

while True:
    if coin != 1 or  coin!= 5 or coin != 10 or coin !=25:
        print("Enter a valid coin denomination")
        continue

    total_inserted += coin
    coin_inserted += 1

    if total_inserted >= price:
        print("That should do it!")
        break

change = calculate_change(total_inserted, price)

print("Your snack coming up in 3...2....1")

print("\n===== PURCHASE SUMMARY =====")
print("Snack Price:", price)
print("Coins Inserted:", coin_inserted)
print("Total Paid:", total_inserted)
print("Change Given:", change)
print("=============================")
print("Thanks for your purchase!")