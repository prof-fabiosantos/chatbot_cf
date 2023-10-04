import streamlit as st
from gradio_client import Client

# Título da aplicação Streamlit
st.title("Chatbot da Constituição Federal do Brasil")

# Criar um campo de entrada de texto para a pergunta
question = st.text_input("Digite sua pergunta:")

# Botão para fazer a previsão
if st.button("Enviar"):
    # Criar uma instância do cliente Gradio
    client = Client("FabioSantos/chatbot_cf", hf_token="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")
    
    # Fazer uma previsão com a pergunta inserida
    result = client.predict(question, api_name="/predict")
    
    # Exibir a resposta
    st.write("Resposta do Chatbot:")
    st.write(result)

# Nota explicativa
st.markdown("*Certifique-se de que o modelo Gradio e o servidor estejam em execução antes de usar esta interface.*")
