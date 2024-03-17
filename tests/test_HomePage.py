import pytest
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from Utilities.BaseClass import BaseClass
from pageObject.HomePage import HomePage


class TestHomePage(BaseClass):

    def test_formSubmission(self,getdata):
        logs = self.getLogger()
        homePage = HomePage(self.driver)

        logs.info("First Name is" + getdata["firstname"])
        homePage.getName().send_keys(getdata["firstname"])
        homePage.getEmail().send_keys(getdata["lastname"])
        homePage.getCheckBox().click()
        self.SelectOptionByText(homePage.getGender(),getdata["gender"])
        homePage.getSubmit().click()

        alertText = homePage.getSuccessMessage().text

        assert ("Success" in alertText)
        alertText1 = homePage.getSuccessMessage().text

        self.driver.refresh()

    # @pytest.fixture(params=[("Rahul","Shetty","Male"),("Anushika","Shetty","Female")])  # Now this way is not used as data is
    # called from seperate Test Data python package file like HomePageDate and test_HomoPageDate is variable there

    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getdata(self, request):
        return request.param

    @pytest.fixture1(params=HomePageData.getTestData("Testcase2"))
    def getdata(self, request):
        return request.param

