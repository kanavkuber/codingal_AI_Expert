amt = int(input("Enter the amount to withdraw: "))

n1 = amt//100
n2 = (amt%100)//50
n3 = ((amt%100)%50)//10

print("Notes of rs 100 ", n1, "\nNotes of rs 50", n2, "\nNotes of rs 10", n3)