#!/usr/bin/python3
import os
from evdev import InputDevice, uinput, ecodes
import subprocess

deviceName = "PenTablet  Pen"
devEvent5 = InputDevice('/dev/input/event5') # PenTablet  Pen (xinput --list)
tabletButtons = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]
useLeftMonitor = 'xinput set-prop "PenTablet  Pen" --type=float "Coordinate Transformation Matrix" 0.5 0 0 0 1 0 0 0 1'
useRightMonitor = 'xinput set-prop "PenTablet  Pen" --type=float "Coordinate Transformation Matrix" 0.5 0 0.5 0 1 0 0 0 1'

for event in devEvent5.read_loop():
    # if button pressed
    if event.value in tabletButtons and event.code == 1 and event.type == 3:        
        if event.value == 1: # Zoom in
            with uinput.UInput() as ui:
                ui.write(ecodes.EV_KEY, ecodes.KEY_EQUAL, 1)
                ui.syn()
        if event.value == 2: # Zoom out
            with uinput.UInput() as ui:
                ui.write(ecodes.EV_KEY, ecodes.KEY_MINUS, 1)
                ui.syn()
        if event.value == 4: # Rotate left
            with uinput.UInput() as ui:
                ui.write(ecodes.EV_KEY, ecodes.KEY_4, 1)
                ui.syn()
        if event.value == 8: # Rotate right
            with uinput.UInput() as ui:
                ui.write(ecodes.EV_KEY, ecodes.KEY_6, 1)
                ui.syn()
        if event.value == 16:
            pass
        if event.value == 32:
            pass
        if event.value == 64: # Use left monitor
            subprocess.Popen(useLeftMonitor, shell=True, executable='/bin/bash')
        if event.value == 128: # Use right monitor
            subprocess.Popen(useRightMonitor, shell=True, executable='/bin/bash')
        if event.value == 256: # Undo
            with uinput.UInput() as ui:
                ui.write(ecodes.EV_KEY, ecodes.KEY_LEFTCTRL, 1)
                ui.write(ecodes.EV_KEY, ecodes.KEY_Z, 1)
                ui.syn()
        if event.value == 512: # Redo
            with uinput.UInput() as ui:
                ui.write(ecodes.EV_KEY, ecodes.KEY_LEFTCTRL, 1)
                ui.write(ecodes.EV_KEY, ecodes.KEY_LEFTSHIFT, 1)
                ui.write(ecodes.EV_KEY, ecodes.KEY_Z, 1)
                ui.syn()
        if event.value == 1024: # Hide all windows
            with uinput.UInput() as ui:
                ui.write(ecodes.EV_KEY, ecodes.KEY_LEFTCTRL, 1)
                ui.write(ecodes.EV_KEY, ecodes.KEY_LEFTMETA, 1)
                ui.write(ecodes.EV_KEY, ecodes.KEY_D, 1)
                ui.syn()
        if event.value == 2048: # Save
            with uinput.UInput() as ui:
                ui.write(ecodes.EV_KEY, ecodes.KEY_LEFTCTRL, 1)
                ui.write(ecodes.EV_KEY, ecodes.KEY_S, 1)
                ui.syn()
