""" Test Extraction of CSV File """
import os
import csv
from tests.configs import csv_test_config
from espn_extractor.league_history import extract_team_records
from .common_test import CommonTests


class TestCsvExtraction(CommonTests):
    """ Class for CSV Extraction Test """
    config = csv_test_config
    output_file = f'{config.output_dir}/{config.history_file}'

    def setUp(self) -> None:
        if os.path.isfile(self.output_file):
            os.remove(self.output_file)
        extract_team_records(self.config, True)

    def test_csv_extraction(self):
        """ Test if CSV file is created """
        self.assertTrue(os.path.isfile(self.output_file))

    def test_verify_csv_header(self):
        """ Verify the header of CSV test file """
        header = ['owner', 'year', 'team_name', 'win', 'loss', 'draws', 'final_standing',
                  'points_for', 'points_against', 'acquisitions', 'trades', 'drops',
                  'streak_length', 'streak_type', 'playoff_seed']
        with open(self.output_file, encoding="utf8") as file:
            reader = csv.reader(file)
            self.assertEqual(header, next(reader))

    def test_verify_csv_first_row(self):
        """ Verify first line of CSV test file """
        user_date = ['jessie marshall', '2018', 'Team 1', '10', '3', '0', '4', '1276.88',
                     '1038.22', '21', '1', '22', '1', 'WIN', '2']
        with open(self.output_file, encoding="utf8") as file:
            reader = csv.reader(file)
            # Skip Header
            next(reader)
            # When reading, remove trailing white space
            self.assertEqual(user_date, next(reader))
