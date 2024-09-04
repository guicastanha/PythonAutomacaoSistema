# 📂 Sistema de Automação de Cadastro de Usuários

Este projeto é uma automação para a gestão de usuários em um sistema web específico usando Python e Selenium. A automação realiza login no sistema, adiciona um novo usuário e preenche informações essenciais como nome, cargo, e-mail, telefone e senha.

## 🚀 Funcionalidades

- **Login no Sistema**: Automatiza o processo de login no sistema da empresa.
- **Adição de Usuário**: Navega até a página de adição de usuários e preenche todos os campos necessários.
- **Preenchimento de Formulário**: Inclui informações como nome, cargo, e-mail, telefone e senha.

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para a automação.
- **Selenium**: Biblioteca para interação com a web e automação de navegadores.
- **Undetected Chromedriver**: Para evitar detecção de bots.

## 📋 Pré-requisitos

Antes de rodar o script, certifique-se de ter as seguintes ferramentas instaladas:

- [Python](https://www.python.org/downloads/) (3.x)
- [Pip](https://pip.pypa.io/en/stable/installation/) (para instalar pacotes Python)

### 📦 Pacotes Python Necessários

Instale os pacotes necessários usando o `pip`:

```bash
pip install selenium undetected-chromedriver requests
```

# Como Usar e Detalhes do Código

## 🛠️ Como Usar

1. **Configuração**: Substitua as credenciais e informações do usuário conforme necessário no script.

2. **Execução**: Execute o script principal. Certifique-se de que o `chromedriver` esteja corretamente configurado.

    ```bash
    python seu_script.py
    ```

3. **Observação**: O script irá abrir o navegador, realizar o login e adicionar o usuário especificado.

## 🔍 Detalhes do Código

1. **Função `JuntaNome`**

   Constrói um e-mail com base no nome completo do usuário.

2. **Função `get_company_email`**

   Gera um e-mail para a empresa especificada.

3. **Classe `SistemaProOcupacional`**

   - **Método `__init__`**: Inicializa o driver do Chrome e configura as credenciais.
   - **Método `logar_sistema`**: Realiza o login no sistema.
   - **Método `add_usuario_sistema`**: Adiciona um novo usuário no sistema.
   - **Método `finalizar`**: Fecha o navegador após a execução.

## 📜 Notas Adicionais

- Certifique-se de que o `chromedriver` é compatível com a versão do seu navegador Chrome.
- O script inclui um tempo de espera (`sleep`) que pode precisar ser ajustado com base na velocidade da sua conexão e resposta do sistema.

