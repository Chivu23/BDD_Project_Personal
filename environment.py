from browser import Browser
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


def before_all(context):
    """
    definim toate instructiunile pe care le executam
    inaintea rularii tuturor pasilor
    """
    context.browser = Browser()
    context.login_page = LoginPage()
    context.products_page = ProductsPage()


def after_all(context):
    """
    def toate instructiunile care trb exectuate
    dupa rualrea tuturor pasilor
    """
    context.browser.close()
