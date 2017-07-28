
import unittest

from mothership.base import MothershipServer
from workers.basic_worker import BasicUserParseWorker


class TestMothershipBasic(unittest.TestCase):

	def test_mothership_initialization(self):
		#test instansiation of mothership
		x = 'data'
		mom = MothershipServer()
		#worker = BasicUserParseWorker("https://www.reddit.com/user/Chrikelnel")
		#worker.send_to_mother(worker,x)

	def test_mothership_thing(self):
		x = 1
		
