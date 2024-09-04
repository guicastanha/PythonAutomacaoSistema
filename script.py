import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
import requests


# Função para construir o email com base no nome completo
def JuntaNome(nome):
    PartesNome = nome.split()
    juntaNome1 = PartesNome[0]
    juntaNome2 = PartesNome[-1]
    EmailNome = juntaNome1 + "." + juntaNome2
    return EmailNome


def get_company_email(company_name, nome_completo):
    empresas = ["proocupacional", "cedusp", "prezecor"]

    if company_name in empresas:
        email_nome = JuntaNome(nome_completo)
        email = f"{email_nome}@{company_name}.com.br"
        return email
    else:
        return None


class SistemaProOcupacional:
    def init(self, email, senha):
        self.email = email
        self.senha = senha
        self.driver = uc.Chrome()
        self.nome = "Leandro rassum Neto"

    def logar_sistema(self):
        self.driver.get("https://sistema.proocupacional.com.br/")  # Define o URL para pesquisa
        self.driver.maximize_window()  # Maximiza a tela

        # Espera até que o campo de email esteja presente
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/form/div[2]/div/input")))

        # Preenchendo o formulário de login
        self.driver.find_element(By.XPATH, "/html/body/div[2]/form/div[2]/div/input").send_keys(self.email)
        self.driver.find_element(By.XPATH, "/html/body/div[2]/form/div[3]/div/input").send_keys(self.senha)
        self.driver.find_element(By.XPATH, "/html/body/div[2]/form/div[4]/button").click()
        # Espera até que a próxima página ou elemento esteja presente
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='menuUsuario']/a"))
        )
        print("Usuário logado no sistema")

    def add_usuario_sistema(self):
        # Navega para a gestão de usuários
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='menuUsuario']/a"))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="submenuUsuario"]/a'))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="button-add"]'))
        ).click()

        print("Página de adição de usuário aberta")

        nome_completo = "jeremias da silva souza"  # Aqui você deve usar o nome do usuário que deseja criar

        # Preenche o campo Nome e pressiona Enter
        nome_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="Nome"]'))
        )
        print("Colocou o nome")
        # Ensure the field is visible and interactable
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="Nome"]'))
        )
        print("Seleciona Nome")
        nome_field.send_keys(nome_completo)

        # Preenche o campo Cargo
        time.sleep(2.0)
        cargo_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="Cargo"]'))
        )
        print("Entrou no cargo")
        # Ensure the field is visible and interactable
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="Cargo"]'))
        )

        # Click on the field to activate dropdown/autocomplete
        cargo_field.click()
        cargo_field.send_keys("Auxiliar de enfermagem")
        print("Chegou no nome do cargo")

        time.sleep(0.3)

        # Preenche o campo Email
        company_name = "proocupacional"  # Substitua pelo nome da empresa conforme a resposta da API

        email_empresa = get_company_email(company_name, nome_completo)
        if email_empresa:
            email_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="Email"]'))
            )
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="Email"]'))
            )
            email_field.send_keys(email_empresa)
            print("Email preenchido")
            time.sleep(0.3)

        # Preenche o campo Telefone
        telefone_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="Telefone"]'))
        )
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="Telefone"]'))
        )
        telefone_field.send_keys("(11) 98765-4321")
        print("Telefone preenchido")
        time.sleep(0.3)

        # Preenche o campo Senha
        senha_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="Senha"]'))
        )
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="Senha"]'))
        )
        senha_field.send_keys("teste123")
        print("Senha preenchida")
        time.sleep(0.3)

        # Preenche o campo Confirmar Senha
        confirmar_senha_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="ConfirmarSenha"]'))
        )
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="ConfirmarSenha"]'))
        )
        confirmar_senha_field.send_keys("teste123")
        print("Confirmação de senha preenchida")

        time.sleep(333333)

    def finalizar(self):
        self.driver.quit()
        print("Finalizado")
        time.sleep(3333)


def main():
    # Credenciais para entrar no sistema da PRO
    email_sistema_pro = "arthur.massimetti@proocupacional.com.br"
    senha_sistema_pro = "teste123"

    sistema_pro = SistemaProOcupacional(email_sistema_pro, senha_sistema_pro)
    sistema_pro.logar_sistema()
    sistema_pro.add_usuario_sistema()
    sistema_pro.finalizar()


if name == "main":
    main()
    print("aqui main")
