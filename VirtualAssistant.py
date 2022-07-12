import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import random
from utils import *

def takeCommand():

    r = sr.Recognizer()

    # a partir do módulo speech_Recognition
    # utiliza o módulo Microphone para ouvir os comandos
    with sr.Microphone() as source:
        print('Ouvindo')

        # tempo em silêncio para considerar o fim da frase
        r.pause_threshold = 0.5
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

def speak(audio):

    engine = pyttsx3.init()
    # pegar o valor atual da propriedade engine
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    # Método de fala do assistente
    engine.say(audio)

    # Bloqueia enquanto processa os comandos
    engine.runAndWait()

def tellDay():
    day = datetime.datetime.today().weekday() + 1

    Day_dict = {
        1: 'Segunda', 
        2: 'Terça',
        3: 'Quarta', 
        4: 'Quinta',
        5: 'Sexta', 
        6: 'Sábado',
        7: 'Domingo'
    }

    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("Hoje é " + day_of_the_week)

def tellTime():
    time = str(datetime.datetime.now())
    # exemplo do formato exibido: "2020-06-05 17:50:14.582630"
    hour = time[11:13] # algarismos 11 e 12 representam a hora
    min = time[14:16]  # algarismos 14 e 15 representam os minutos
    if min == '00':
        min = format_minutes(min)
    else:
        min = format_minutes(min) + "minutos"
    speak("Agora são" + format_hour(hour) + "horas e" + min)  

def Hello():
    # Função inicial, apresentação do assistente
    speak("Olá, eu sou Assistente Virtual, me diga como posso te ajudar")

def Take_query():
    # Inicia com a saudação
    Hello()

    # Continuar executando até dizer 'tchau' ou 'desligar'
    while(True):
        # deixa o comando em letras minúsculas para melhor resultado
        query = takeCommand().lower()

        if "estou com fome" in query:
            speak("Da uma olhada no ai food")
            webbrowser.open("www.ifood.com.br")
            continue

        elif "pesquisar" in query:
            speak("Abrindo Google ")
            webbrowser.open("www.google.com")
            continue

        elif "que dia é hoje" in query:
            tellDay()
            continue

        elif "que horas são" in query:
            tellTime()
            continue

        elif "wikipédia" in query:
            query = query.replace("Wikipédia", "")
            speak("Checando" + query)
            # da um resumo, lendo alguns techos da wikipedia (sentences)
            wikipedia.set_lang('pt')
            result = wikipedia.summary(query, sentences=1)
            speak("De acordo com wikipedia")
            speak(result)
            continue

        elif "curiosidade" in query:
            speak(random.choice(curiosities()))
            continue

        # comandos para terminar a execução
        elif "desligar" in query or  "sair" in query or "tchau" in query:
            speak("Desligando.. até a próxima")
            exit()

        else:
            speak("Desculpe, ainda não reconheço esse comando")
            continue


if __name__ == '__main__':
    Take_query()