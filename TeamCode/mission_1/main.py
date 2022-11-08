# LEGO type:standard slot:0 autostart

import hub
import time
from PID import PID  # ../PID.py


gyro_pid = PID(1, 0, 0)

motorPair = hub.port.C.motor.pair(hub.port.D.motor)

start = time.time()
start_heading: int = hub.motion.yaw_pitch_roll()[0]

while (time.time() - start) < 100:
    out = gyro_pid.calculate(hub.motion.yaw_pitch_roll()[0], start_heading)
    print(
        "out: {} heading: {}"
        .format(out, hub.motion.yaw_pitch_roll()[0] - start_heading)
    )
    motorPair.run_at_speed(-out-75, -out+75)


time.sleep(1)

motorPair.hold()

raise SystemExit("Done")
