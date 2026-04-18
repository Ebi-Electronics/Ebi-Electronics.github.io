Title: PWM and Analogwrite Explained
Date: 2025-10-05
Category: Tutorial

Pulse Width Modulation (PWM) allows you to control the brightness of LEDs and speed of motors.

## What is PWM?

PWM rapidly switches a digital signal between high and low. By varying the ratio of on-time to off-time, you can simulate analog control.

## Duty Cycle

The percentage of time the signal is high. A 50% duty cycle means the signal is on half the time.

## Using Analogwrite in Arduino

The `analogWrite()` function sets PWM on pins 3, 5, 6, 9, 10, and 11 on most Arduino boards.

```cpp
analogWrite(pin, value); // value: 0-255
```

Value 0 = fully off, 255 = fully on, 128 = 50% brightness.
