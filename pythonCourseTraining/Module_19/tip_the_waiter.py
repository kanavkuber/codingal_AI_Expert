def total_calc(bill_amount, tip_perc):
    total = (1+tip_perc/100)*bill_amount
    total = round(total, 2)
    return print(f"The total amount payable is ${total}")

total_calc(150, 20)

