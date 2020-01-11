# vim: set sw=4 noet ts=4 fileencoding=utf-8:
import sys
sys.path.append('./../subsystems')
from unittest import mock
import unittest


class TestDummy(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass()')

    def setUp(self):
        print('setUp()')

    def test_func(self):
        print('test_func()')

    def tearDown(self):
        print('setUp()')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass()')
