from behave import given, when, then
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from faker import Faker
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given("que o usuário esteja na página de criação de conta")
def step_open_create_acount(context):
    context.browser.find_element(By.CLASS_NAME, "register").click()


@when("o usuário preencher o formulário de criação com dados válidos")
def step_fill_registration_form(context):
    
    wait = WebDriverWait(context.browser, 10)
    wait.until(EC.visibility_of_element_located((By.NAME, "email"))).send_keys(context.user_email)

    wait.until(EC.visibility_of_element_located((By.NAME, "password"))).send_keys(context.password)
    
    wait.until(EC.visibility_of_element_located((By.NAME, "confirmPassword"))).send_keys(context.password)


@when("clicar no botão de criar conta")
def step_click_create_account(context):
    context.browser.find_element(By.XPATH, '//*[@id="root"]/div/form/button').submit()


@then("o sistema deverá exibir uma mensagem de sucesso indicando que a conta foi criada")

def step_verify_account_creation_success_message(context):
    wait = WebDriverWait(context.browser, 10)

    sucess = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "sucess")))
    assert ("Usuário cadastrado com sucesso" in sucess.text), "Erro no cadastro de usuário"
