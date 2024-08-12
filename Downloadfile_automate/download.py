
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the WebDriver (Firefox in this case)
driver = webdriver.Firefox()
driver.maximize_window()

# Navigate to the file download page
driver.get("https://demo.automationtesting.in/FileDownload.html")

# Create a WebDriverWait object
wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds

# Enter data to generate a text file
text_area = wait.until(EC.presence_of_element_located((By.ID, 'textbox')))
text_area.send_keys('Some Data')
time.sleep(2)

# Click the generate file button to generate the text file
generate_button = wait.until(EC.element_to_be_clickable((By.ID, 'createTxt')))
generate_button.click()
time.sleep(2)

# Click the download button after it becomes clickable
download_link = wait.until(EC.element_to_be_clickable((By.ID, 'link-to-download')))
download_link.click()

# Sleep for a few seconds to ensure the file is downloaded
time.sleep(5)

# Close the browser
driver.quit()
