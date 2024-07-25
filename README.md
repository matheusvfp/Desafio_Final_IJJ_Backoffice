# Backoffice JogaJunto 
<img src="https://github.com/matheusvfp/Squad1-IJJ/assets/65199677/3782a146-deb0-43eb-847d-6099ba7f506d" alt="Image 1" style="width: 213px; height: auto;">
<img src="https://github.com/matheusvfp/Squad1-IJJ/assets/65199677/1770a178-1d2a-434a-b12a-3ea2b3079e22" alt="Image 2" style="width: 300px; height: auto;">
<div align="center">
  <picture>
    
  </picture>
</div>
<br>

O sistema de controle de estoque do Instituto Joga Junto visa proporcionar uma experiência intuitiva para os colaboradores. O objetivo é organizar os produtos de forma lógica e acessível, facilitando tanto o cadastro de novos colaboradores quanto o gerenciamento de produtos.

Este repositório conta com a suíte de **testes automatizados** para o Backoffice JogaJunto.

# Arquitetura
Os testes automatizados foram desenvolvidos utilizando `Python`, `Selenium Webdriver` e `Behave`.<br>
A utilização do Behave nos permite que os casos de testes estejam em Gherkin

## Testes E2E
Foram desenvolvidos testes automatizados das seguintes funcionalidades do sistema 
 - Criação de Usuário
 - Login
 - Logout
 - Cadastro de Produto



# Executando o projeto
Abaixo, um passo-a-passo de como executar os testes localmente.

## Pré-requisitos 📋
- [Python 3.x](https://www.python.org/downloads/) (Eu utilizei a versão `3.11.2` enquanto desenvolvia esse projeto).
- WebDriver do seu navegador (veja mais abaixo).

## WebDrivers
Para executar os testes você precisa instalar a versão do webdriver para o seu navegador.
- [ChromeDriver](https://chromedriver.chromium.org/downloads) for Google Chrome
- [Geckodriver](https://github.com/mozilla/geckodriver/releases/latest) for Firefox.
  
ChromeDriver e geckodriver devem estar presentes no [system path](https://en.wikipedia.org/wiki/PATH_(variable)).

## Virtual Environment 🌲
É recomendado a utilização de um ambiente virtual para a instalação de dependencias. <br>
Dentro da pasta do backoffice-jogajunto execute `python -m venv venv` para criar um ambiente virtual:
```bash
python -m venv venv
```

### Ative o ambiente virtual:

- Windows

```bash
venv\Scripts\activate
```
- Linux/MacOs
  
```bash
venv/bin/activate
```

## Instalação 🏗️
Instale todos os requisitos:
```bash
pip install -r requirements.txt
```

## Configs ⚙️
As configurações como **navegador** e **endpoints** da aplicação podem ser configuradas dentro do arquivo `behave.ini`

Os navegadores suportados são, ambos também no modo `headless`:
- Firefox
- Chrome

Lembrando que é necessário o `webdriver` do navegador escolhido, como citado nos **Pré-requisitos**

##  Rodadando os testes ✔️
Para executar os testes, basta utilizar o comando `behave`

```bash
behave
```

## Apoie o projeto 🙌

Se você quiser apoiar o projeto, deixe uma ⭐.

## QA Avengers 🚀
<img></img>
Desenvolvido pela Squad QA Avengers durante o módulo avançado do curso **Bugou? QA TA ON** do [Instituto Joga Junto](https://www.jogajuntoinstituto.org/)


___
Made with ❤️ by QA Avengers da Automação. <br>
