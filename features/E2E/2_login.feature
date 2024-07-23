Feature: Login na página do Joga Junto
    
    Scenario: Login no sistema Backoffice 

    Como usuário credenciado do Instituto Joga Junto
    Eu quero acessar o sistema Backoffice
    Para realizar minhas atividades rotineiras

    Given que o usuário esteja na página de login do Instituto Joga Junto
    When inserir as credenciais válidas
    And clicar no botão Login 
    Then o usuário deverá logar no sistema

