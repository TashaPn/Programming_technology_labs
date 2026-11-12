class Device:
    def turn_on(self):
        pass


class TV(Device):
    def turn_on(self):
        print("Телевизор включён")


class AirConditioner(Device):
    def turn_on(self):
        print("Кондиционер включён")


class Remote:
    def __init__(self, device):
        self.device = device

    def press_button(self):
        self.device.turn_on()


tv_remote = Remote(TV())
tv_remote.press_button()

ac_remote = Remote(AirConditioner())
ac_remote.press_button()