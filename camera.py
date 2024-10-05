# Import libraries
import RPi.GPIO as GPIO
import time
from picamera import PiCamera

# Set GPIO mode and pins
GPIO.setmode(GPIO.BCM)
TRIG = 18 # Trigger pin for ultrasonic sensor
ECHO = 24 # Echo pin for ultrasonic sensor
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

# Initialize camera
camera = PiCamera()

# Define a function to measure distance using ultrasonic sensor
def measure_distance():
    # Send a pulse to trigger pin
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    
    # Record the start and end time of the echo
    start = time.time()
    end = time.time()
    while GPIO.input(ECHO) == 0:
        start = time.time()
    while GPIO.input(ECHO) == 1:
        end = time.time()
    
    # Calculate the distance based on the speed of sound
    duration = end - start
    distance = duration * 34300 / 2 # Speed of sound is 34300 cm/s
    distance = round(distance, 2)
    return distance

# Main loop
try:
    while True:
        # Measure the distance and print it
        dist = measure_distance()
        print("Distance: {} cm".format(dist))
        
        # If the distance is less than 50 cm, take a picture and a video
        if dist < 50:
            # Take a picture and save it with timestamp
            timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")
            camera.start_preview()
            time.sleep(2)
            camera.capture("/home/raspi/Pictures/{}.jpg".format(timestamp))
            camera.stop_preview()
            print("Picture saved as {}.jpg".format(timestamp))
            
            # Take a video and save it with timestamp
            camera.start_preview()
            camera.start_recording("/home/raspi/Videos/{}.h264".format(timestamp))
            time.sleep(10)
            camera.stop_recording()
            camera.stop_preview()
            print("Video saved as {}.h264".format(timestamp))
        
        # Wait for 1 second before next measurement
        time.sleep(1)

# Exit gracefully by pressing Ctrl+C
except KeyboardInterrupt:
    print("Program stopped by user")
    GPIO.cleanup()
    camera.close()
