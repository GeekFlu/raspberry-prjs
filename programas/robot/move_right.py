import gpiozero
import time

robot = gpiozero.Robot(left=(17,18), right=(27,22))

for i in range(4):
    robot.right()
    print("turning")
    time.sleep(1)

robot.stop()
print("Stoping")

