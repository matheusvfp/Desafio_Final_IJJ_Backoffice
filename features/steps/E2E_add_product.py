from behave import given, when, then
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from faker import Faker
import random
import os


@given("que o usuário está na página de cadastro de produtos")
def step_page_register_product(context):


    context.browser.find_element(By.NAME, "email").send_keys(context.user_email)
    context.browser.find_element(By.NAME, "password").send_keys(context.password)

    context.browser.find_element(By.XPATH, '//*[@id="root"]/main/form/button').submit()


@when('o usuário clica no botão "Adicionar"')
def step_click_add_button(context):
    wait = WebDriverWait(context.browser, 10)

    wait.until(EC.visibility_of_element_located((By.XPATH, '//button[normalize-space(text())="Adicionar"]'))).click()


@when("preenche o formulário com os dados do produto")
def step_add_data_product(context):
    fake = Faker()
    wait = WebDriverWait(context.browser, 10)

    product_name = fake.name()
    product_description = fake.text()
    value = fake.random_number(digits=2)
    formatted_value = f"{value},00"

    file_path = os.path.abspath(os.path.join('media', 'p1.png'))
    
    categories = ["Roupas", "Calçados", "Acessórios"]
    category = random.choice(categories)
    

    context.browser.find_element(By.NAME, "name").send_keys(product_name)
    context.browser.find_element(By.NAME, "description").send_keys(product_description)
    wait.until(EC.visibility_of_element_located((By.XPATH, f"//label[contains(.,'{category}')]"))).click()
    context.browser.find_element(By.NAME, "price").send_keys(formatted_value)
    context.browser.find_element(By.NAME, "shipment").send_keys(formatted_value)

    file_input = context.browser.find_element(By.NAME, "image")
    file_input.send_keys(file_path)


@then('o usuário clica no botão "Enviar" para registrar o novo produto')
def step_click_register_product(context):
    wait = WebDriverWait(context.browser, 10)

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".sc-feUZmu > button:nth-child(8)"))).click()


@then("o sistema deve exibir uma mensagem de sucesso indicando que o produto foi cadastrado com sucesso")
def step_sucess_mensage(context):
    wait = WebDriverWait(context.browser, 10)

    element = wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@role='status'][contains(.,'Produto enviado com sucesso!!')]",)))

    assert ("Produto enviado com sucesso!!" in element.text), "Erro no cadastro do produto"
