""" Extract Data from ESPN Fantasy Football League into Delimited File """
import datetime
from espn_api.football import League
from colorama import Fore, Back, Style
import config
import testing_config


def extract_team_records(file_path, delimiter=',', is_test=False) -> None:
    """ Extract ESPN Fantasy Owner/League Data into Delimited File """
    # Load testing configuration or real configuration
    data = testing_config if is_test else config
    print(f'{Back.CYAN}{Fore.WHITE}Extracting{Fore.RED} ESPN {Fore.WHITE}Data')
    today = datetime.date.today()
    with open(file_path, "a", encoding="utf8") as file:
        headers = ['owner', 'year', 'team_name', 'win', 'loss', 'draws', 'final_standing',
                   'points_for', 'points_against', 'acquisitions', 'trades', 'drops',
                   'streak_length', 'streak_type', 'playoff_seed']
        file.write(f'{format_data(headers, delimiter)}\n')
        # CSV header
        end_year = today.year if data.is_active else data.year_founded + 1
        for year in range(data.year_founded, end_year):
            print(f'{Fore.BLACK}Processing Year {Fore.WHITE}{year}')
            if is_test:
                league = League(league_id=data.league_id, year=year)
            else:
                league = League(league_id=data.league_id, year=year,
                                espn_s2=data.s2, swid=data.swid)
            for team in league.teams:
                datas = [team.owner, year, clean_name(team.team_name), team.wins, team.losses,
                         team.ties, team.final_standing, team.points_for, team.points_against,
                         team.acquisitions, team.trades, team.drops, team.streak_length,
                         team.streak_type, team.standing]
                file.write(f'{format_data(datas, delimiter)}\n')
    print(f'{Fore.YELLOW}Extraction Complete{Style.RESET_ALL}')


def clean_name(name) -> str:
    """ Clean name string that comes from espn_api """
    return name.replace("'", "")


def format_data(datas, delimiter) -> str:
    """ Format data list into delimited string """
    output = ''
    # Build output
    for data in datas:
        output += f'{data}{delimiter}'
    # Removing trailing seperator
    return output[:-len(delimiter)]
