import time

from selenium import webdriver

driver = webdriver.Chrome('C:\Users\GIGACHAD\PycharmProjects\selenium_with_python\driver\chrome.exe')
url = "http://www.google.com"

driver.get(url)

time.sleep(5)  # Let the user actually see something!

search_box = driver.find_element_by_name('q')

search_box.send_keys('ChromeDriver')

search_box.submit()

time.sleep(5)  # Let the user actually see something!

driver.quit()
