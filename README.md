# ric-grill

The plan is to have a custom controller for the Optigrill by Tefal where you can just set a temperature and not worry about all the shit in the normal controller.

## Status

This project is in its baby steps and **not yet functional**! Almost nothing is implemented so far.

## Documentation

- How to install (Not written yet)
- [Interpolation](docs/Interpolation.pdf)

## Requirements

This is **subject to change!**

### Hardware

- Raspberry Pi Pico
- Screwdriver
- SH1106 I2C OLED display with a resolution of 128 x 64 that fits in the OptiGrill
  - I recommend [this one from AZ-Delivery](https://www.az-delivery.de/en/products/1-3zoll-i2c-oled-display), but other ones should work as well
- Soldering iron
- Tefal Optigrill (obviously)

### Software

- CircuitPython
- interpolation.mpy (included)
