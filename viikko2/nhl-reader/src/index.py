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
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    while True:
        nationality = Prompt.ask("Nationality", choices=NATIONALITIES, default="")
        if nationality == "":
            break

        players = stats.top_scorers_by_nationality(nationality)

        Console().print(create_table(season, nationality, players))

def create_table(season, nationality, players):
    table = Table(title=f"Season {season} players from {nationality}")
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
