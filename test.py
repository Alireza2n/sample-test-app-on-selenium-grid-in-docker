import unittest

from selenium.webdriver import Remote, DesiredCapabilities


class TestSeleniumInDockerAndFirefox(unittest.TestCase):
    def setUp(self):
        self.browser = Remote(
            desired_capabilities=DesiredCapabilities.FIREFOX,
            command_executor="http://172.20.0.2:4444/wd/hub"
        )

    def tearDown(self):
        self.browser.close()

    def test_sample(self):
        self.browser.get('http://sauceclient.readthedocs.io')
        self.assertIn('Selenium', self.browser.page_source)


class TestSeleniumInDockerAndChrome(unittest.TestCase):
    def setUp(self):
        self.browser = Remote(
            desired_capabilities=DesiredCapabilities.CHROME,
            command_executor="http://172.20.0.2:4444/wd/hub"
        )

    def tearDown(self):
        self.browser.close()

    def test_sample(self):
        self.browser.get('http://sauceclient.readthedocs.io')
        self.assertIn('Selenium', self.browser.page_source)
