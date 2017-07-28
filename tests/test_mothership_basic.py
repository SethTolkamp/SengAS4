
import unittest

from mothership.base import MothershipServer


class TestMothershipBasic(unittest.TestCase):

	def test_mothership_initialization(self):

		x = 'data'
		mom = MothershipServer()
		worker = BasicUserParseWorker("https://www.reddit.com/user/Chrikelnel")
		worker.send_to_mother(worker,x,mom)
		#test instansiation of mothership
