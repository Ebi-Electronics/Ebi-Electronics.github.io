Title: Introduction to UART Communication
Date: 2025-10-01
Category: Advanced

UART (Universal Asynchronous Receiver Transmitter) is a fundamental communication protocol used in many embedded systems.

## Serial Communication Basics

UART transmits data one bit at a time over two wires:
- TX (transmit): sends data
- RX (receive): receives data

## Baud Rate

Baud rate is the speed of communication, typically 9600 or 115200 bits per second.

## Arduino Serial Library

The Arduino Serial library provides easy UART communication:
- `Serial.begin(baud_rate)` - initialize
- `Serial.print()` - send data
- `Serial.read()` - receive data

## Practical Applications

- Debug output to computer
- Communication between Arduinos
- Sensor data logging
- Command interface
