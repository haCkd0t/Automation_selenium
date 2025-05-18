import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import logging


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--incognito")  # OR use a temp profile dir
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-save-password-bubble")
    prefs = {
        "download.default_directory": 'C:\\Users\\joke\\Downloads',
        "download.prompt_for_download": False,
        "directory_upgrade": True,
        "safebrowsing.enabled": True,
    }
    options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 20)


@pytest.fixture()
def action(driver):
    return ActionChains(driver)


@pytest.fixture(autouse=True)
def setup_logging():
    logger = logging.getLogger('selenium')
    log_path = 'test_logs.log'
    # Avoid adding multiple handlers if fixture runs more than once
    if not logger.handlers:
        handler = logging.FileHandler(log_path)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

    return logger
@pytest.fixture
def mock_driver(mocker):
    driver = mocker.Mock()
    return driver