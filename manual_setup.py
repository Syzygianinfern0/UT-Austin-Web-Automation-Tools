import json
import time

from selenium import webdriver

# create webdriver with local storage
# local_storage = json.loads(local_storage)
# options = webdriver.ChromeOptions()
# options.set_local_storage(local_storage)
# driver = webdriver.Chrome(chrome_options=options)
driver = webdriver.Chrome()

# open url
driver.get("https://utdirect.utexas.edu/apps/registrar/course_schedule/20232/52620/")

# wait for redirect
time.sleep(2)

# set local storage
local_storage = open("local_storage.json").read()
for key, value in json.loads(local_storage).items():
    driver.execute_script(f"window.localStorage.setItem('{key}', '{value}');")

# load website cookies
cookies = open("cookies.json").read()
for cookie in json.loads(cookies):
    try:
        driver.add_cookie(cookie)
    except AssertionError as e:
        print(e)

print("done")
# dummy
input("Press enter to continue...")

# close the browser
driver.close()
