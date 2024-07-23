Feature: Logout na página do Joga Junto

    Scenario: Logout no sistema Backoffice
    
    Como usuário logado
    Eu quero deslogar do sistema
    Para manter minha conta segura em minha ausência

    Given que o usuário esteja logado no sistema 
    When quando clicar em Perfil na navbar
    And clicar no Logout no drop list 
    Then o sistema deverá redirecionar o usuário para a página de login