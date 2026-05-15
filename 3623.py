import math

points = [[1,0],[2,0],[3,0],[2,2],[3,2]]    # 3
points = [[0,0],[1,0],[0,1],[2,1]]          # 1

def slope(p1, p2):
    return (p2[1]-p1[1])/(p2[0]-p1[0])

options = 0

for a in range(len(points)-3):
    for b in range(a+1, len(points)-2):
        for c in range(b+1, len(points)-1):
            for d in range(c+1, len(points)):
                try:
                    if slope(points[a], points[b]) == slope(points[c], points[d]):
                        options += 1
                        continue
                except:
                    continue
                try:
                    if slope(points[a], points[c]) == slope(points[b], points[d]):
                        options += 1
                        continue
                except:
                    continue
                try:
                    if slope(points[a], points[d]) == slope(points[b], points[c]):
                        options += 1
                        continue
                except:
                    continue



print(options)


