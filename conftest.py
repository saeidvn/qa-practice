import pytest
from core.browser import get_browser, BrowserType
from config import config

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default=None,
        help="Browser name: chrome, firefox, edge"
    )

@pytest.fixture(scope="function")
def driver(request):
    cli_browser = request.config.getoption("--browser")
    browser_name = (cli_browser if cli_browser else config.BROWSER).upper()

    browser_type = BrowserType[browser_name]
    driver = get_browser(browser_type)
    yield driver
    driver.quit()