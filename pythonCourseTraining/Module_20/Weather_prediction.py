weather = (0,1,0,0,0,1,1,0)
sunny = 0
rainy = 0

for day in range(0,8):
    if day==0:
        sunny+=1
    elif day==1:
        rainy+=1

if sunny>rainy:
    print("Good weather")
else: 
    print ("Bad weather")














