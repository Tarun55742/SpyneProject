import os
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyautogui


@pytest.fixture(params=["chrome", "firefox"])
def browser(request):
    browser_name = request.param
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    yield driver
    driver.quit()

@allure.feature('Navigation')
def test_navigation(browser):
    browser.get('https://www.spyne.ai/image-upscaler')
    browser.maximize_window()
    time.sleep(10)
    assert browser.current_url == 'https://www.spyne.ai/image-upscaler'
    assert browser.find_element(By.XPATH,"//button[text()='Upload an image']").is_displayed()
    assert browser.find_element(By.XPATH, "//button[contains(text(),'Get a Demo')]").is_displayed()


@allure.feature('File Upload')
def test_file_upload(browser):
    browser.get('https://www.spyne.ai/image-upscaler')
    browser.maximize_window()
    time.sleep(10)
    upload_element = browser.find_element(By.XPATH, "//body/div[@id='__next']/div[2]/section[2]/div[1]/div[1]/div[1]/div[2]/button[1]")
    upload_element.click()
    time.sleep(1)
    pyautogui.typewrite(r'C:\Users\tarun\PycharmProjects\SpyneProject\Data\Suit.jpg')  # Replace with your image path
    pyautogui.press('enter')
    time.sleep(10)  # Wait for upload to complete
    # Validate upload success
    assert browser.find_element(By.XPATH, "//body/div[@id='__next']/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]/img[1]").is_displayed()


@allure.feature('Invalid File Upload')
def test_invalid_file_upload(browser):
    browser.get('https://www.spyne.ai/image-upscaler')
    time.sleep(2)
    upload_element = browser.find_element(By.XPATH, "//body/div[@id='__next']/div[2]/section[2]/div[1]/div[1]/div[1]/div[2]/button[1]")
    upload_element.click()
    time.sleep(1)
    pyautogui.typewrite(r'C:\Users\tarun\PycharmProjects\SpyneProject\Data\abc.txt')  # Replace with your image path
    pyautogui.press('enter')
    time.sleep(10)
    process_button = browser.find_element(By.XPATH, "//body/div[@id='__next']/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]/img[1]")
    process_button.is_displayed()
    is_disabled = process_button.get_attribute('disabled')is None
    assert is_disabled, "The Process button is disabled as expected."


@allure.feature('Image Upscaling')
def test_image_upscaling(browser):
    browser.get('https://www.spyne.ai/image-upscaler')
    browser.maximize_window()
    time.sleep(10)
    upload_element = browser.find_element(By.XPATH,
                                          "//body/div[@id='__next']/div[2]/section[2]/div[1]/div[1]/div[1]/div[2]/button[1]")  # Update with actual element ID or selector
    upload_element.click()
    time.sleep(1)
    pyautogui.typewrite(r'C:\Users\tarun\PycharmProjects\SpyneProject\Data\Suit.jpg')  # Replace with your image path
    pyautogui.press('enter')
    time.sleep(10)  # Wait for upload to complete
    # Validate upload success
    assert browser.find_element(By.XPATH,
                                "//body/div[@id='__next']/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]/img[1]").is_displayed()  # Update with actual element ID or selector
    image_process = browser.find_element(By.XPATH,
                                         "//body/div[@id='__next']/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]/img[1]")
    image_process.click()
    time.sleep(5)

@allure.feature('UI Validation')
def test_ui_validation(browser):
    browser.get('https://www.spyne.ai/image-upscaler/result')
    assert browser.find_element(By.XPATH, "//body/div[@id='__next']/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/label[1]/label[1]").is_displayed()   # Upload button
    assert browser.find_element(By.ID, 'preview').is_displayed()  # Image preview
    assert browser.find_element(By.XPATH, "//body/div[@id='__next']/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/button[1]").is_displayed()  # Download button


@allure.feature('Download Functionality')
def test_download_functionality(browser):
    browser.get('https://www.spyne.ai/image-upscaler')
    browser.maximize_window()
    time.sleep(10)
    upload_element = browser.find_element(By.XPATH, "//body/div[@id='__next']/div[2]/section[2]/div[1]/div[1]/div[1]/div[2]/button[1]")  # Update with actual element ID or selector
    upload_element.click()
    time.sleep(1)
    pyautogui.typewrite(r'C:\Users\tarun\PycharmProjects\SpyneProject\Data\Suit.jpg')  # Replace with your image path
    pyautogui.press('enter')
    time.sleep(10)  # Wait for upload to complete
    # Validate upload success
    assert browser.find_element(By.XPATH, "//body/div[@id='__next']/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]/img[1]").is_displayed()  # Update with actual element ID or selector
    image_process = browser.find_element(By.XPATH, "//body/div[@id='__next']/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]/img[1]")
    image_process.click()
    time.sleep(10)
    download_button = browser.find_element(By.XPATH, "//body/div[@id='__next']/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/button[1]")  # Update with actual button ID or selector
    download_button.click()
    time.sleep(5)  # Wait for download to complete
    DOWNLOAD_PATH = 'C:/Users/tarun/Downloads'  # Update the download path here
    downloaded_files = os.listdir(DOWNLOAD_PATH)
    assert len(downloaded_files) > 0, "No files were downloaded"
    print("Downloaded files:", downloaded_files)

    # Optionally, you can verify the file is of the expected type
    downloaded_file = downloaded_files[0]
    assert downloaded_file.endswith('.jpg'), "Downloaded file is not an image"
    print(f"Downloaded file: {downloaded_file}")

