from selenium import webdriver
import time

driver = webdriver.Ie("D:\IEDriverServer_x64_3.13.0\IEDriverServer.exe")
driver.get('https://pi.persistent.co.in/SitePages/Pi-Home.aspx')
time.sleep(10)
driver.save_screenshot("D:\Screenshots\pi.png")
print("Screenshot is successfully took.")

driver.quit()