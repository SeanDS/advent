count = 0
floor = 0

with open("input") as f:
    while True:
        count += 1
        
        char = f.read(1)
        
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1
        else:
            break
        
        if floor == -1:
            break

print "Floor -1 first entered at position {0}".format(count)