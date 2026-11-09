import unittest

from player import Player
from player_stats import PlayerStats


class PlayerReaderStub:
    def get_players(self):
        return [
            Player({
                "name": "Alex Multi",
                "nationality": "FIN",
                "assists": 30,
                "goals": 20,
                "team": "COL, CAR, DAL",
            }),
            Player({
                "name": "Bill Finland",
                "nationality": "FIN",
                "assists": 10,
                "goals": 30,
                "team": "BOS",
            }),
            Player({
                "name": "Chris Canada",
                "nationality": "CAN",
                "assists": 25,
                "goals": 10,
                "team": "DAL",
            }),
            Player({
                "name": "Dana Finland",
                "nationality": "FIN",
                "assists": 5,
                "goals": 10,
                "team": "COL",
            }),
            Player({
                "name": "Eddie USA",
                "nationality": "USA",
                "assists": 5,
                "goals": 35,
                "team": "NYR",
            }),
        ]


class TestPlayerStats(unittest.TestCase):
    def setUp(self):
        self.stats = PlayerStats(PlayerReaderStub())

    def test_top_scorers_by_nationality_returns_players_ordered_by_points(self):
        players = self.stats.top_scorers_by_nationality("FIN")

        self.assertEqual(
            [player.name for player in players],
            ["Alex Multi", "Bill Finland", "Dana Finland"],
        )

    def test_top_scorers_by_team_includes_player_with_multiple_teams(self):
        players = self.stats.top_scorers_by_team("DAL")

        self.assertEqual(
            [player.name for player in players],
            ["Alex Multi", "Chris Canada"],
        )

    def test_top_goal_scorers_returns_requested_number_ordered_by_goals(self):
        players = self.stats.top_goal_scorers(3)

        self.assertEqual(
            [player.name for player in players],
            ["Eddie USA", "Bill Finland", "Alex Multi"],
        )


if __name__ == "__main__":
    unittest.main()
