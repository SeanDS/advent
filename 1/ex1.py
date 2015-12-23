floor = 0

with open("input") as f:
    # read single character    
    while True:
        char = f.read(1)
        
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1
        else:
            break

print "Floor: {0}".format(floor)