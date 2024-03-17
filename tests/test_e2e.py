import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Utilities.BaseClass import BaseClass
from pageObject.CheckoutPage import CheckoutPage
from pageObject.ConfirmPage import ConfirmPage
from pageObject.HomePage import HomePage


class TestOne(BaseClass):
    def test_e2e(self):
        logs = self.getLogger()
        homePage = HomePage(self.driver)
        checkoutPage = homePage.shopItems()
        logs.info("getting all the card titles")

        productTitles = checkoutPage.getCardTitles()
        for productTitle in productTitles:
            productName = productTitle.find_element(By.XPATH, "div/h4/a").text
            logs.info(productName)
            if productName == "Blackberry":
                productTitle.find_element(By.XPATH, "div/button").click()

        checkoutPage.getcheckoutButton().click()

        confirmPage = checkoutPage.getFinalCheckoutButton()
        logs.info("Entering country name as ind")
        confirmPage.getCountryName().send_keys("Ind")

        self.verifyLinkPresence("India")
        confirmPage.getSelectCountry().click()
        confirmPage.getSelectCheckbox().click()

        confirmPage.getSubmitButton().click()

        successText = confirmPage.getAlertSuccessMessage().text
        logs.info("Text received from application is " + successText)
        assert "Success! Thank you!" in successText

