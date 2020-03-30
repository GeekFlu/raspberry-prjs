import argparse 
import gpiozero
import time

  
# Initialize parser 
parser = argparse.ArgumentParser() 
  
# Adding optional argument 
parser.add_argument("-d", "--direction", help = "Rovr Direction") 
parser.add_argument("-s", "--steps",type=int, help = "Number of steps the Rovr should walk")
parser.add_argument("-r", "--reverse",type=bool, help = "Reverse modo activated")
parser.add_argument("-t", "--time",type=float, help = "Time executing the command each step")
# Read arguments from command line 
args = parser.parse_args() 
  
if args.direction and args.steps: 
    print("Diplaying Rovr direction as: % s" % args.direction)
    print("Displaying Rovr steps to perform %s" % args.steps)
    robot = gpiozero.Robot(left=(4,14), right=(17,18))
    if args.reverse:
        print("Activating REVERSE MOdo!!!!!!")
        robot.reverse()
    d = args.direction.lower()
    if args.time:
        tt = args.time
    else:
        tt = 2
    for i in range(args.steps):
        
        if d == 'left':
            print("Moving LEFT")
            robot.left()
            time.sleep(tt)
        elif d == 'right':
            print("Moving RIGTH")
            robot.right()
            time.sleep(tt)
        elif d == 'forward':
            print("Moving FORWARD")
            robot.forward()
            time.sleep(tt)
        elif d == 'backward':
            print("Moving BACKWARD")
            robot.backward()
            time.sleep(tt)
        
    robot.stop()
    print("Stoping Rovr")

else:
    print("Need both arguments Directions and steps...")
