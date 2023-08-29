""" Extract Data from ESPN Fantasy Football League into Delimited File """
import datetime
import sys

from espn_api.football import League
from colorama import Fore, Back, Style
from espn_extractor.utils import tools

HEADERS = ['Name', 'Position', 'POS-Rank', 'Team', 'Projection', 'Status']
POSITIONS = ['QB', 'RB', 'WR', 'TE', 'D/ST', 'K']


def extract_draft_board(config, size, is_test=False) -> None:
    """ Extract ESPN Fantasy Draft Projects into Delimited File """
    # Load testing configuration or real configuration
    print(f'{Back.CYAN}{Fore.WHITE}Extracting{Fore.RED} ESPN {Fore.WHITE}Data')
    today = datetime.date.today()
    output_file = f'{config.output_dir}/{config.draft_file}'
    with open(output_file, "a", encoding="utf8") as file:
        file.write(f'{tools.format_data(HEADERS, config.format)}\n')
        print(f'{Fore.BLACK}Processing Year {Fore.WHITE}{today.year}')
        league = get_league(config, is_test)
        for position in POSITIONS:
            for player in league.free_agents(position=position, size=size):
                if position == 'DST':
                    datas = [player.name, position, player.posRank, player.proTeam,
                             player.projected_points, None]
                else:
                    datas = [player.name, position, player.posRank, player.proTeam,
                             player.projected_points, player.injuryStatus]

                file.write(f'{tools.format_data(datas, config.format)}\n')
    print(f'{Fore.YELLOW}Extraction Complete{Style.RESET_ALL}\n')


def extract_draft_positions(config, size, is_test=False) -> None:
    """ Extract ESPN data into position data files """
    print(f'{Back.CYAN}{Fore.WHITE}Extracting{Fore.RED} ESPN {Fore.WHITE}Data')
    for position in POSITIONS:
        generate_position_data(config, position, size, is_test)
    print(f'{Fore.YELLOW}Extraction Complete{Style.RESET_ALL}\n')


def extract_draft_position(config, position, size, is_test=False) -> None:
    """ Extract ESPN data for a position into a data file"""
    # Load testing configuration or real configuration
    print(f'{Back.CYAN}{Fore.WHITE}Extracting{Fore.RED} ESPN {Fore.WHITE}Data')
    # Users can pass DST or D/ST
    if position in POSITIONS or position == 'DST':
        generate_position_data(config, position, size, is_test)
    else:
        print(f'{Fore.RED}Position {position} not supported {Style.RESET_ALL}\n')
        sys.exit(1)
    print(f'{Fore.YELLOW}Extraction Complete{Style.RESET_ALL}\n')


def generate_position_data(config, position, size, is_test):
    """ Extract ESPN Fantasy Draft data into file """
    league = get_league(config, is_test)
    print(f'{Fore.BLACK}Processing Position {Fore.WHITE}{position}')
    position = 'DST' if position == 'D/ST' else position
    file_name = f'{config.output_dir}/{position}.csv'
    with open(file_name, "a", encoding="utf8") as file:
        file.write(f'{tools.format_data(HEADERS, config.format)}\n')
        for player in league.free_agents(position=position, size=size):
            if position == 'DST':
                datas = [player.name, position, player.posRank, player.proTeam,
                         player.projected_points, None]
            else:
                datas = [player.name, position, player.posRank, player.proTeam,
                         player.projected_points, player.injuryStatus]
            file.write(f'{tools.format_data(datas, config.format)}\n')


def get_league(data, is_test) -> League:
    """ Returns league or test league """
    today = datetime.date.today()
    if is_test:
        return League(league_id=data.league_id, year=today.year)
    return League(league_id=data.league_id, year=today.year,
                  espn_s2=data.s2, swid=data.swid)
