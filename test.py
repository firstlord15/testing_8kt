import time
import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.extensions.action_helpers import ActionHelpers
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import *

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    appActivity='.Settings',
    language='en',
    locale='US'
)

class TestAppium(unittest.TestCase):    
    def setUp(self) -> None:
        self.driver = webdriver.Remote(
            appium_server_url,
            options=UiAutomator2Options().load_capabilities(capabilities)
        )
        self.action_helpers = ActionHelpers

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()
    
    def exit(self):
        self.action_helpers.swipe(self.driver, 10, 1300, 400, 1300)

    def home(self):
        while(True):
            try:
                self.driver.find_element(AppiumBy.XPATH, home).click()
                break
            except:
                self.exit()

    def shorts(self):
        self.driver.find_element(AppiumBy.XPATH, shorts).click()

    def test_scroll(self):
        self.home()
        el1 = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, el1_uiselector)
        el2 = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, el2_uiselector)
        self.action_helpers.scroll(self.driver, el2, el1)
        
    def test_drag_and_drop(self):
        self.home()
        self.action_helpers.tap(self.driver, [[515, 816]])
        mainScreenView = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, main_screen_view)
        navBar = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, navigationBar)
        self.action_helpers.drag_and_drop(self.driver, mainScreenView, navBar)

    def test_tap(self):
        self.home()
        self.action_helpers.tap(self.driver, [[515, 816]])
        time.sleep(2)
        self.action_helpers.tap(self.driver, [[564, 1161]])
    
    def test_swipe(self):
        self.home()
        self.action_helpers.tap(self.driver, [[515, 816]])
        time.sleep(2)
        self.action_helpers.swipe(self.driver, start_y=742, start_x=18, end_y=742, end_x=500)
        
    
    def test_flick(self):
        self.home()
        self.shorts()
        self.action_helpers.flick(self.driver, 500, 2000, 500, 500);
        self.action_helpers.flick(self.driver, 500, 2000, 500, 500);
        self.action_helpers.flick(self.driver, 500, 2000, 500, 500);
        


        
        
if __name__ == '__main__':
    unittest.main()