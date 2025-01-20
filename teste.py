from langchain_ollama.llms import OllamaLLM
import whisper

# Passo 1: Transcrever áudio com Whisper
model_whisper = whisper.load_model("base")
audio_file = "audio_unidade7.mp3"  # Substitua pelo nome do seu arquivo de áudio
transcription_result = model_whisper.transcribe(audio_file)
transcription_text = transcription_result['text']
print("Texto transcrito:", transcription_text)

# Passo 2: Configurar modelo Ollama para extração de pontos-chave
ollama_model = OllamaLLM(model="llama3.2:latest")  # Substitua pelo modelo correto se necessário

# Passo 3: Criar prompt para extração de pontos-chave
prompt = f"Extraia os principais pontos do seguinte texto transcrito:\n\n{transcription_text}\n\nResumo:"

# Passo 4: Invocar o modelo com o prompt
response = ollama_model.invoke(prompt)
print("Pontos-chave extraídos:")
print(response)
