import os
import csv
from unittest import TestCase
from espn_extractor.extract import extract_team_records


class TestCsvExtraction(TestCase):

    def setUp(self) -> None:
        if os.path.isfile('tests/results/test_csv_file.csv'):
            os.remove('tests/results/test_csv_file.csv')
        extract_team_records('tests/results/test_csv_file.csv', ',', True)

    def test_csv_extraction(self):
        self.assertTrue(os.path.isfile('tests/results/test_csv_file.csv'))

    def test_verify_csv_header(self):
        header = ['owner', 'year', 'team_name', 'win', 'loss', 'draws', 'final_standing', 'points_for',
                  'points_against', 'acquisitions', 'trades', 'drops', 'streak_length', 'streak_type', 'playoff_seed']
        with open('tests/results/test_csv_file.csv', newline='') as f:
            reader = csv.reader(f)
            self.assertEqual(header, next(reader))

    def test_verify_csv_first_row(self):
        user_date = ['jessie marshall', '2018', 'Team 1', '10', '3', '0', '4', '1276.88', '1038.22', '21', '1',
                     '22', '1', 'WIN', '2']
        with open('tests/results/test_csv_file.csv', newline='\n') as f:
            reader = csv.reader(f)
            # Skip Header
            next(reader)
            # When reading, remove trailing white space
            self.assertEqual(user_date, next(reader))
