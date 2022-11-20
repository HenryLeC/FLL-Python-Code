class CurvePoint:
    def __init__(self, x: float, y: float, moveSpeed: float, turnSpeed: float, followDistance: float, slowDownTurnRadians: float, slowDownTurnAmmount: float):
        self.x = x
        self.y = y
        self.moveSpeed = moveSpeed
        self.turnSpeed = turnSpeed
        self.followDistance = followDistance
        self.slowDownTurnRadians = slowDownTurnRadians
        self.slowDownTurnAmmount = slowDownTurnAmmount

    def __init__(self, thisPoint: "CurvePoint"):
        self.x = thisPoint.x
        self.y = thisPoint.y
        self.moveSpeed = thisPoint.moveSpeed
        self.turnSpeed = thisPoint.turnSpeed
        self.followDistance = thisPoint.followDistance
        self.slowDownTurnRadians = thisPoint.slowDownTurnRadians
        self.slowDownTurnAmmount = thisPoint.slowDownTurnAmmount
    