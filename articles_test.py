import unittest
from models import articles

articles = articles.Articles


class ArticlesTest (unittest.TestCase):
    """
    Test class to test behaviour of the articles class
    """

    def setUp(self):
        """
        Method to run before every Test
        """
        self.new_article = Articles(
            "abc-news", "ABC News", "http://abcnews.go.com")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Articles))


if __name__ == '__main__':
    unittest.main()
