import pytest
import time
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup")
class Test_RadioButtonDemo:

    """ Locators"""
    Radito_Button_Male_Locator = (By.XPATH, "//body/div/div/div/div/div/label[contains(text(),'Male')]/input[1]")
    Radio_Button_Female_Locator = (By.XPATH, "//body/div/div/div/div/div/label[contains(text(),'Female')]/input[1]")


    def test_radiobuttons01(self):
        print('test radio button test case 01')
        print('is Female radio button selected : ', self.driver.find_element(*self.Radio_Button_Female_Locator).is_selected())
        self.driver.find_element(*self.Radio_Button_Female_Locator).click()
        print('is Female radio button selected : ', self.driver.find_element(*self.Radio_Button_Female_Locator).is_selected())
        time.sleep(5)

    def test_radiobutton02(self):
        print('test radio button test case 02')
        print('is Male Radio button selected :', self.driver.find_element(*self.Radito_Button_Male_Locator).is_selected())
        self.driver.find_element(*self.Radito_Button_Male_Locator).click()
        print('is Male Radio button selected :',self.driver.find_element(*self.Radito_Button_Male_Locator).is_selected())
        time.sleep(5)






