""" Run ESPN Fantasy Data Extractor """
import config
from espn_extractor.extract import extract_team_records


if __name__ == '__main__':
    extract_team_records(config.output_file, config.format)
