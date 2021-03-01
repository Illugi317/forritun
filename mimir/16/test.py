import csv

RANK = "rank"
NAME = "name"
COUNTRY = "country"
SCORE = "score"
BIRTH_YEAR = "birth year"


def switch_names(name: str) -> str:
    names = name.split(", ")

    return f"{names[1]} {names[0]}"


def parse_line(line: str) -> dict:
    parts = [part.strip() for part in line.split(";")]
    return {
        RANK: int(parts[0]),
        NAME: switch_names(parts[1]),
        COUNTRY: parts[2],
        SCORE: int(parts[3]),
        BIRTH_YEAR: int(parts[4])
    }


def read_player_data_csv(filename: str) -> list:
    players = []
    with open(filename, "r") as f:
        for line in f:
            players_dict = parse_line(line)
            players.append(players_dict)

    return players


def group_players_by_country(players: list) -> dict:
    grouped_players = {}

    for player in players:
        country = player[COUNTRY]
        if country not in grouped_players:
            grouped_players[country] = []

        grouped_players[country].append(player)

    return  grouped_players


def get_average(players: list) -> float:
    return round(sum([player[SCORE] for player in players]) / len(players), 1)


def show_country_stats(country: str, players: list) -> None:
    average_score = get_average(players)
    print(f"{country} ({len(players)}) ({average_score}):")


def show_player_name_and_score(players: list) -> None:
    for player in players:
        print(f"{player[NAME]:>40}{player[SCORE]:>10d}")


def group_players_by_birth_year(players) -> dict:
    grouped_players = {}

    for player in players:
        birth_year = player[BIRTH_YEAR]
        if birth_year not in grouped_players:
            grouped_players[birth_year] = []

        grouped_players[birth_year].append(player)

    return grouped_players


def show_players_by_birth_year(players: list):
    print("Players by birth year:")
    print("-------------------")
    players_by_country = group_players_by_birth_year(players)
    sorted_countries = sorted(players_by_country.keys())
    for country in sorted_countries:
        country_players = players_by_country[country]
        show_country_stats(country, country_players)
        show_player_name_and_score(country_players)

def show_players_by_country(players: list):
    print("Players by country:")
    print("-------------------")
    players_by_country = group_players_by_country(players)
    sorted_countries = sorted(players_by_country.keys())
    for country in sorted_countries:
        country_players = players_by_country[country]
        show_country_stats(country, country_players)
        show_player_name_and_score(country_players)



def main() -> None:
    file_name = input("Enter filename: ")
    # file_name = "data.csv"
    players = read_player_data_csv(file_name)
    show_players_by_country(players)
    show_players_by_birth_year(players)
if __name__ == '__main__':
        main()