L = [1,3,5,7,9]
print(L)
ctr = 0
for i in L:
    ctr += i

avg = ctr/len(L)

print("The sum is: ", ctr," and the average is: ", avg)

print(L.sort())

print("Smallest element = ", L[0]," Largest Element: ", L[-1])