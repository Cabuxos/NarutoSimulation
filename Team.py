from typing import List
from Shinobi import Shinobi


class Team:
    def __init__(self, name="<BasicTeamName>", members: List[Shinobi]=None):
        self.name = name
        self.members = members or []
        self.leader = None

    def add_member(self, shinobi):
        if len(self.members) < 4:
            if isinstance(shinobi, Shinobi):
                if shinobi not in self.members:
                    self.members.append(shinobi)
                else:
                    print(f"Shinobi {shinobi.name} is already a member of {self.name}!")
            else:
                print("Who is that?!")
        else:
            print("Team's already assembled!")

    def delete_member(self, shinobi):
        if shinobi in self.members:
            if shinobi == self.leader and self.leader:
                self.leader = None
            self.members.remove(shinobi)
            print(f"{shinobi.name} has been excluded from team {self.name}")

    def set_leader(self, leader):
        if leader in self.members:
            self.leader = leader
            print(f"New team leader: {self.leader.name}!")
        else:
            print("Who is that?")

    def display_team(self):
        print(f"Team {self.name} members:")
        if self.leader:
            print(f"Team {self.name} leader: {self.leader.name}")
        else:
            print(f"Team {self.name} has no leader...")
        for member in self.members:
            if member is not self.leader:
                print(f"Team member: {member.name}")
