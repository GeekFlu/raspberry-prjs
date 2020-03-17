import gpiozero
import time

ledRed = gpiozero.LED(27)
ledYellow = gpiozero.LED(17)
ledGreen = gpiozero.LED(4)

ledRed.off()
ledYellow.off()
ledGreen.off()

while True:
	ledRed.on()
	time.sleep(6)
	ledRed.off()

	ledYellow.on()
	time.sleep(3)
	ledYellow.off()

	ledGreen.on()
	time.sleep(2)
	ledGreen.off()

