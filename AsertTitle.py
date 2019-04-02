from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Ie("D:\IEDriverServer_x64_3.13.0\IEDriverServer.exe")
driver.get("https://www.google.com")
assert "Google" in driver.title
print("Google Title is present")
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("fifa2018")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
