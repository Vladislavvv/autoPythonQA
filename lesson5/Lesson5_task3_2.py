from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

try:
    count = 0
    chrome.get('http://uitestingplayground.com/dynamicid')
    firefox.get('http://uitestingplayground.com/dynamicid')
# Кликаем на синюю кнопку
    blue_button_c = chrome.find_element(
        "xpath", '//button[text()="Button with Dynamic ID"]').click()
    blue_button_f = firefox.find_element(
        "xpath", '//button[text()="Button with Dynamic ID"]').click()

# Кликаем 3 раза
    for _ in range (3):
        blue_button_c = chrome.find_element(
            "xpath", '//button[text()="Button with Dynamic ID"]')
        blue_button_f = firefox.find_element(
            "xpath", '//button[text()="Button with Dynamic ID"]')
        count = count + 1
        sleep(2)
        print(count)
    
    
except Exception as ex:
    print(ex)
finally:
    chrome.quit()
    firefox.quit()