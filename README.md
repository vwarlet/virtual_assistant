## Configuração e Utilização

#### Baixar o Pyaudio referente à versão python instalada
https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio

#### Módulos utilizados
- __pyttsx3__: texto para fala
- __speech_recognition__: fala para texto
- __webbrowser__: abrir website no browser
- __wikipedia__: pesquisa no wikipédia (ler resumos, por exemplo)

## Funcionamento

#### Método principal
Rotina do Assistente
Utiliza o módulo _speech_recognition_ para fazer o reconhecimento da fala através do microfone
```
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Ouvindo')
        r.pause_threshold = 0.5     # tempo para considerar o fim da frase
        audio = r.listen(source)
        try:
            print("Processando")
            Query = r.recognize_google(audio, language='pt-BR')
            print("O que eu entendi:", Query)
        except Exception as e:
            print(e)
            print("Não entendi. Repita, por favor")
            return "None"
        return Query
```
#### Método para realizar comandos do Assistente
Método que chama o __takeCommand__ e realiza ações conforme o que for dito
```
def Take_query():
    while(True):
        query = takeCommand().lower()
        if "oi" in query:
            speak("Olá!")
            continue
        elif "desligar" in query:
            speak("Desligando.. até a próxima")
            exit()
        else:
            speak("Desculpe, ainda não reconheço esse comando")
            continue
```
#### Método para fala do Assistente
Inicializa o Assistente, configura a voz e a 'fala e espera'
Utiliza o módulo _pyttsx3_
```
def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()
```