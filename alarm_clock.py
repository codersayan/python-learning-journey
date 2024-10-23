import time

# Input the number of seconds for the alarm
seconds = int(input("Enter the number of seconds for the alarm: "))

print("Alarm set for", seconds, "seconds.")
time.sleep(seconds)
print("Alarm! Time's up!")
