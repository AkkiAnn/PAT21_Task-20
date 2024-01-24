from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize webdriver
driver = webdriver.Chrome()

# Maximize browser window
driver.maximize_window()

# Open URL
url = "https://www.cowin.gov.in/"
driver.get(url)

# Click "FAQ" link to open new window
driver.find_element(By.LINK_TEXT, "FAQ").click()

#time delay
time.sleep(4)

# Click "Partners" link to open another new window
driver.find_element(By.XPATH, "//*[@id='navbar']/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[5]/a").click()

#time delay
time.sleep(4)

# Get handles of all open windows
evy_windows = driver.window_handles

# Display window/frame IDs on the console
for window_id in evy_windows:
    driver.switch_to.window(window_id)
    print(f"Window/Frame ID: {window_id}")

# Close two new windows and come back to Home page
for window_id in evy_windows[1:]:
    driver.switch_to.window(window_id)
    driver.close()

# Switch back to main window
driver.switch_to.window(evy_windows[0])

#time delay
time.sleep(4)

# Close main window
driver.quit()


