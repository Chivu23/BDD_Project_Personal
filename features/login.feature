Feature: Check the functionality of login page
  # scenariu 1 : user ok pass ok
  # scenariu 2 : user ok pass not ok
  # scenariu 3 : user not ok pass ok
  # scenariu 4 : user ok pass none
  # scenariu 5 : user none pass ok
  # scenariu 6 : user none pss none
  # scenariu 7 : user not ok pass none
  # scenariu 8 : user none pass not ok
  # scenariu 9 : user not ok pass not ok
  # scenariu 10: user block pass ok
  Background:
    Given I am on the saucedemo login page

  Scenario: Success login when pass and user are ok
    When I insert the correct username and correct pass
    And I click the login button
    Then I can login into the app and see the list of products


  Scenario: Check login funct when user is valid but pass is invalid
    When I insert the correct user and incorrect pass
    And I click the login button
    Then I can't login into the app and receive error Epic sadface: Username and password do not match any user in this service


  Scenario: Check login functionality when user is incorrect, but the pass is valid
    When I insert the incorrect username and correct password
    And I click the login button
    Then I can't login into the app and receive error Epic sadface: Username and password do not match any user in this service


  Scenario: Check login funct when user is correct and pass is none
    When I insert the correct username and none pass
    And I click the login button
    Then I can't login into the app and receive error Epic sadface: Password is required

  @invalid_login5
  Scenario: Check login funct when user is none and pass is ok
    When I insert username none and pass valid
    And I click the login button
    Then I can't login into the app and receive error Epic sadface: Username is required

  @invalid_login6
  Scenario: Check login funct when username is none and pass is none
    When I click the login button
    Then I can't login into the app and receive error Epic sadface: Username is required

  @invalid_login7
  Scenario: Check login funct when username is incorrect and pass is none
    When I insert incorrect username and none password
    And  I click the login button
    Then I cannot login into the application and receive error message:Epic sadface: Password is required

  @invalid_login8
  Scenario: Check login func when username is none and pass is incorrect
    When I insert none username and incorrect pass
    And I click the login button
    Then I cannot login into the application and receive error message:Epic sadface: Username is required


  @invalid_login9
  Scenario: Check login func when username is incorrect and pass si incorrect
    When I insert username and password incorrect
    And I click the login button
    Then I cannot login into the application and receive error message:Epic sadface: Username and password do not match any user in this service

  @invalid_login10
  Scenario: Check login func when username in block and pass is correct
    When I insert a block username and correct pass
    And I click the login button
    Then I cannot login into the application and receive error message:Epic sadface: Sorry, this user has been locked out.


