Feature: Criação de usuário na página do Instituto

    Scenario: criar um usuário
    
    Como usuário da plataforma do Joga Junto
    Eu quero criar uma conta
    Para conseguir acessar ao sistema

    Given que o usuário esteja na página de criação de conta
    When o usuário preencher o formulário de criação com dados válidos
    And clicar no botão de criar conta
    Then o sistema deverá exibir uma mensagem de sucesso indicando que a conta foi criada