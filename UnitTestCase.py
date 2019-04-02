# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class abc(unittest.TestCase):
    def setup(self):
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_abc(self):
        self.driver = webdriver.Ie("D:\IEDriverServer_x64_3.13.0\IEDriverServer")
        self.driver.get("https://www.google.com/")
        assert "Google" in self.driver.title
        print("Google Title is present")
        elem = self.driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys("fifa2018")
        elem.send_keys(Keys.RETURN)
        self.driver.find_element_by_partial_link_text("2018 FIFA World Cup - Wikipedia").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:self.accept_next_alert = True
    
    def teardown(self):
        self.driver.close()
        self.assertEqual([], self.verificationErrors)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

