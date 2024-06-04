import utime
from led import LED
from button import Button

# Setup the LEDs
led_pins = [8, 9]  # Add more pin numbers as needed
leds = [LED(pin) for pin in led_pins]

# Mapping from button pins to their corresponding LED indices
button_to_led_map = {
    1: 0,  # Button on pin 1 controls LED on pin 8
    2: 1,  # Button on pin 2 controls LED on pin 9
    # Add more mappings as needed
}

# Define a callback function for the button press
def button_pressed(pin_number):
    led_index = button_to_led_map.get(pin_number)
    if led_index is not None:
        leds[led_index].toggle()
        print(f"Button on pin {pin_number} pressed! Press count for pin {pin_number}: {buttons[pin_number].get_press_count()}")

# Setup the buttons
button_pins = [1, 2]  # Add more pin numbers as needed
buttons = {pin: Button(pin, button_pressed) for pin in button_pins}

# Keep the script running
while True:
    # Main loop can be used for other tasks
    utime.sleep(1)
