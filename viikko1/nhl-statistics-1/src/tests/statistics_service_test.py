import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
	def get_players(self):
		return [
			Player("Semenko", "EDM", 4, 12),
			Player("Lemieux", "PIT", 45, 54),
			Player("Kurri",   "EDM", 37, 53),
			Player("Yzerman", "DET", 42, 56),
			Player("Gretzky", "EDM", 35, 89)
		]

class TestStatisticsService(unittest.TestCase):
	def setUp(self):
		self.stats = StatisticsService(PlayerReaderStub())

	def test_search_when_not_in(self):
		search = self.stats.search("ä")
		self.assertIsNone(search)

	def test_search_when_in(self):
		search = self.stats.search("Semenko")
		self.assertIsNotNone(search)

	def test_team_when_in(self):
		team = self.stats.team("ABC")
		self.assertIsNotNone(team)

	def test_team_when_not_in(self):
		team = self.stats.team("EDM")
		self.assertIsNotNone(team)

	def test_top(self):
		team = self.stats.top(1)
		self.assertEqual(team[0].name, "Gretzky")
		
	def test_top_goals(self):
		team = self.stats.top(1, SortBy.GOALS)
		self.assertEqual(team[0].name, "Lemieux")
		
	def test_top_assists(self):
		team = self.stats.top(1, SortBy.ASSISTS)
		self.assertEqual(team[0].name, "Gretzky")
