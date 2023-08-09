from firsttry.Mission.AbstractMission import AbstractMission


class SimpleMission(AbstractMission):
    def __init__(self, level, tasks):
        super().__init__(level, tasks)

    def is_completed(self):
        return all(task.is_completed for task in self.tasks)