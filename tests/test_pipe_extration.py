""" Test Extraction of Pipe Delimited File """
import os
import csv
from unittest import TestCase
from espn_extractor.extract import extract_team_records


class TestPipeExtraction(TestCase):
    """ Class for Pipe Delimited Extraction Test """
    def setUp(self) -> None:
        if os.path.isfile('tests/results/test_pipe_file.txt'):
            os.remove('tests/results/test_pipe_file.txt')
        extract_team_records('tests/results/test_pipe_file.txt', '|', True)

    def test_pipe_extraction(self):
        """ Test if Pipe Delimited file is created """
        self.assertTrue(os.path.isfile('tests/results/test_pipe_file.txt'))

    def test_verify_pipe_header(self):
        """ Verify the header of Pipe Delimited test file """
        header = ['owner', 'year', 'team_name', 'win', 'loss', 'draws', 'final_standing',
                  'points_for', 'points_against', 'acquisitions', 'trades', 'drops',
                  'streak_length', 'streak_type', 'playoff_seed']
        with open('tests/results/test_pipe_file.txt', newline='', encoding="utf8") as file:
            reader = csv.reader(file, delimiter='|')
            self.assertEqual(header, next(reader))

    def test_verify_pipe_first_row(self):
        """ Verify first line of Pipe Delimited test file """
        user_date = ['jessie marshall|2018|Team 1|10|3|0|4|1276.88|'
                     '1038.22|21|1|22|1|WIN|2']
        with open('tests/results/test_pipe_file.txt', newline='\n', encoding="utf8") as file:
            reader = csv.reader(file)
            # Skip Header
            next(reader)
            # When reading, remove trailing white space
            self.assertEqual(user_date, next(reader))
