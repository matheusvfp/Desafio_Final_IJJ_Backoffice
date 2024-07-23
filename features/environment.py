from selenium.webdriver import Firefox

def before_all(context):
    context.browser = Firefox()
    context.browser.get('https://projetofinal.jogajuntoinstituto.org/')

def after_all(context):
    context.browser.quit()
    
