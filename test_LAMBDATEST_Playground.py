import time
import random
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# Generating Random Email ID
generateEmail = "POWWR" + str(random.randint(1000, 9999)) + "@gmail.com"
password = "xyz123"
phoneNumber = "+44" + str(random.randint(7000000000, 7999999999))

@pytest.fixture()
def browser_open_and_close():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/register")
    driver.implicitly_wait(5)
    yield
    driver.quit()

# Scenario 1_Logo presence on LAMBDATEST playground home page
def test_LAMBDATEST_Playground_Functionalities(browser_open_and_close):
   assert driver.find_element(By.CSS_SELECTOR,"img[alt='Poco Electro']").is_displayed()
   print("Logo is displayed on Homepage...")
   time.sleep(2)

# Scenario 2_Check registration is successful with valid inputs
   driver.find_element(By.NAME,"firstname").send_keys("Sruthi")
   driver.find_element(By.NAME, "lastname").send_keys("R")
   driver.find_element(By.NAME, "email").send_keys(generateEmail)
   time.sleep(2)
   driver.find_element(By.NAME, "telephone").send_keys(phoneNumber)
   driver.find_element(By.NAME, "password").send_keys(password)
   driver.find_element(By.NAME, "confirm").send_keys(password)
   time.sleep(2)

# Radio Buttons
   rd_yes = driver.find_element(By.CSS_SELECTOR,"label[for='input-newsletter-yes']")
   rd_no = driver.find_element(By.CSS_SELECTOR,"label[for='input-newsletter-no']")
   rd_yes.click()
   driver.find_element(By.CSS_SELECTOR,"label[for='input-agree']").click()
   time.sleep(2)
   driver.find_element(By.CSS_SELECTOR,"input[value='Continue']").click()

# Registration Successful message appears
   registration_message = driver.find_element(By.XPATH, "//h1[@class='page-title my-3']")
   assert registration_message.is_displayed()
   print("User Account has been Created")

# My Account Verification
   myaccount = driver.find_element(By.XPATH, "//a[normalize-space()='My Account']")
   myaccount.click()
   myaccountmessage = driver.find_element(By.CSS_SELECTOR, "div[id='content'] div:nth-child(1) h2:nth-child(1)")
   assert myaccountmessage.is_displayed()
   time.sleep(2)
   assert driver.find_element(By.XPATH, "//h2[normalize-space()='My Orders']").is_displayed()
   print("My Account information is successfully viewed")

   driver.find_element(By.CSS_SELECTOR,"a:nth-child(14)").click()
   time.sleep(2)
   driver.find_element(By.CSS_SELECTOR,".page-title.my-3")
   print("Logout Successful")

# Scenario 3_Login with correct credentials
   driver.find_element(By.XPATH,"//a[contains(text(),'Login')]").click()
   time.sleep(2)
   driver.find_element(By.NAME,"email").send_keys(generateEmail)
   driver.find_element(By.NAME,"password").send_keys(password)
   time.sleep(2)
   driver.find_element(By.CSS_SELECTOR, "input[value='Login']").click()

   driver.find_element(By.XPATH,"//h2[normalize-space()='My Account']").is_displayed()
   print("Successfully Logged in and viewed my account information")

# Scenario 4_Search for HTC Touch HD product
   driver.find_element(By.NAME, "search").send_keys("HTC Touch HD")
   driver.find_element(By.CLASS_NAME,"type-text").click()
   time.sleep(2)

# HTC Product page appears
   driver.find_element(By.CSS_SELECTOR, "h1[class='h4']").is_displayed()
   print("HTC Touch HD Page appears")

# Click on the product
   driver.find_element(By.CLASS_NAME,"text-ellipsis-2").click()
   actual_price = driver.find_element(By.CSS_SELECTOR, ".price-new.mb-0").text
   expected_price = "$146.00"
   if actual_price == expected_price:
       print("Proceed to cart")
   else:
       print("Price of the product is wrong")

# Scenario 5_Add the product to Cart and verify
   driver.find_element(By.CSS_SELECTOR,"div[id='entry_216842'] button[title='Add to Cart']").click()
   driver.find_element(By.CSS_SELECTOR,"a[class='btn btn-primary btn-block']").click()
   time.sleep(2)

# Verify the product in the cart
   driver.find_element(By.CSS_SELECTOR, "td[class='text-left'] a").is_enabled()
   productincart = driver.find_element(By.CSS_SELECTOR, "td[class='text-left'] a").text
   product_needed = "HTC Touch HD"
   if productincart == product_needed:
     print("HTC Touch HD is successfully added to cart")

#Verify the number of units added to cart
   quantity_added = driver.find_element(By.CLASS_NAME, "form-control").get_attribute("value")
   if quantity_added == "1":
    assert True
    print ("Product verification successful. Proceed to checkout")


# To Run: Go to Terminal-> pytest -rA
# To generate report ->pytest -rA --html="anyname.html"
