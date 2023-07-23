""" Test Extraction of CSV File """
import os
import csv
from unittest import TestCase
import pytest
import csv_test_config
from espn_extractor.draft_board import extract_draft_board


@pytest.mark.skip(reason="Test League cannot load Free Agent Data")
class TestDraftBoardCSV(TestCase):
    """ Class for CSV Extraction Test """
    config = csv_test_config
    output_file = f'{config.output_dir}/{config.draft_file}'

    def setUp(self) -> None:
        if os.path.isfile(self.output_file):
            os.remove(self.output_file)
        extract_draft_board(csv_test_config, True)

    def test_csv_extraction(self):
        """ Test if CSV file is created """
        self.assertTrue(os.path.isfile(self.output_file))

    def test_verify_csv_header(self):
        """ Verify the header of CSV test file """

        header = ['name', 'position', 'projection']
        with open(self.output_file, newline='', encoding="utf8") as file:
            reader = csv.reader(file)
            self.assertEqual(header, next(reader))

    def test_verify_csv_first_row(self):
        """ Verify first line of CSV test file """
        user_date = ['Patrick Mahomes', 'QB', 455.76]
        with open(self.output_file, newline='\n', encoding="utf8") as file:
            reader = csv.reader(file)
            # Skip Header
            next(reader)
            # When reading, remove trailing white space
            self.assertEqual(user_date, next(reader))
