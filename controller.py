import RPi.GPIO as gpio
import time
import sys
import pygame

# Setup GPIO mode and pin configuration
gpio.setmode(gpio.BCM)
gpio.setup(4, gpio.OUT)   # Motor 1 (left) forward pin
gpio.setup(5, gpio.OUT)   # Motor 2 (right) forward pin
gpio.setwarnings(False)

# Setup PWM for the motors
motor1_forward_pwm = gpio.PWM(4, 100)  # Motor 1 (left) forward
motor2_forward_pwm = gpio.PWM(5, 100)  # Motor 2 (right) forward

motor1_forward_pwm.start(0)
motor2_forward_pwm.start(0)

def set_motor_speed(motor_pwm, speed_percent):
    motor_pwm.ChangeDutyCycle(speed_percent)

def stop_motors():
    set_motor_speed(motor1_forward_pwm, 0)
    set_motor_speed(motor2_forward_pwm, 0)

# Initialize Pygame and joystick
pygame.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

max_speed = 100  # Maximum speed

try:
    while True:
        pygame.event.pump()
        axis_x = joystick.get_axis(0)  # Get X-axis value of joystick
        axis_y = -joystick.get_axis(1)  # Get Y-axis value of joystick and invert
        
        # Calculate motor speeds based on joystick input
        speed_motor1 = int(axis_y * max_speed) + int(axis_x * max_speed)  # Motor 1 (left)
        speed_motor2 = int(axis_y * max_speed) - int(axis_x * max_speed)  # Motor 2 (right)
        
        # Map motor speeds to valid duty cycle range
        speed_motor1_dc = max(0, min(abs(speed_motor1), 100))  # Limit to 0-100
        speed_motor2_dc = max(0, min(abs(speed_motor2), 100))  # Limit to 0-100
        
        # Set motor speeds based on joystick input
        set_motor_speed(motor1_forward_pwm, speed_motor1_dc)
        set_motor_speed(motor2_forward_pwm, speed_motor2_dc)
        
        time.sleep(0.05)

except KeyboardInterrupt:
    stop_motors()
    joystick.quit()
    pygame.quit()
    sys.exit()
