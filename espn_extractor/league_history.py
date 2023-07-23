""" Extract Data from ESPN Fantasy Football League into Delimited File """
import datetime
from espn_api.football import League
from colorama import Fore, Back, Style
from espn_extractor.utils import tools


def extract_team_records(config, is_test=False) -> None:
    """ Extract ESPN Fantasy Owner/League Data into Delimited File """
    # Load testing configuration or real configuration
    print(f'{Back.CYAN}{Fore.WHITE}Extracting{Fore.RED} ESPN {Fore.WHITE}Data')
    today = datetime.date.today()
    file_name = f'{config.output_dir}/{config.history_file}'
    with open(file_name, "a", encoding="utf8") as file:
        headers = ['owner', 'year', 'team_name', 'win', 'loss', 'draws', 'final_standing',
                   'points_for', 'points_against', 'acquisitions', 'trades', 'drops',
                   'streak_length', 'streak_type', 'playoff_seed']
        file.write(f'{tools.format_data(headers, config.format)}\n')
        # CSV header
        end_year = today.year if config.is_active else config.year_founded + 1
        for year in range(config.year_founded, end_year):
            print(f'{Fore.BLACK}Processing Year {Fore.WHITE}{year}')
            if is_test:
                league = League(league_id=config.league_id, year=year)
            else:
                league = League(league_id=config.league_id, year=year,
                                espn_s2=config.s2, swid=config.swid)
            for team in league.teams:
                datas = [team.owner, year, tools.clean_name(team.team_name), team.wins, team.losses,
                         team.ties, team.final_standing, team.points_for, team.points_against,
                         team.acquisitions, team.trades, team.drops, team.streak_length,
                         team.streak_type, team.standing]
                file.write(f'{tools.format_data(datas, config.format)}\n')
    print(f'{Fore.YELLOW}Extraction Complete{Style.RESET_ALL}\n')
