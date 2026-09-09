from enum import Enum
from selenium import webdriver

class BrowserType(Enum):
    CHROME = "chrome"
    FIREFOX = "firefox"
    EDGE = "edge"

def get_browser(browser_type: BrowserType):
    if browser_type == BrowserType.CHROME:
        return webdriver.Chrome()
    elif browser_type == BrowserType.FIREFOX:
        return webdriver.Firefox()
    elif browser_type == BrowserType.EDGE:
        return webdriver.Edge()
    else:
        raise ValueError(f"Browser '{browser_type}' is not supported")