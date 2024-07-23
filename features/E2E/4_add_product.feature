Feature: Cadastro de produto na Loja IJJ

    Scenario: Cadastro de produtos no sistema Backoffice

    Como usuário logado do sistema IJJ
    Eu quero cadastrar novos produtos
    Para que eles fiquem disponíveis para venda na loja

    Given que o usuário está na página de cadastro de produtos
    When o usuário clica no botão "Adicionar"
    And preenche o formulário com os dados do produto
    Then o usuário clica no botão "Enviar" para registrar o novo produto
    And o sistema deve exibir uma mensagem de sucesso indicando que o produto foi cadastrado com sucesso
