from machine import I2C
import time
from MotorControl import PCA9685, Motor

# Initialize I2C bus and PCA9685
i2c = I2C(2)  # I2C bus 2
pca9685 = PCA9685(i2c_bus=2, address=0x40)

# Create a motor object with PCA9685 instance and two PWM pins
motor1 = Motor(pca9685, pin1=0, pin2=1)

# Run motor forward at 50% speed
motor1.forward(50)  # Forward direction, speed 50%
time.sleep(2)  # Run for 2 seconds

# Run motor reverse at 50% speed
motor1.forward(-50)  # Reverse direction, speed 50%
time.sleep(2)  # Run for 2 seconds

# Stop the motor
motor1.forward(0)  # Stop the motor
