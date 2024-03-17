from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    countryName = (By.ID, "country")
    selectCountry = (By.LINK_TEXT,"India")
    checkBox = (By.XPATH,"//label[@for='checkbox2']")
    submitButton = (By.CSS_SELECTOR, "[type='submit']")
    alertSuccessMessage = (By.CLASS_NAME, "alert-success")


    def getCountryName(self):
        return self.driver.find_element(*ConfirmPage.countryName)

    def getSelectCountry(self):
        return self.driver.find_element(*ConfirmPage.selectCountry)

    def getSelectCheckbox(self):
        return self.driver.find_element(*ConfirmPage.checkBox)

    def getSubmitButton(self):
        return self.driver.find_element(*ConfirmPage.submitButton)

    def getAlertSuccessMessage(self):
        return self.driver.find_element(*ConfirmPage.alertSuccessMessage)