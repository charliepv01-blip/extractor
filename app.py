import streamlit as st
import re

# Função de Extração de Dados (mantida a sua lógica original)
def extrair_dados(texto):
    """Extrai números, emails e URLs de um bloco de texto."""
    # Usando st.cache_data para cachear resultados e otimizar o desempenho (opcional, mas recomendado)
    
    # \d+
    numeros = re.findall(r'\d+', texto)
    
    # Padrão para emails
    emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', texto)
    
    # Padrão para URLs
    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', texto)
    
    return numeros, emails, urls

# Configuração da Interface Streamlit
def main():
    st.set_page_config(page_title="Análise e Extração de Dados", layout="centered")
    st.title("🔎 Análise e Extração de Dados")
    st.markdown("Insira o texto para extrair automaticamente números, e-mails e URLs.")

    # Equivalente ao tk.Text
    texto_input = st.text_area("Área de Texto", height=200, 
                               placeholder="Cole seu texto aqui, ex: Meu email é teste@exemplo.com e meu telefone é 123456. Acesse o link https://www.google.com.")

    # Equivalente ao tk.Button
    if st.button("Extrair Dados", type="primary"):
        if texto_input:
            # Chama a função de extração
            numeros, emails, urls = extrair_dados(texto_input)
            
            st.subheader("Resultados da Extração:")
            
            # Exibição dos resultados (Substituindo os tk.Label)
            
            # Resultados de Números
            st.markdown("#### 🔢 Números Encontrados:")
            if numeros:
                st.success(', '.join(numeros))
            else:
                st.info("Nenhum número encontrado.")

            # Resultados de Emails
            st.markdown("#### 📧 E-mails Encontrados:")
            if emails:
                # Usamos um conjunto (set) para remover duplicatas e depois voltamos para lista
                st.success(', '.join(sorted(list(set(emails)))))
            else:
                st.info("Nenhum e-mail encontrado.")
            
            # Resultados de URLs
            st.markdown("#### 🔗 URLs Encontradas:")
            if urls:
                # Usamos um conjunto (set) para remover duplicatas e depois voltamos para lista
                st.success('\n\n'.join(sorted(list(set(urls)))))
            else:
                st.info("Nenhuma URL encontrada.")
        else:
            st.warning("Por favor, insira algum texto para extrair os dados.")

if __name__ == "__main__":
    main()
