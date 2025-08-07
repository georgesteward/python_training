# Code performs a countdown and plays a sound when the time is up.
# It takes input in minutes and seconds from the user.
from playsound import playsound
import time

def alarm(seconds):
    time_elapsed = 0

    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1
        # print(f"Time elapsed: {time_elapsed} seconds")

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60
        print(f"Time left: {minutes_left:02d} minutes and {seconds_left:02d} seconds", end='\r')

    playsound("hello.mp3")

minutes = int(input("Enter the number of minutes for the alarm: "))
seconds = int(input("Enter the number of seconds for the alarm: "))
total_seconds = minutes * 60 + seconds
alarm(total_seconds)
