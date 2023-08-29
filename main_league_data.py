""" Run ESPN Fantasy Data Extractor """
from espn_extractor.league_history import extract_team_records
import config

if __name__ == '__main__':
    extract_team_records(config, False)
