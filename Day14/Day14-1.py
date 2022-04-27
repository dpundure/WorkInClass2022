import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("C:\\Users\\pundudac\\Documents\\chromedriver.exe")

url = "https://www.ss.com/"
driver.get(url)
time.sleep(2)

cars_element = driver.find_element(by=By.ID, value="mtd_97")  # cars category
cars_element.click()
time.sleep(0.5)
bmw = driver.find_element(by=By.LINK_TEXT, value="BMW")
bmw.click()
time.sleep(0.5)
page = driver.find_element(by=By.CLASS_NAME, value="am")

get_links = [x.get_attribute("href") for x in page if x.text != ""]
get_all_links = [x for x in get_links if x.startswith("https://www.ss.com/lv/transport/cars/bmw/")]

with open("all_cars_first_page.txt", "w") as f:
    json.dump(get_all_links, f, indent=2)

