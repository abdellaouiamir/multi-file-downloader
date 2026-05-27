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

def handelDownloadPage(url):
    driver.get(url)
    #wait = WebDriverWait(driver, 10)
    original_window = driver.current_window_handle
    download_button = driver.find_element(By.CLASS_NAME, "link-button.text-5xl.gay-button")
    ActionChains(driver).move_to_element(download_button).click().perform()
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
        
def handelDownloadPage2(url):
    driver.get(url)
    #wait = WebDriverWait(driver, 10)
    time.sleep(20)
    #download_button = WebDriverWait(driver, 20).until(
    #        EC.presence_of_element_located(
    #            (By.XPATH, "//form[@id='downloadForm']/button[@id='method_free']")
    #        )
    #    )
    original_window = driver.current_window_handle
    download_button = driver.find_element(By.XPATH, "//form[@id='downloadForm']/button[@id='method_free']")
    ActionChains(driver).move_to_element(download_button).click().perform()
    time.sleep(60)
    driver.get('chrome://downloads/')
    driver.execute_script("""
        document.querySelector('downloads-manager')
        .shadowRoot.querySelector('#toolbar')
        .shadowRoot.querySelector('#clearAll')
        .click();
    """)
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            driver.close()
    driver.switch_to.window(original_window)
    print("done")
    time.sleep(60)
    download_button = driver.find_element(By.XPATH, "//div[@class='shrink-0 w-full md:w-auto']/button")
    while True:
        time.sleep(10)
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
    
def handelDownloadPage_witanime(url):
    driver.get(url)
    #wait = WebDriverWait(driver, 10)
    original_window = driver.current_window_handle
    download_button = driver.find_element(By.CLASS_NAME, "link-button.text-5xl.gay-button")
    ActionChains(driver).move_to_element(download_button).click().perform()
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

with open("./output.json", "r") as file:
    urls = json.load(fp=file)

count = 0
for url in urls: 
    handelDownloadPage(url)
    count+=1
    print(count)


# Close the browser
driver.quit()