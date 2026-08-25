def palind(r):
    e = r[-1]
    s = r[0]

    while (s<e):
        if r[s] != r[e]:
            return False
        s+=1
        e-=1
    return True

r = ("a", "b", "c", "c", "b", "a")

if palind(r):
    print ("The tuple is a Flip-Flop")
else: 
    print("Nope, not a Flip-flopper")