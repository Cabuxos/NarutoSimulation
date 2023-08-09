from firsttry.Mission.AbstractMissionFactory import AbstractMissionFactory
from firsttry.Mission.SimpleMission import SimpleMission

class SimpleMissionFactory(AbstractMissionFactory):
    def create_mission(self, config):
        return SimpleMission(config["level"], config["tasks"])
