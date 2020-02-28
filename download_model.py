from selenium import webdriver
import os
import time

def model_download():
    """
    Function to download model, in pkl format.
    """
    model_url = "https://drive.google.com/uc?export=download&id=105Cz0TpQfLaGshLjVzK3dLY7IZkKZZnd"
    options = webdriver.ChromeOptions()
    prefs = {
        "profile.default_content_settings.popups": 0,
        "download.default_directory": os.getcwd(),
        "directory_upgrade": True
    }
    options.add_experimental_option("prefs", prefs)
    # create webdriver
    driver = webdriver.Chrome(options=options)
    driver.get(model_url)
    
    # click button to download file
    button = driver.find_element_by_id("uc-download-link")
    button.click()
    print("Wait for it...")
    time.sleep(20)
    print("Done! The model, in pkl format, should now be in your current working directory.")
    print("Closing webdriver...")
    driver.quit()
    
if __name__ == "__main__":
    model_download()