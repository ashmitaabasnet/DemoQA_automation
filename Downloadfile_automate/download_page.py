from locators import FileDownloadLocators

class FileDownloadPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_text_to_generate_file(self, text):
        text_area = self.driver.find_element(*FileDownloadLocators.TEXTBOX)
        text_area.clear()
        text_area.send_keys(text)

    def generate_text_file(self):
        generate_button = self.driver.find_element(*FileDownloadLocators.CREATE_TXT_BUTTON)
        generate_button.click()

    def download_text_file(self):
        download_link = self.driver.find_element(*FileDownloadLocators.DOWNLOAD_LINK)
        download_link.click()
