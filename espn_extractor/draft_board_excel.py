""" Extract Data from ESPN Fantasy Football League into Delimited File """
import datetime
import pandas as pd
from espn_api.football import League
from colorama import Fore, Back, Style

HEADERS = ['Name', 'Position', 'POS-Rank', 'Team', 'Projection', 'Status']
POSITIONS = ['RB', 'WR', 'TE', 'D/ST', 'K']


def extract_draft_cheatsheet(config, size, is_test=False) -> None:
    """ Extract ESPN Fantasy Draft Projects by Position into Delimited File """
    # Load testing configuration or real configuration
    print(f'{Back.CYAN}{Fore.WHITE}Extracting{Fore.RED} ESPN {Fore.WHITE}Data')
    file_name = f'{config.output_dir}draft.xlsx'
    league = get_league(config, is_test)
    names, positions, pos_rank, team, projections, status = [], [], [], [], [], []
    # First Create Excel file, with QB data
    # pylint: disable=abstract-class-instantiated
    with pd.ExcelWriter(file_name) as writer:
        print(f'{Fore.BLACK}Processing Position {Fore.WHITE}QB')
        size = 50 if size is None else size
        for player in league.free_agents(position='QB',
                                         size=size):
            names.append(player.name)
            positions.append('QB')
            pos_rank.append(player.posRank)
            team.append(player.proTeam)
            projections.append(player.projected_points)
            status.append(player.injuryStatus)
        data_frame = pd.DataFrame({'name': names,
                                   'position': positions,
                                   'pos_rank': pos_rank,
                                   'team': team,
                                   'projection': projections,
                                   'status': status})
        data_frame.to_excel(writer, sheet_name='QB', index=False)
        names, positions, pos_rank, team, projections, status = [], [], [], [], [], []
    # Loop through remaining positions, and append data into new sheets
    for position in POSITIONS:
        print(f'{Fore.BLACK}Processing Position {Fore.WHITE}{position}')
        position = 'DST' if position == 'D/ST' else position
        # pylint: disable=abstract-class-instantiated
        with pd.ExcelWriter(file_name, mode="a", engine="openpyxl") as writer:
            for player in league.free_agents(position=position,
                                             size=size):
                names.append(player.name)
                positions.append(position)
                pos_rank.append(player.posRank)
                team.append(player.proTeam)
                projections.append(player.projected_points)
                status.append(player.injuryStatus)
            data_frame = pd.DataFrame({'name': names,
                                       'position': positions,
                                       'pos_rank': pos_rank,
                                       'team': team,
                                       'projection': projections,
                                       'status': status})
            data_frame.to_excel(writer, sheet_name=position, index=False)
            names, positions, pos_rank, team, projections, status = [], [], [], [], [], []
    print(f'{Fore.YELLOW}Extraction Complete{Style.RESET_ALL}\n')


def get_league(data, is_test) -> League:
    """ Returns league or test league """
    today = datetime.date.today()
    if is_test:
        return League(league_id=data.league_id, year=today.year)
    return League(league_id=data.league_id, year=today.year,
                  espn_s2=data.s2, swid=data.swid)
