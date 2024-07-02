import serial
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

'''
def navigate_to_right_page(driver):
    try:
        # Check if there is a next page button available
        next_page_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".icon-book-next.stripe-btn")))
        
        # If next page button is present, navigate to the next page
        if next_page_button.is_displayed():
            driver.execute_script("arguments[0].scrollIntoView(true);", next_page_button)
            next_page_button.click()
        else:
            print("No next page available.")
    except Exception as e:
        print("Error navigating to the right page:", e)

'''

def navigate_to_right_page(driver):
    try:
        next_page_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".icon-book-next.stripe-btn")))
        driver.execute_script("arguments[0].scrollIntoView(true);", next_page_button)
        next_page_button.click()
    except Exception as e:
        print("Error navigating to the right page:", e)

'''
def navigate_to_left_page(driver):
    try:
        # Check if there is a previous page button available
        prev_page_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".icon-book-prev.stripe-btn")))
        
        # If previous page button is present, navigate to the previous page
        if prev_page_button.is_displayed():
            driver.execute_script("arguments[0].scrollIntoView(true);", prev_page_button)
            prev_page_button.click()
        else:
            print("No previous page available.")
    except Exception as e:
        print("Error navigating to the left page:", e)

'''

def navigate_to_left_page(driver):
    try:
        next_page_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".icon-book-prev.stripe-btn")))
        driver.execute_script("arguments[0].scrollIntoView(true);", next_page_button)
        next_page_button.click()
    except Exception as e:
        print("Error navigating to the left page:", e)

print("Sample test case started")

# Initialize Chrome webdriver
driver = webdriver.Chrome()
driver.maximize_window()

# Open the URL
driver.get("https://online.flippingbook.com/view/478641475/")

# Wait for the page to load
time.sleep(5)

# Initialize serial connection with Arduino
arduino = serial.Serial('COM4', 115200)

while True:
    # Read data from serial port
    data = arduino.readline().strip().decode('utf-8')
    data1 = data  # Assign the value of data directly to data1
    print(data1)
    
    if data1 == '2':
        navigate_to_left_page(driver)
    elif data1 == '1':
        navigate_to_right_page(driver)
    else:
        print("Invalid data received:", data)

# Close the serial connection
arduino.close()

# Close the browser
driver.close()

print("Sample test case successfully completed")
