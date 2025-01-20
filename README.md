<<<<<<< HEAD
# joaovitor-whisper
Este repositório contém um script Python que utiliza a biblioteca whisper para transcrição de arquivos mp3 para texto. Também possui integração com o ollama para extração de textos chaves por meio do modelo llama3.2.
=======
# Transcrição e Extração de Pontos-chave com Whisper e LangChain Ollama

Este projeto realiza a transcrição de arquivos de áudio utilizando o modelo Whisper e extrai os principais pontos do texto transcrito usando o modelo de linguagem Ollama via LangChain.

## Requisitos

Antes de executar o projeto, certifique-se de ter os seguintes itens instalados:

- **Python 3.8+**  
- **FFmpeg** (necessário para o Whisper)  
  - Linux/macOS:  
    ```bash
    sudo apt update && sudo apt install ffmpeg
    ```
    ou  
    ```bash
    brew install ffmpeg
    ```
  - Windows:  
    Baixe e instale pelo site oficial: [FFmpeg Download](https://ffmpeg.org/download.html)
- **Ollama**  
  1. Instale a Ollama: [ollama.com](https://ollama.com/download)  
  2. Baixe o modelo necessário:  
     ```bash
     ollama pull llama3.2:latest
     ```

### Instalando dependências do projeto

Execute o comando abaixo para instalar todas as bibliotecas necessárias:

```bash
pip install torch torchvision torchaudio whisper langchain langchain_ollama ollama
>>>>>>> 7967d4c (Adicionando arquivos da Unidade 7)
