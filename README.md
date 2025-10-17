# Extrator

# 🔎 Extrator de Dados WebApp

Um aplicativo web simples e rápido, construído com Python e Streamlit, para extrair automaticamente números, endereços de e-mail e URLs de qualquer bloco de texto inserido.

Este projeto migra a funcionalidade original de uma aplicação desktop Tkinter para um ambiente web, com deploy contínuo via Vercel e GitHub.

## ✨ Funcionalidades

* **Extração de Números:** Identifica sequências de dígitos.
* **Extração de E-mails:** Localiza padrões de e-mail válidos (ex: `usuario@dominio.com`).
* **Extração de URLs:** Encontra links que começam com `http://` ou `https://`.
* **Interface Amigável:** Utiliza Streamlit para uma experiência de usuário limpa e intuitiva.

## 🛠️ Tecnologias Utilizadas

* **Python**
* **Streamlit:** Para a construção da interface web.
* **`re` (Regex):** Para o poderoso processamento de padrões de texto.
* **Vercel:** Plataforma de deploy.
* **GitHub:** Controle de versão e integração de deploy contínuo.

## 🚀 Como Executar Localmente

Siga estas etapas para executar o aplicativo na sua máquina local.

### Pré-requisitos

Certifique-se de ter o Python (3.9+) instalado.

### Instalação

1.  **Clone o Repositório:**
    ```bash
    git clone [https://github.com/SEU-USUARIO/nome-do-seu-repositorio.git](https://github.com/SEU-USUARIO/nome-do-seu-repositorio.git)
    cd nome-do-seu-repositorio
    ```

2.  **Crie e Ative um Ambiente Virtual (Recomendado):**
    ```bash
    python -m venv venv
    # No Windows
    .\venv\Scripts\activate
    # No macOS/Linux
    source venv/bin/activate
    ```

3.  **Instale as Dependências:**
    ```bash
    pip install -r requirements.txt
    ```

### Execução

Basta rodar o script Streamlit:

```bash
streamlit run app.py
