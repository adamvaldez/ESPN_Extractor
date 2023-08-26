""" Common reusable test """
import os
from unittest import TestCase


class CommonTests(TestCase):
    """ Class for Common test functions """
    def result_file_exist(self, file):
        """ Test if file is created """
        self.assertTrue(os.path.isfile(file))
