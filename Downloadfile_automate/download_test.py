import time
import os
from selenium import webdriver
from download_page import FileDownloadPage
from selenium.webdriver.firefox.options import Options

# Create Firefox profile
firefox_profile = webdriver.FirefoxProfile()

# Set preferences for file download
firefox_profile.set_preference("browser.download.folderList", 2)  # 2 means use custom download directory
firefox_profile.set_preference("browser.download.dir",'C:\\Users\\ACER\\Documents')
firefox_profile.set_preference("browser.download.useDownloadDir", True)
firefox_profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain,application/octet-stream")  # MIME types to auto-download
firefox_profile.set_preference("pdfjs.disabled", True)  # Disable built-in PDF viewer

# Set Firefox options to include the custom profile
options = Options()
options.profile = firefox_profile

# Initialize Firefox WebDriver with the options
driver = webdriver.Firefox(options=options)
driver.maximize_window()

# Navigate to the file download page
driver.get("https://demo.automationtesting.in/FileDownload.html")

# Initialize the page object
file_download_page = FileDownloadPage(driver)

# Perform the actions
file_download_page.enter_text_to_generate_file('Some Data')
time.sleep(2)  # Optional, for demonstration purposes

file_download_page.generate_text_file()
time.sleep(1)  # Optional, for demonstration purposes

file_download_page.download_text_file()
time.sleep(2)

# Sleep for a few seconds to ensure the file is downloaded
time.sleep(5)

# Close the browser
driver.quit()
