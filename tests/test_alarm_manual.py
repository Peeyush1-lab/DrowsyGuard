from app.alarm.alarm import Alarm
import time


alarm = Alarm("assets/sounds/alarm.mp3")

print("Playing alarm...")
alarm.play()

time.sleep(5)

print("Stopping alarm...")
alarm.stop()