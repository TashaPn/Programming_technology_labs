class Photo:
    def load(self):
        print("Фотография загружена")


class PhotoProxy:
    def __init__(self, has_access):
        self.has_access = has_access
        self.photo = Photo()

    def load(self):
        if self.has_access:
            self.photo.load()
        else:
            print("Доступ запрещён")


proxy = PhotoProxy(False)
proxy.load()

proxy = PhotoProxy(True)
proxy.load()