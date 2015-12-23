def calcArea(l, w, h):
    dimensions = [l * w, l * h, w * h]
    
    return 2 * sum(dimensions) + min(dimensions)

area = 0

for line in open("input").readlines():
    (l, w, h) = list(map(int, line.strip().split("x")))
    
    area += calcArea(l, w, h)

print area