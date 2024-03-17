from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#.....Chrome
Service_obj = Service("C:\\webdrivers\\chromedriver.exe")
driver = webdriver.Chrome(service=Service_obj)

# Firfox
# Service_obj = Service("C:\\webdrivers\\geckodriver.exe")
# driver = webdriver.Firefox(service=Service_obj)
driver.maximize_window()
filepath = "C:/download.xlsx"
fruit_name = "Apple"
# driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/upload-download-test/index.html")
driver.implicitly_wait(5)
driver.find_element(By.ID,"downloadButton").click()

file_input = driver.find_element(By.CSS_SELECTOR, "input[id=fileinput]")
file_input.send_keys(filepath)
toast_Locator = (By.CSS_SELECTOR,".Toastify__toast-body div:nth-child(2)")
wait = WebDriverWait(driver,5)
wait.until(expected_conditions.visibility_of_element_located(toast_Locator))
print(driver.find_element(*toast_Locator).text)
priceColumn = driver.find_element(By.XPATH,"//div[text()='Price']").get_attribute("data-column-id")
actual_price = driver.find_element(By.XPATH,"//div[contains(text(),'"+fruit_name+"')]/parent::div/parent::div/div[@id='cell-"+priceColumn+"-undefined']").text
# or xpath can be thus      //div[text()='Apple']/parent::div/parent::div/div[@id='cell-4-undefined']

print(actual_price)

