import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        # logger = logging.getLogger(__name__)

        # earlier __name__ was used and it returns the file name with path here in this case it is "PytestDemo.BaseClass"
        # But we want the testcase name (basically is method name we called it case test case)
        # from where it is called and in this case it is "test_editProfile" in test_fitureDemo file
        # so we used "loggerName = inspect.stack()[1][3]"

        fileHandler = logging.FileHandler('logfile.log')

        formatter = logging.Formatter("%(asctime)s : %(levelname)s :%(name)s: %(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # Filehandler Object is added as parameter here. Filehandler is basically file location

        logger.setLevel(logging.DEBUG)  # As level is set to INFO so logger will log from info ownwards ..Say if we say DEBUG then it will log from debug
        return logger
    def verifyLinkPresence(self,text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def SelectOptionByText(self,Locator,Text):
        sel = Select(Locator)
        sel.select_by_visible_text(Text)
