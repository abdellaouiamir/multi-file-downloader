from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import json


# Path to your Brave executable
brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

# Set up Chrome options and specify Brave as the binary
options = Options()
options.binary_location = brave_path    # Point to Brave brower
# options.add_argument('--headless')      # Optional: Run brower in headless mode

download_dir = r"C:\Users\Amir\Downloads"
# options for download a file
options.add_experimental_option("prefs", {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,          # Disable "Save As" pop-up
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True                   # Optional for security
})

# Create a Service object
# service = Service()

# Create a WebDriver instance
driver = webdriver.Chrome(options = options)

actions = ActionChains(driver)

# Target website
website = "https://fitgirl-repacks.site/marvels-spider-man-2/"
#driver.get(website)
# Use the driver to open a website
#driver.get(website)

def check_download():
    # Get the downloads directory path (works for most operating systems)
    downloads_dir = os.path.expanduser('~/Downloads')
    test_files = [f for f in os.listdir(downloads_dir) if f.endswith('.crdownload')]
    if test_files:
        return True
    else:
        return False
    
def handelDownloadPage_witanime(url):
    driver.get(url)
    #wait = WebDriverWait(driver, 10)
    original_window = driver.current_window_handle
    download_button = driver.find_elements(By.CLASS_NAME, "col-lg-3.col-md-3.col-sm-12.col-xs-12.col-no-padding.col-mobile-no-padding.DivEpisodeContainer")
    i = 0
    while i < len(download_button):
        ActionChains(driver).move_to_element(download_button[i]).click().perform()
        workupload_button = driver.find_element(By.XPATH,"//li[normalize-space(text())='الجودة الخارقة FHD']/following-sibling::li//span[text()='workupload']/..")
        workupload_button.click()
        time.sleep(10)
        exit()
        if check_download():
            while check_download():
                time.sleep(10)
            i += 1
        
    exit()
    #download_button.click()
    while True:
        time.sleep(5)
        if not check_download():
            #driver.close()
            #actions.key_down(Keys.CONTROL).send_keys('w').perform()
            #driver.switch_to.window(driver.window_handles[0])
            for window_handle in driver.window_handles:
                if window_handle != original_window:
                    driver.switch_to.window(window_handle)
                    driver.close()
            driver.switch_to.window(original_window)
            download_button.click()
        else:
            while check_download():
                time.sleep(10)
            return
    return
    WebDriverWait(driver=driver, timeout=10).until(EC.number_of_windows_to_be(2))
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_name=window_handle)
            break

urls = []

handelDownloadPage_witanime("https://witanime.you/anime/spy-x-family-season-2/")


# Close the browser
driver.quit()