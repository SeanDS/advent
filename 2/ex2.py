def calcVolume(l, w, h):    
    return l * w * h

def calcSmallestPerimeter(*args):
    d1, d2 = sorted(args)[0:2]
    
    return 2 * d1 + 2 * d2

length = 0

for line in open("input").readlines():
    (l, w, h) = list(map(int, line.strip().split("x")))
    
    length += calcVolume(l, w, h) + calcSmallestPerimeter(l, w, h)

print length