from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS

import os

# Caminho do seu PDF gigante
pdf_path = "pdfs/documentation.pdf"

# 1. Carregar documento
loader = PyPDFLoader(pdf_path)
documents = loader.load()

print(f"Carregou {len(documents)} páginas.")

# 2. Quebrar texto em chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len
)
chunks = text_splitter.split_documents(documents)

print(f"Quebrou em {len(chunks)} pedaços.")

# 3. Gerar embeddings com Ollama
embeddings = OllamaEmbeddings(model="deepseek-r1")

# 4. Criar e salvar índice FAISS
faiss_index = FAISS.from_documents(chunks, embeddings)

# Salvar índice para carregar depois e não ter que fazer tudo de novo
faiss_index.save_local("vectorstore_faiss")

print("Índice FAISS criado e salvo com sucesso!")
