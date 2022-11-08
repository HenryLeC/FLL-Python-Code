import time


class PID:
    def __init__(self, p: float, i: float, d: float):
        self.kp = p
        self.ki = i
        self.kd = d
        self.last_call = None

        self.integral = 0.0
        self.last_error = 0.0

    def calculate(self, measurement: float, setpoint: float,
                  dt: float = None) -> float:
        now = time.time()

        if dt is None:
            if self.last_call is None:
                dt = 0
            else:
                dt = now - self.last_call
        self.last_call = now

        error = setpoint - measurement
        self.integral += error * dt
        derivative = (error - self.last_error) / (dt if dt != 0 else 1)

        output = self.kp * error + \
            self.ki * self.integral + \
            self.kd * derivative

        self.last_error = error
        return output
