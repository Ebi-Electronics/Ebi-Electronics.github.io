Title: Interrupt Handling in Arduino
Date: 2025-10-02
Category: Advanced

Interrupts allow your Arduino to respond immediately to external events without constantly polling.

## What are Interrupts?

When an interrupt occurs, the Arduino pauses current execution and runs an interrupt service routine (ISR).

## Hardware Interrupts

Arduino boards have external interrupts on specific pins:
- Uno: pins 2 and 3
- Mega: pins 2-13

## Interrupt Modes

- LOW: triggered when low
- CHANGE: triggered on any change
- RISING: triggered when going from low to high
- FALLING: triggered when going from high to low

## Attaching an Interrupt

```cpp
attachInterrupt(digitalPinToInterrupt(pin), ISR_function, mode);
```

## Using Interrupts

Best for responsive input like buttons or sensors that require immediate attention.
