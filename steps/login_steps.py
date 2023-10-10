from behave import *


@given("I am on the saucedemo login page")
def step_impl(context):
    context.login_page.navigate_to_login_page()


@when("I insert the correct username and correct pass")
def step_impl(context):
    context.login_page.insert_correct_username()
    context.login_page.insert_correct_password()


@when("I click the login button")
def step_impl(context):
    context.login_page.click_login_button()


@then("I can login into the app and see the list of products")
def step_impls(context):
    # trebuie sa apelam met chec current url
    # disponibila in clasa prod page
    context.products_page.check_current_url()


@when("I insert the correct user and incorrect pass")
def step_impl(context):
    context.login_page.insert_correct_username()
    context.login_page.insert_incorrect_password()


@when("I insert the incorrect username and correct password")
def step_impl(context):
    context.login_page.insert_incorrect_username()
    context.login_page.insert_correct_password()


@when("I insert the correct username and none password")
def step_impl(context):
    context.login_page.insert_correct_username()


@when('I insert none username and valid password')
def step_impl(context):
    context.login_page.insert_correct_password()


@then('I cannot login into the application and receive error message:Epic sadface: Username is required')
def step_impl(context):
    context.login_page.check_error_msg_no_username()


@when("I insert incorrect username and none password")
def step_impl(context):
    context.login_page.insert_incorrect_username()


@then("I cannot login into the application and receive error message:Epic sadface: Password is required")
def step_impl(context):
    context.login_page.check_error_msg_no_pass()


@when("I insert none username and incorrect pass")
def step_impl(context):
    context.login_page.insert_incorrect_password()


@when("I insert username and password incorrect")
def step_impl(context):
    context.login_page.insert_incorrect_username()
    context.login_page.insert_incorrect_password()


@when("I insert a block username and correct pass")
def step_impl(context):
    context.login_page.insert_blocked_username()
    context.login_page.insert_correct_password()


@then("I cannot login into the application and receive error message:Epic sadface: Sorry, this user has been locked out.")
def step_impl(context):
    context.login_page.check_msg_blocked_user()


'''  
    
@when("I can't login into the app and receive error Epic sadface: Username and password do not match any user in this service")
def step_impl(context):
    context.login_page.check_error_message_invalid_pwd()


# @when("I can't login into the app and receive error Epic sadface: Username and password do not match any user in this service")
# def step_impl(context):
#     context.login_page.check_error_message_invalid_username()


@when("I can't login into the app and I receive error Epic sadface: Password is required")
def step_impl(context):
    context.login_page.check_error_message_none_password()


# @when("I can't login into the app and I receive error Epic sadface: Username is required")
# def step_impl(context):
#     context.login_page.

@then("I can't login into the app and receive error Epic sadface: Username is required")
def step_impl(context):
    context.login_page.check_error_msg_no_username()
    
'''

