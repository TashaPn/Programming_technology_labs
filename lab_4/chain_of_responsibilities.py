
class SupportHandler:
    def __init__(self):
        self.next = None

    def set_next(self, handler):
        self.next = handler

    def handle(self, problem):
        if self.next:
            return self.next.handle(problem)

        return "Проблему не удалось решить"


class FirstEmployee(SupportHandler):
    def handle(self, problem):
        if problem == "password":
            return "Первый сотрудник решил проблему"

        print("Первый сотрудник не смог решить проблему")
        return super().handle(problem)


class SecondEmployee(SupportHandler):
    def handle(self, problem):
        if problem == "internet":
            return "Второй сотрудник решил проблему"

        print("Второй сотрудник не смог решить проблему")
        return super().handle(problem)


class ThirdEmployee(SupportHandler):
    def handle(self, problem):
        if problem == "account":
            return "Третий сотрудник решил проблему"

        print("Третий сотрудник не смог решить проблему")
        return super().handle(problem)


first = FirstEmployee()
second = SecondEmployee()
third = ThirdEmployee()

first.set_next(second)
second.set_next(third)

print(first.handle("account"))
