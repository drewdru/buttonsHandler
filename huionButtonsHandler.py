from evdev import InputDevice, uinput, ecodes

devEvent5 = InputDevice('/dev/input/event5') # PenTablet  Pen (xinput --list)
tabletButtons = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]
for event in devEvent5.read_loop():
    with uinput.UInput() as ui:
        # if button pressed
        if event.value in tabletButtons and event.code == 1 and event.type == 3:
            if event.value == 1: # Zoom in
                ui.write(ecodes.EV_KEY, ecodes.KEY_EQUAL, 1)
            if event.value == 2: # Zoom out
                ui.write(ecodes.EV_KEY, ecodes.KEY_MINUS, 1)
            if event.value == 4: # Rotate left
                ui.write(ecodes.EV_KEY, ecodes.KEY_4, 1)
            if event.value == 8: # Rotate right
                ui.write(ecodes.EV_KEY, ecodes.KEY_6, 1)
            if event.value == 16:
                pass
            if event.value == 32:
                pass
            if event.value == 64:
                pass
            if event.value == 32:
                pass
            if event.value == 256: # Undo
                ui.write(ecodes.EV_KEY, ecodes.KEY_LEFTCTRL, 1)
                ui.write(ecodes.EV_KEY, ecodes.KEY_Z, 1)
            if event.value == 512: # Redo
                ui.write(ecodes.EV_KEY, ecodes.KEY_LEFTCTRL, 1)
                ui.write(ecodes.EV_KEY, ecodes.KEY_LEFTSHIFT, 1)
                ui.write(ecodes.EV_KEY, ecodes.KEY_Z, 1)
            if event.value == 1024: # Hide all windows
                ui.write(ecodes.EV_KEY, ecodes.KEY_LEFTCTRL, 1)
                ui.write(ecodes.EV_KEY, ecodes.KEY_LEFTMETA, 1)
                ui.write(ecodes.EV_KEY, ecodes.KEY_D, 1)
            if event.value == 2048: # Save
                ui.write(ecodes.EV_KEY, ecodes.KEY_LEFTCTRL, 1)
                ui.write(ecodes.EV_KEY, ecodes.KEY_S, 1)
        ui.syn()
