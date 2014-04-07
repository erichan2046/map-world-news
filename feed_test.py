import unittest
from feed import *
 
class TestFeed(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_from_file(self):
        feed = Feed(file='data/2014-04-05_16-54.atom')
        self.assertEqual(len(feed.articles),89)
        
    def test_duplicate_articles(self):
        feed = Feed(file='data/2014-04-05_16-54.atom')
        feed.add_file('data/2014-04-05_16-54.atom')
        self.assertEqual(len(feed.articles),89)