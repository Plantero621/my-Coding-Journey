people = "t w o"

def wave(people):
    c = len(people)
    arr = []
    for x in range(c):
        for i, val in enumerate(people[:]):
            up=people[i].upper()
            c=people[:i] + up + people[i+1:]

            if  c.islower() == False:
                arr.append(c)
            print(c.islower())
        return arr
        x+=1
    if c == 0:
        return []
        
print(wave(people))