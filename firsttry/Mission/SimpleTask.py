from firsttry.Mission.AbstractTask import AbstractTask


class SimpleTask(AbstractTask):
    def __init__(self, description):
        super().__init__(description)

    def complete(self):
        self.is_completed = True
        print(f"Задача '{self.description}' завершена!")