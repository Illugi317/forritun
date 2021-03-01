from typing import Dict
from collections import defaultdict
RANK = "rank"
NAME = "name"
COUNTRY = "country"
SCORE = "score"
BIRTH_YEAR = "birth_year"


def main():
    #file_name = input("Enter filename: ")
    file_name = '/home/star/HR/forritun/16/chess.csv'
    players = read_player_data_from_csv(file_name)
    show_players_by_country(players)


def read_player_data_from_csv(file_name:str) -> list:
    players = []
    with open(file_name) as file_object:
        for line in file_object:
            player_dict = parse_line(line)
            players.append(player_dict)
    return players

def parse_line(line:str) -> dict:
    parts = line.split("; ")
    return{
        RANK: int(parts[0]),
        NAME: switch_last_and_first_names(parts[1]),
        COUNTRY: parts[2],
        SCORE: int(parts[3]),
        BIRTH_YEAR: int(parts[4])
    }
    
def switch_last_and_first_names(name: str) -> str:
    last_name, first_name = name.split(", ")
    return f"{first_name.strip()} {last_name.strip()}"


def show_players_by_country(players:list)->None:
    print("Player by country:")
    print("-------------------")
    players_by_country = group_players_by_country(players)
    sorted_countries = sorted(players_by_country.keys())
    for country in sorted_countries:
        country_players = players_by_country[country]
        show_country_stats(country,country_players)
        show_player_names_and_scores(country_players)

        pass

def group_players_by_country(players:list)->dict:
    grouped_players:Dict[str,list] = defaultdict(list)
    for player in players:
        country = player[COUNTRY]
        grouped_players[country].append(player)
    return grouped_players


def show_country_stats(country:str,players:list)->None:
    avarage_score = calculate_avarage_score(players)
    print(f"{country} ({len(players)}) ({avarage_score:.1f}):")

def calculate_avarage_score(players: list) -> float:
    scores = [player[SCORE] for player in players]
    return sum(scores)/len(players)

def show_player_names_and_scores(players:list)-> None:
    for player in players:
        print(f"{player[NAME]:>40} {player[SCORE]:>10d}")

main()