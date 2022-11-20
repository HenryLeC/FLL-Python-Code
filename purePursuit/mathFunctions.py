import math

class Point():
    pass

def AngleWrap(angle: float):
    while(angle < -math.PI):
        angle += 2 * math.PI
    while(angle > math.PI):
        angle -= 2 * math.PI
    return angle

def lineCircleIntersection(circleCenter: Point, radius, linePoint1: Point, linePoint2: Point) -> list[Point]:
    if(abs(linePoint1.y - linePoint2.y) < 0.003):
        linePoint1.y = linePoint2.y + 0.003
    if(abs(linePoint1.x - linePoint2.x) < 0.003):
        linePoint1.x = linePoint2.x + 0.003

    m1 = (linePoint2.y - linePoint1.y)/(linePoint2.x - linePoint1.x)

    quadraticA = 1.0 + m1**2

    x1 = linePoint1.x - circleCenter.x
    y1 = linePoint1.y - circleCenter.y


    quadraticB = (2.0 * m1 * y1) - (2.0 * m1 ** 2 * x1)

    quadraticC = m1 ** 2 * x1 ** 2 - (2.0 * y1 * m1 * x1) + y1 ** 2 - radius ** 2

    allPoints = []

    try:
        xRoot1 = (-quadraticB + math.sqrt(quadraticB ** 2 - (4.0 * quadraticA * quadraticC)))/(2.0 * quadraticA)

        yRoot1 = m1 * (xRoot1 - x1) + y1


        # put back the offset
        xRoot1 += circleCenter.x
        yRoot1 += circleCenter.y

        minX = linePoint1.x if linePoint1.x < linePoint1.x  else linePoint2.x
        maxX = linePoint1.x if linePoint1.x > linePoint1.x else linePoint2.x


        if xRoot1 > minX and xRoot1 < maxX:
            allPoints.add(Point(xRoot1,yRoot1)) 

        xRoot2 = (-quadraticB - math.sqrt(quadraticB ** 2 - (4.0 * quadraticA * quadraticC)))/(2.0 * quadraticA)
        yRoot2 = m1 * (xRoot2 - x1) + y1


        xRoot2 += circleCenter.x
        yRoot2 += circleCenter.y

        if xRoot2 > minX and xRoot2 < maxX:
            allPoints.add(Point(xRoot2,yRoot2))

    finally:
        return allPoints