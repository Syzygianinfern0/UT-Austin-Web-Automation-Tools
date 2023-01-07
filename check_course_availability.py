import json
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# COURSE_URL = "https://utdirect.utexas.edu/apps/registrar/course_schedule/20232/52620/" # testing waitlisted course
COURSE_URL = "https://utdirect.utexas.edu/apps/registrar/course_schedule/20232/17150/"  # testing open course

# read config file
config = json.load(open("config.json"))
eid = config["eid"]
password = config["password"]

# setup driver with local user data directory
# this saves local storage and cookies
# do not share this folder with anyone else
chrome_options = Options()
chrome_options.add_argument("user-data-dir=seleniumdata")
chrome_options.add_argument("headless")  # comment out to see browser (headless better if you wanna automate checking)
driver = webdriver.Chrome(options=chrome_options)

# open random website which requires login
driver.get(COURSE_URL)
time.sleep(2)

# selenium fill form and submit
driver.find_element(By.ID, "username").send_keys(eid)
driver.find_element(By.ID, "password").send_keys(password)
driver.find_element(By.CLASS_NAME, "button").click()

# check if course is waitlisted
time.sleep(2)
status = driver.find_elements(By.TAG_NAME, "td")
waitlisted = status[6].text
if waitlisted == "waitlisted":
    print("Course is wait-listed")
else:
    print("Course is now open!!!")

driver.close()
