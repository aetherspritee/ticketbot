from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.keys import Keys

service = Service(executable_path="/usr/bin/chromedriver")

# TODO: get correct url, make sure approach works for multiple sites
driver = webdriver.Chrome()
driver.get("https://www.eventim.de/artist/eisbaeren-berlin/")
elements = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.NAME, "searchterm")))
button = driver.find_element(By.CLASS_NAME, "btn.btn-primary.theme-btn.btn-sm.btn-block.visible-lg.visible-sm.visible-md")
button.send_keys(Keys.RETURN)
elements = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.NAME, "searchterm")))
seats = driver.find_element(By.CLASS_NAME, "seat-switch.u-shadow.js-tab-switch.js-tracking.standard-gray-shadow.theme-content-bg.theme-text-color.theme-alt-interaction-color.cro-active.active")
seats.send_keys(Keys.RETURN)

# TODO: find correct ticket

# TODO: handle actual purchase

# driver.quit()
