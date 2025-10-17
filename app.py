import streamlit as st
import re

# Função de Extração com Regex AVANÇADO
def extrair_dados(texto):
    """Extrai telefones (no lugar de números genéricos), e-mails e URLs."""
    
    # NOVAS EXPRESSÕES REGULARES AVANÇADAS:
    
    # 1. Telefones Brasileiros (DDD opcional, 8/9 dígitos, com/sem separadores)
    # Ex: (11) 98765-4321, 9876-5432, 11987654321
    telefones = re.findall(
        r'(?:\(?\d{2}\)?\s?)?(?:9\d{4}|\d{4})[-\s]?\d{4}', 
        texto
    )
    
    # 2. E-mails (Padrão robusto)
    emails = re.findall(
        r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', 
        texto
    )
    
    # 3. URLs/Links (HTTP/HTTPS opcional, WWW opcional)
    # Ex: google.com, https://blog.streamlit.io/caminho
    urls = re.findall(
        r'(?:https?://)?(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/\S*)?', 
        texto
    )
    
    # --- Formatação dos Resultados (para visualização e download) ---
    
    output_text = "--- Resultados da Extração Avançada ---\n\n"
    
    output_text += f"Total de TELEFONES Encontrados: {len(telefones)}\n"
    output_text += "TELEFONES ENCONTRADOS:\n"
    output_text += "\n".join(telefones) + "\n\n"
    
    output_text += f"Total de E-mails Encontrados: {len(emails)}\n"
    output_text += "E-MAILS ENCONTRADOS:\n"
    output_text += "\n".join(emails) + "\n\n"
    
    output_text += f"Total de URLs Encontradas: {len(urls)}\n"
    output_text += "URLS ENCONTRADAS:\n"
    output_text += "\n".join(urls)
    
    return output_text, telefones, emails, urls

# ----------------------------------------------------
# APLICATIVO STREAMLIT
# ----------------------------------------------------

st.title("🔎 Extrator de Dados WebApp")
st.markdown("Cole o texto abaixo para extrair números, e-mails e URLs.")

# Área de entrada de texto
input_text = st.text_area("Cole seu texto aqui:", height=300)

# Botão para iniciar a extração
if st.button("Extrair Dados"):
    if input_text:
        # Chama a função de extração
        downloadable_data, n, e, u = extrair_dados(input_text)
        
        # Exibe os resultados na tela (opcional, mas bom para visualização)
        st.subheader("Resultados da Extração")
        
        st.success(f"Extração Concluída! {len(n)} números, {len(e)} e-mails, {len(u)} URLs.")

        # Exibe a string formatada no Streamlit (opcional)
        st.code(downloadable_data, language='text')

        # ----------------------------------------------------
        # BOTAO DE DOWNLOAD (A SOLUÇÃO)
        # ----------------------------------------------------
        st.markdown("---")
        
        # O st.download_button PRECISA da string de dados e do nome do arquivo
        st.download_button(
            label="💾 Baixar Dados Extraídos (.txt)",
            data=downloadable_data,
            file_name="dados_extraidos.txt",
            mime="text/plain" # Tipo de arquivo de texto simples
        )
        # ----------------------------------------------------

    else:
        st.warning("Por favor, cole algum texto para iniciar a extração.")
