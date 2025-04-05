# PCA9685 Motor Control Library for MicroPython

This library provides an interface to control motors through the PCA9685 PWM driver using I2C communication. The motors are controlled with forward or reverse directions based on the provided speed values.

## Features
- **Control motor speed**: Using PWM signals to control motor speed.
- **Forward/Reverse directions**: Motor direction can be set based on the provided speed value.
- **Configurable PWM frequency**: Set the PWM frequency for the motor driver.

## Requirements
- **MicroPython**: Ensure MicroPython is installed on your board.
- **PCA9685 PWM driver**: This library is designed to work with the PCA9685 I2C PWM driver.
- **Motor driver**: This library is for controlling motors through the PCA9685 board, so you need a  two pin motor driver (like the ZK-5A) connected to the board.

## Installation
1. Import the class.
2. Create an object.

