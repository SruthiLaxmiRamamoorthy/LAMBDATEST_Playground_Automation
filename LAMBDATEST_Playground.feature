Feature: LAMBDATEST_Playground functionalities testing

  Scenario 1:Logo presence on LAMBDATEST playground home page
    Given launch chrome browser
    When open LAMBDATEST Playground home page
    Then verify that the logo present on home page

  Scenario 2: Check registration is successful with valid inputs
    Given User is on registration page
    And enter valid First Name and Last Name
    And enter valid inputs
    When all inputs are correct
    And click on continue
    Then User must successfully view the My Account page
    And click on logout

  Scenario 3: Login with correct credentials
    Given User is on login page
    When User enters valid E-mail address and password
    And click on login button
    Then User should successfully login and view the My Account page

  Scenario 4: Search for HTC Touch HD product
    Given User is on home page
    When User enters HTC TOUCH HD product into the search box field
    And click on search button
    Then HTC Touch HD product page should display

  Scenario 5:Add the product to Cart and verify
    Given User is on product page
    Then verify the price of the product
    And click on add to cart button
    Then verify the quantity and product name in the Cart
    And close the browser








