from behave import given, when, then
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time


@given("que o usuário esteja logado no sistema")
def step_login_user(context):

    wait = WebDriverWait(context.browser, 10)
    nav_bar = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "NavigationMenuList")))

    assert nav_bar is not None, "Não está na página de Perfil"


@when("quando clicar em Perfil na navbar")
def step_click_navbar_profile(context):

    wait = WebDriverWait(context.browser, 10)
    actions = ActionChains(context.browser)

    wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "go3958317564")))
    
    perfil_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(@class,'NavigationMenuTrigger')]")))
    actions.move_to_element(perfil_button).perform()

    data_state = perfil_button.get_attribute("data-state")
    if data_state != "open":
        perfil_button.click()


@when("clicar no Logout no drop list")
def step_click_logout_profile(context):
    wait = WebDriverWait(context.browser, 10)
    actions = ActionChains(context.browser)

    logout_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[text()='LogOut']")))

    actions.move_to_element(logout_button).click().perform()


@then("o sistema deverá redirecionar o usuário para a página de login")
def step_redirect_login_page(context):
    wait = WebDriverWait(context.browser, 10)
    button_login = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "sc-eqUAAy")))
    assert "Iniciar sessão" in button_login.text, "Botão não encontrado"
