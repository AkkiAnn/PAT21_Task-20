from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import requests
import time

# Set path to ChromeDriver executable
serv_obj=Service(r"C:\Drivers_Selenium\chromedriver-win64\chromedriver.exe")

# Create new instance of Chrome driver
driver = webdriver.Chrome(service=serv_obj)

# Maximize the browser window
driver.maximize_window()

# ActionChains
actions = ActionChains(driver)

# Navigate the Labour Ministry website
driver.get("https://labour.gov.in/")

driver.implicitly_wait(60)

#Close the Ad Banner:
driver.find_element(By.CLASS_NAME, "open_button").click()

# Download monthly progress report, select and click
time.sleep(2)
element_to_hover_over = driver.find_element(By.XPATH, '//*[@id="nav"]/li[7]/a')  # DOCUMENT XPATH
time.sleep(2)
actions.move_to_element(element_to_hover_over)
time.sleep(2)
actions.perform()
driver.find_element(By.LINK_TEXT, "Monthly Progress Report").click()

time.sleep(2)
pdf=(driver.find_element(By.XPATH, '//*[@id="fontSize"]/div/div/div[3]/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[2]/div[2]/table/tbody/tr[2]/td[2]/a').click())

time.sleep(4)
alert=driver.switch_to.alert
alert.accept()

driver.implicitly_wait(20)

#time delay
time.sleep(6)

# Get handles of all open windows
window_handles = driver.window_handles

# Display window/frame IDs in the console
for handle in window_handles:
    driver.switch_to.window(handle)
# Close the two new windows and switch back to original window
for handle in window_handles[1:]:
    driver.switch_to.window(handle)
    driver.close()

# Switch back to original window
driver.switch_to.window(window_handles[0])

#time delay
time.sleep(6)

# Download 10 photos from the "Photos Gallery" under the "Media" menu
driver.find_element(By.LINK_TEXT, "Media").click()

# time delay
time.sleep(10)

driver.implicitly_wait(20)

# Manually enter the swachhata-hi-seva PAGE. (Not able to access the element)
driver.get('https://labour.gov.in/gallery/swachhata-hi-seva')

# Wait for photos to load
photos = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="quicktabs-tabpage-album_gallery-0"]/div/div[2]/div/ul/li[1]/div[1]/div/a/img'))) #Photo Gallery

# Create folder to store downloaded photos
folder_path = 'downloaded_photos'
os.makedirs(folder_path, exist_ok=True)

# Download the first 10 photos (Got only single src in one X-PATH)
for i, photo in enumerate(photos[:10]):
    photo_url = photo.get_attribute('src')
    response = requests.get(photo_url)
    with open(os.path.join(folder_path, f'photo_{i+1}.jpg'), 'wb') as f:
        f.write(response.content)

#time delay
time.sleep(3)

# Close browser
driver.close()