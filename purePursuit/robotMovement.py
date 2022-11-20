import math
from robot import *
from mathFunctions import AngleWrap, lineCircleIntersection
from point import Point
from curvePoint import CurvePoint

def clip(input_val: float, min_val: float, max_val: float) -> float:
    return max(min(input_val, max_val), min_val)

def followCurve(allPoints: list[CurvePoint], followAngle: float):
    followMe = getFollowPointPath(allPoints, Point(worldXPosition, worldYPosition), allPoints[0].followDistance)
    goToPosition(followMe.x, followMe.y, followMe.moveSpeed, followAngle, followMe.turnSpeed)

def getFollowPointPath(pathPoints: list[Point], robotLocation: Point, followRadius: float) -> CurvePoint:
    followMe = CurvePoint(pathPoints)

    for i in range(len(pathPoints) - 1):
        startLine = pathPoints[i]
        endLine = pathPoints[i + 1]
        intersections = lineCircleIntersection(robotLocation, followRadius, startLine.toPoint(), endLine.toPoint())
        closestAngle = 99999999999
        for intersection in intersections:
            angle = math.atan2(intersection.y - worldYPosition, intersection.x - worldXPosition)
            deltaAngle = abs(AngleWrap(angle - worldAngle_rad))

            if deltaAngle < closestAngle:
                closestAngle = deltaAngle
                followMe.setPoint(intersection)
    return followMe


def goToPosition(x: float, y: float, movementSpeed: float, preferredAngle: float, turnSpeed: float):
    distanceToTarget = math.hypot(x -worldXPosition, y - worldYPosition)

    absoluteAngleToTarget = math.atan2(y-worldYPosition,x-worldXPosition)

    relativeAngleToPoint = AngleWrap(absoluteAngleToTarget - (worldAngle_rad - math.radians(90)))



    relativeXToPoint = math.cos(relativeAngleToPoint) * distanceToTarget
    relativeYToPoint = math.sin(relativeAngleToPoint) * distanceToTarget

    movementXPower = relativeXToPoint / (abs(relativeXToPoint) + abs(relativeYToPoint))
    movementYPower = relativeYToPoint / (abs(relativeXToPoint) + abs(relativeYToPoint))

    movement_x = movementXPower * movementSpeed
    movement_y = movementYPower * movementSpeed

    relativeTurnAngle = relativeAngleToPoint - math.radians(180) + preferredAngle

    movement_turn = clip(relativeTurnAngle/math.radians(30),-1,1) * turnSpeed

    if distanceToTarget < 10:
        movement_turn = 0
