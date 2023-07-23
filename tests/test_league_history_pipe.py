""" Test Extraction of Pipe Delimited File """
import os
import csv
import pipe_test_config
from espn_extractor.league_history import extract_team_records
from .common_test import CommonTests


class TestPipeExtraction(CommonTests):
    """ Class for Pipe Delimited Extraction Test """
    config = pipe_test_config
    output_file = f'{config.output_dir}/{config.history_file}'

    def setUp(self) -> None:
        if os.path.isfile(self.output_file):
            os.remove(self.output_file)
        extract_team_records(pipe_test_config, True)

    def test_pipe_extraction(self):
        """ Test if Pipe Delimited file is created """
        self.result_file_exist(self.output_file)

    def test_verify_pipe_header(self):
        """ Verify the header of Pipe Delimited test file """
        header = ['owner', 'year', 'team_name', 'win', 'loss', 'draws', 'final_standing',
                  'points_for', 'points_against', 'acquisitions', 'trades', 'drops',
                  'streak_length', 'streak_type', 'playoff_seed']
        with open(self.output_file, encoding="utf8") as file:
            reader = csv.reader(file, delimiter='|')
            self.assertEqual(header, next(reader))

    def test_verify_pipe_first_row(self):
        """ Verify first line of Pipe Delimited test file """
        user_date = ['jessie marshall|2018|Team 1|10|3|0|4|1276.88|'
                     '1038.22|21|1|22|1|WIN|2']
        with open(self.output_file, encoding="utf8") as file:
            reader = csv.reader(file)
            # Skip Header
            next(reader)
            # When reading, remove trailing white space
            self.assertEqual(user_date, next(reader))
