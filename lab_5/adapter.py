class USB_C:
    def connect(self):
        print("Устройство подключено через USB-C")


class USB_A:
    def connect_usb_a(self):
        print("Компьютер подключён через USB-A")


class Adapter:
    def __init__(self, device):
        self.device = device

    def connect(self):
        print("Адаптер преобразует USB-A в USB-C")
        self.device.connect()


device = USB_C()
adapter = Adapter(device)
adapter.connect()