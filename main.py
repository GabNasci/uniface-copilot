import streamlit as st
import ollama

st.set_page_config(page_title="Chat com DeepSeek", page_icon="🤖", layout="centered")

st.title("💬 Chat com DeepSeek via Ollama")
st.write("Converse com o modelo **DeepSeek** rodando localmente.")

# Área de histórico
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibir histórico
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Campo de entrada
if prompt := st.chat_input("Digite sua mensagem..."):
    # Adicionar mensagem do usuário ao histórico
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Resposta do modelo
    with st.chat_message("assistant"):
        response = ollama.chat(model="deepseek-r1", messages=[
            {"role": "system", "content": "Você é um assistente útil."},
            *st.session_state.messages
        ])
        msg = response['message']['content']
        st.markdown(msg)

    # Adicionar resposta ao histórico
    st.session_state.messages.append({"role": "assistant", "content": msg})
