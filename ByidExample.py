from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Ie("D:\IEDriverServer_x64_3.13.0\IEDriverServer.exe")
driver.get("https://www.google.com/")
# assert "Google" in driver.title
print("Title Present")
elem = driver.find_element_by_id("lst-ib")
elem.send_keys("India")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()


