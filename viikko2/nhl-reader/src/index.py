from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from player_reader import PlayerReader
from player_stats import PlayerStats


SEASONS = ["2018-19", "2019-20", "2020-21", "2021-22",
           "2022-23", "2023-24", "2024-25", "2025-26"]
NATIONALITIES = ["USA", "FIN", "CAN", "SWE", "CZE", "RUS", "SLO", "FRA",
                 "GBR", "SVK", "DEN", "NED", "AUT", "BLR", "GER", "SUI",
                 "NOR", "UZB", "LAT", "AUS"]


def main():
    season = Prompt.ask("Season", choices=SEASONS, default="2024-25")

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    stats = PlayerStats(PlayerReader(url))

    while True:
        search_type = Prompt.ask(
            "Search by", choices=["Nationality", "Team", "Quit"], default="Nationality"
        )
        if search_type == "Quit":
            break

        value, players = ask_players(stats, search_type)
        Console().print(create_table(season, search_type.lower(), value, players))


def ask_players(stats, search_type):
    if search_type == "Nationality":
        value = Prompt.ask("Nationality", choices=NATIONALITIES)
        return value, stats.top_scorers_by_nationality(value)

    teams = sorted({team for player in stats.players for team in player.teams})
    value = Prompt.ask("Team", choices=teams)
    return value, stats.top_scorers_by_team(value)


def create_table(season, search_type, value, players):
    table = Table(title=f"Season {season} players by {search_type}: {value}")
    table.add_column("Name", style="cyan")
    table.add_column("Teams", style="magenta")
    table.add_column("Goals", justify="right", style="green")
    table.add_column("Assists", justify="right", style="green")
    table.add_column("Points", justify="right", style="green")

    for player in players:
        table.add_row(
            player.name,
            player.team,
            str(player.goals),
            str(player.assists),
            str(player.points),
        )
    return table

if __name__ == "__main__":
    main()
