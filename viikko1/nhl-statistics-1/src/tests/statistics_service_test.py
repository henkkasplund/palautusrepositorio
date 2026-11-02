import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_loytaa_pelaajan(self):
        player = self.stats.search("Kurri")
        self.assertEqual(player.name, "Kurri")

    def test_search_palauttaa_none_jos_ei_loydy(self):
        player = self.stats.search("Asplund")
        self.assertIsNone(player)

    def test_team_palauttaa_joukkueen_pelaajat(self):
        team = self.stats.team("EDM")
        self.assertEqual(len(team), 3)

    def test_top_oletuksena_pisteiden_mukaan(self):
        top = self.stats.top(2)
        self.assertEqual([p.name for p in top], ["Gretzky", "Lemieux"])

    def test_top_palauttaa_parhaat_maalintekijat(self):
        top = self.stats.top(2, SortBy.GOALS)
        self.assertEqual([p.name for p in top], ["Lemieux", "Yzerman"])

    def test_top_palauttaa_parhaat_syottajat(self):
        top = self.stats.top(2, SortBy.ASSISTS)
        self.assertEqual([p.name for p in top], ["Gretzky", "Yzerman"])

    def test_top_palauttaa_parhaat_pisteidentekijat(self):
        top = self.stats.top(2, SortBy.POINTS)
        self.assertEqual([p.name for p in top], ["Gretzky", "Lemieux"])