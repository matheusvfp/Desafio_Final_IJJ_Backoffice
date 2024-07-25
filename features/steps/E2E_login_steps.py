from behave import given, when, then
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given("que o usuário esteja na página de login do Instituto Joga Junto")
def step_open_page(context):

    wait = WebDriverWait(context.browser, 10)
    button_login = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "sc-eqUAAy")))
    assert "Iniciar sessão" in button_login.text, "Botão não encontrado"


@when("inserir as credenciais válidas")
def step_enter_valid_credential(context):

    context.browser.find_element(By.NAME, "email").send_keys(context.user_email)
    context.browser.find_element(By.NAME, "password").send_keys(context.password)


@when("clicar no botão Login")
def step_click_button_login(context):
    context.browser.find_element(By.XPATH, '//*[@id="root"]/main/form/button').submit()


@then("o usuário deverá logar no sistema")
def step_verify_login(context):
    wait = WebDriverWait(context.browser, 10)

    element = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@role='status'][contains(.,'logado com sucesso')]")))
    assert "logado com sucesso" in element.text, "Login não realizado"
