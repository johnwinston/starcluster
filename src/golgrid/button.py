import machine
import utime

class Button:
    def __init__(self, pin_number, callback, debounce_interval=400):
        self.pin_number = pin_number
        self.pin = machine.Pin(pin_number, machine.Pin.IN)
        self.callback = callback
        self.debounce_interval = debounce_interval
        self.last_press_time = 0
        self.press_count = 0
        self.pin.irq(trigger=machine.Pin.IRQ_FALLING, handler=self._debounced_callback)

    def _debounced_callback(self, pin):
        current_time = utime.ticks_ms()
        if utime.ticks_diff(current_time, self.last_press_time) > self.debounce_interval:
            self.press_count += 1
            self.callback(self.pin_number)
            self.last_press_time = current_time

    def get_press_count(self):
        return self.press_count
