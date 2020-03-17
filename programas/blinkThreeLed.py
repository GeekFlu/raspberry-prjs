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
	time.sleep(1)
	ledRed.off()

	ledGreen.on()
	time.sleep(1)
	ledGreen.off()

	ledYellow.on()
	time.sleep(1)
	ledYellow.off()
