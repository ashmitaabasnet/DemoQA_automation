from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox() #Initializes a new Firefox browser session
driver.maximize_window()
driver.get("https://demoqa.com/automation-practice-form")

# Set up an explicit wait
wait = WebDriverWait(driver, 10)

# Fill in the First Name and Last Name
wait.until(EC.element_to_be_clickable((By.ID, "firstName"))).send_keys("Ashmita")
wait.until(EC.element_to_be_clickable((By.ID, "lastName"))).send_keys("Basnet")

# Fill in the Email
wait.until(EC.element_to_be_clickable((By.ID, "userEmail"))).send_keys("basnet@gmail.com")

# Select Gender
wait.until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Female']"))).click()

# Fill in the Mobile Number
wait.until(EC.element_to_be_clickable((By.ID, "userNumber"))).send_keys("9810000000")

# Select Date of Birth
dob = wait.until(EC.element_to_be_clickable((By.ID, "dateOfBirthInput")))
dob.click()
time.sleep(1)  # Wait for the date picker to load
Select(wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "react-datepicker__month-select")))).select_by_visible_text("February")
Select(wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "react-datepicker__year-select")))).select_by_visible_text("2002")
wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='react-datepicker__day react-datepicker__day--014']"))).click()

# Fill in the Subjects
subjects = wait.until(EC.element_to_be_clickable((By.ID, "subjectsInput")))
subjects.send_keys("Computer Science")
subjects.send_keys(Keys.RETURN)

# Scroll to the hobbies section to ensure it's in view
hobbies_label = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="hobbiesWrapper"]/div[2]/div[2]/label')))
driver.execute_script("arguments[0].scrollIntoView(true);", hobbies_label)
driver.execute_script("arguments[0].click();", hobbies_label)

# Upload Picture
wait.until(EC.presence_of_element_located((By.ID, "uploadPicture"))).send_keys("C:\\Users\\ACER\\Pictures\\Screenshots\\pic01.png")

# Fill in Current Address
wait.until(EC.element_to_be_clickable((By.ID, "currentAddress"))).send_keys("Kapan, Chabahil, Kathmandu")

# Select State
state = wait.until(EC.element_to_be_clickable((By.ID, "react-select-3-input")))
state.send_keys("NCR")
state.send_keys(Keys.RETURN)

# Select City
city = wait.until(EC.element_to_be_clickable((By.ID, "react-select-4-input")))
city.send_keys("Delhi")
city.send_keys(Keys.RETURN)

# Submit the form
submit_button = wait.until(EC.element_to_be_clickable((By.ID, "submit")))
driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
submit_button.click()

# Pause to view the result
time.sleep(10)

# Close the browser
driver.quit()
