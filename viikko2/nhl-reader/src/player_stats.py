class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        players = []
        for player in self.players:
            if player.nationality == nationality:
                players.append(player)

        return sorted(players, key=lambda p: p.points, reverse=True)

    def top_scorers_by_team(self, team):
        players = []
        for player in self.players:
            if team in player.teams:
                players.append(player)

        return sorted(players, key=lambda p: p.points, reverse=True)

    def top_goal_scorers(self, how_many):
        """Palauttaa how_many eniten maaleja tehnyttä pelaajaa maalimäärän mukaan laskevassa järjestyksessä"""
        return sorted(self.players, key=lambda player: player.goals, reverse=True)[:how_many]
