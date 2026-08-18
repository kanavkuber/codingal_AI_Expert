flag = False

while not flag:
    try:
        num=int(input("Enter the number: "))

        while num%2 == 0:
            print("bye")
            num = int(input("Enter the number: "))
        flag = True

    except ValueError:
        print("Invalid value")

