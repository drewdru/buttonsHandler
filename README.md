# buttonsHandler

Script for handling Huion wh1409 buttons

# Build

In `buttons.py` change path to your device, and commands for button.
Then make the script run at startup

## Get path to your device and buttons

use evtest in console:

    sudo evtest

You will see all your input devices like "path  deviceName". If you don't sure
what is your device write number and try to use buttons on the device then
you will see info about pressed button (time when button was pressed, type,
code, and value).

## Install dependencies

    sudo pip3 install evdev

# Sevice set up

To view device properties run:

    xinput --list-props "PenTablet  Pen"

## Dual and multiMonitor set up for graphics tablet

If you have two or more monitors and want to confine the stylus to one screen you can use the Coordinate Transformation Matrix to accomplish that. For example with two monitors of the same size side by side you would use:

### left monitor

    xinput set-prop "device name" --type=float "Coordinate Transformation Matrix" 0.5 0 0 0 1 0 0 0 1

### Right monitor

    xinput set-prop "device name" --type=float "Coordinate Transformation Matrix" 0.5 0 0.5 0 1 0 0 0 1

## More about graphics tablet set up

For more information about graphics tablet setup see https://digimend.github.io/support/howto/drivers/evdev/
And where you can try to find drivers for your graphics tablet
