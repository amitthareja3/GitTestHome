from selenium.webdriver.common.by import By

from pageObject.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    productTitles = (By.XPATH, "//div[@class='card h-100']")
    checkoutLink = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    finalCheckout = (By.CSS_SELECTOR, "button[class*='btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.productTitles)

    def getcheckoutButton(self):
        return self.driver.find_element(*CheckoutPage.checkoutLink)

    def getFinalCheckoutButton(self):
        # return self.driver.find_element(*CheckoutPage.finalCheckout)

        self.driver.find_element(*CheckoutPage.finalCheckout).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage


