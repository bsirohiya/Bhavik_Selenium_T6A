import pytest
from seleniumbase import Driver
from config.env import ConfigReader

@pytest.fixture(scope="session")
def setup_and_teardown():

    config = ConfigReader.read_config()
    env = config['qa']
    base_url = env['base_url']

    driver = Driver(
        uc=True,
        headed=True
    )

    driver.maximize_window()
    driver.get(base_url)

    yield driver
    input("Enter to close window...")  # Wait for user input before closing the window
    driver.quit()