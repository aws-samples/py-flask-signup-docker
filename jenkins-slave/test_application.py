import unittest
from selenium import webdriver


class TestSignup(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.PhantomJS()
        self.driver.set_window_size(1120, 550)

    def test_signup(self):
        self.driver.get("http://elb-flask-signup-beta-7177155.us-east-1.elb.amazonaws.com/#signupModal")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
