Title: Creating a Weather Station with Arduino
Date: 2025-10-03
Category: Project

Build a complete weather station that measures temperature, humidity, and air pressure.

## Components List

- Arduino Mega or Uno
- DHT22 temperature/humidity sensor
- BMP280 pressure sensor
- 16x2 LCD display
- Breadboard and wires

## Assembly

Connect the sensors to I2C pins (SDA/SCL) on your Arduino. The DHT22 uses a single data pin. Mount everything in a weatherproof box.

## Code Structure

1. Initialize sensors
2. Read sensor values in a loop
3. Calculate averages
4. Display on LCD

## Data Logging

Extend the project by logging data to an SD card for later analysis.
