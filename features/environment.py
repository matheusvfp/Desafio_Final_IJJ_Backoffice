from selenium.webdriver import Firefox
from faker import Faker


def before_all(context):
    fake = Faker()
    
    context.browser = Firefox()
    context.browser.get("https://projetofinal.jogajuntoinstituto.org/")
    
    context.user_email = fake.free_email()
    context.password = fake.password()
    


def after_all(context):
    context.browser.quit()
