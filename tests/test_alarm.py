from drowsyguard.alarm import Alarm
import time


alarm = Alarm("assets/sounds/alarm.mp3")

print("Playing alarm...")
alarm.play()

time.sleep(8)

print("Stopping alarm...")
alarm.stop()