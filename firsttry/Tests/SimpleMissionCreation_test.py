from firsttry.Mission.SimpleMissionFactory import SimpleMissionFactory
from firsttry.Mission.SimpleTask import SimpleTask

mission_config = {
    "level": "D",
    "tasks": [SimpleTask("Задача 1"), SimpleTask("Задача 2")]
}

mission_factory = SimpleMissionFactory()
mission = mission_factory.create_mission(mission_config)

print(f"Mission lvl: {mission.level}")
print(f"Mission description: {mission.tasks[0].description}")