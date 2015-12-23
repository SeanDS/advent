presents = {}

def addPresent(north, east):
    global presents
    
    if north not in presents.keys():
        presents[north] = {}
        
    if east not in presents[north].keys():
        presents[north][east] = 0
    
    presents[north][east] += 1

north = 0
east = 0

with open("input") as f:
    while True:
        char = f.read(1)
        
        # give present to current location
        addPresent(north, east)
        
        if char == '>':
            east += 1
        elif char == '<':
            east -= 1
        elif char == '^':
            north += 1
        elif char == 'v':
            north -= 1
        else:
            break

count = 0

for n in presents:
    for e in presents[n]:
        if presents[n][e] > 0:
            count += 1

print count