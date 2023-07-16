import os
import csv
from unittest import TestCase
from espn_extractor.extract import extract_team_records


class TestPipeExtraction(TestCase):

    def setUp(self) -> None:
        if os.path.isfile('tests/results/test_pipe_file.txt'):
            os.remove('tests/results/test_pipe_file.txt')
        extract_team_records('tests/results/test_pipe_file.txt', '|', True)

    def test_pipe_extraction(self):
        self.assertTrue(os.path.isfile('tests/results/test_pipe_file.txt'))

    def test_verify_pipe_header(self):
        header = ['owner', 'year', 'team_name', 'win', 'loss', 'draws', 'final_standing', 'points_for',
                  'points_against', 'acquisitions', 'trades', 'drops', 'streak_length', 'streak_type', 'playoff_seed']
        with open('tests/results/test_pipe_file.txt', newline='') as f:
            reader = csv.reader(f, delimiter='|')
            self.assertEqual(header, next(reader))

    def test_verify_pipe_first_row(self):
        user_date = ['jessie marshall|2018|Team 1|10|3|0|4|1276.88|1038.22|21|1|22|1|WIN|2']
        with open('tests/results/test_pipe_file.txt', newline='\n') as f:
            reader = csv.reader(f)
            # Skip Header
            next(reader)
            # When reading, remove trailing white space
            self.assertEqual(user_date, next(reader))
