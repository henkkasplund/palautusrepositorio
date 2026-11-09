class Player:
    def __init__(self, player_dict):
        self.name = player_dict['name']
        self.nationality = player_dict['nationality']
        self.assists = player_dict['assists']
        self.goals = player_dict['goals']
        self.team = player_dict['team']

    @property
    def points(self):
        return self.goals + self.assists

    @property
    def teams(self):
        return [team.strip() for team in self.team.split(",")]

    def __str__(self):
        return f"{self.name:20} team {self.team:20} {self.goals:>2} + {self.assists:>3} = {self.points:3}"
