
import unittest

from mothership.base import MothershipServer


class TestMothershipBasic(unittest.TestCase):

	def test_mothership_initialization(self):

		mom = MothershipServer()
		#test instansiation of mothership
