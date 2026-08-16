def greet_customer():
    print("Hi, Welcome to my lemonade stand. I have got fresh lemonade just for you")
    name=input("what is your name starnger!")
    return name

name = greet_customer()

price_per_cup = float(input("what price cup do you want?"))
cups_sold = int(input("How many cups do you want?"))

def calculate_total(price, num):
    return round(price*num, 2)

total = calculate_total(price_per_cup, cups_sold)

print(f"Your total comes out to be {total}")

def calculate_change(paid, total):
    return paid-total

paid = float(input ("How much did the customer pay!"))
change = calculate_change(paid, total)
print(f"Here is your {change}")   

def thank_you_message():
    print(f"Thank you {name} for your purchase. Hope you enjoyed the drink and will come back for more!")

thank_you_message()

print (f""" ************** LEMON STAND SUMMARY ************** 

       {name} bought {cups_sold} cups for ${price_per_cup} each.
       The total cost for this purchase was {total}
       {name} paid ${paid} and the change they got back was ${change}

 """)