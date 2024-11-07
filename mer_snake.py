
import RPi.GPIO as GPIO; import time
GPIO.setmode(GPIO.BCM)
time.sleep(5) # to put the MER on the ground
motor_left = 4; motor_right = 5; run_time = 0

GPIO.setup(motor_left, GPIO.OUT); GPIO.setup(motor_right, GPIO.OUT)

while run_time < 2:
    #straight
    GPIO.output(motor_left, True); GPIO.output(motor_right, True); time.sleep(1.0)
    GPIO.output(motor_left, False); GPIO.output(motor_right, False)
    #right
    GPIO.output(motor_left, True); time.sleep(1.5); GPIO.output(motor_left, False)
    #straight
    GPIO.output(motor_left, True); GPIO.output(motor_right, True); time.sleep(1.0)
    GPIO.output(motor_left, False); GPIO.output(motor_right, False)
    #left
    GPIO.output(motor_right, True); time.sleep(1.5); GPIO.output(motor_right, False)
    #straight
    GPIO.output(motor_left, True); GPIO.output(motor_right, True); time.sleep(1.0)
    GPIO.output(motor_left, False); GPIO.output(motor_right, False)
    #right
    GPIO.output(motor_left, True); time.sleep(1.5); GPIO.output(motor_left, False)
    #straight
    GPIO.output(motor_left, True); GPIO.output(motor_right, True); time.sleep(1.0)
    GPIO.output(motor_left, False); GPIO.output(motor_right, False)
    #left
    GPIO.output(motor_right, True); time.sleep(1.5); GPIO.output(motor_right, False)
    run_time = run_time+1
    GPIO.cleanup() 
    

