print("Enter Marks Obtained in 4 Subjects: ")
math = int(input("maths :"))
english = int(input("english :"))
science = int(input("science :"))
hindi = int(input("hindi :"))

sum = math+english+science+hindi
print("sum of all subject marks = ",sum)

perc = (sum/400)*100

print("Percentage Mark =", perc, "%")