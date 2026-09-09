import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By



@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.implicitly_wait(3)
    yield browser
    browser.quit()

def test_open_s6(browser):
    browser.get('https://www.demoblaze.com/')
    galaxy_s6 = browser.find_element(By.XPATH, "//a[text()='Samsung galaxy s6']")
    galaxy_s6.click()
    title = browser.find_element(By.CSS_SELECTOR, "h2")
    assert title.text == "Samsung galaxy s6"

def test_monitor_count(browser):
    browser.get('https://www.demoblaze.com/')
    monitor_count = browser.find_element(By.XPATH, "//div[@class='monitor-count']")