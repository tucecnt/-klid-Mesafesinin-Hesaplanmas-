import math

points=[(1,2),(3,4)]

def oklidmesafesi(points):
    for i in range(len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        print(f"noktalar arasındaki mesafe: {d}")

oklidmesafesi(points)
