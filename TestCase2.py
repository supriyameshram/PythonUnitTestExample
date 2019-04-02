import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Ie("D:\IEDriverServer_x64_3.13.0\IEDriverServer.exe")

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.guru99.com/")
        # self.assertIn("guru99", driver.title)
        elem = driver.find_element_by_id("search")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()