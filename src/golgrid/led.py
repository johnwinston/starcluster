import machine

class LED:
    def __init__(self, pin_number):
        self.pin = machine.Pin(pin_number, machine.Pin.OUT)
        self.state = False

    def on(self):
        self.pin.value(1)
        self.state = True

    def off(self):
        self.pin.value(0)
        self.state = False

    def toggle(self):
        self.state = not self.state
        self.pin.value(self.state)

    def get_state(self):
        return self.state
