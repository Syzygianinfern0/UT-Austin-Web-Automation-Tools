import json
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# read config file
config = json.load(open("config.json"))
eid = config["eid"]
password = config["password"]

# setup driver with local user data directory
# this saves local storage and cookies
# do not share this folder with anyone else
chrome_options = Options()
chrome_options.add_argument("user-data-dir=seleniumdata")
driver = webdriver.Chrome(options=chrome_options)

# open random website which requires login
driver.get("https://utdirect.utexas.edu/utdirect/index.WBX")
time.sleep(2)

# selenium fill form and submit
driver.find_element(By.ID, "username").send_keys(eid)
driver.find_element(By.ID, "password").send_keys(password)
driver.find_element(By.CLASS_NAME, "button").click()
