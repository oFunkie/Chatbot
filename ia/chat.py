from logging.config import stopListening
import re
from time import sleep
from turtle import position
import long_responses as long
import speech_recognition as sr
from win32com.client import Dispatch

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    percentage = float(message_certainty) /float(len(recognised_words))        

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage*100)
    else: 
        return 0

def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Réponses 
    response("Bonjour", ["yo", "salut", "bonjour", "slt", "coucou", "hello"], single_response=True)
    response("ça va bien et toi ?", ["comment", "ça", "va", "tu", "vas", "bien"], single_response=True)  
    response("mdr la blague", ["feur"], required_words=["feur"])        
    response("Merci.", ["joli", "jolie"], single_response=True)
    response("De rien.", ["merci"], single_response=True)
    response("Non. Tu n'es rien pour moi.", ["est-ce", "que", "on", "est", "amis"], single_response=True)
    response(":c", ["ah", "oh", "aie", "ok"], single_response=True)

    response(long.R_EATING, ["tu", "manges", "quoi"], required_words=["manges"])        
    response(long.R_LOVE, ["tu", "aimes", "bien "], required_words=["m'aimes"])  
    response(long.R_DO, ["ça", "tu", "fais", "fait", "quoi"], single_response=True)  
    response(long.R_SQUID_LOVE, ["tu", "aimes", "squid", "game"], required_words=["squid"])  
    response(long.R_NAME, ["tu", "t'appelles", "t appelles", "comment"], required_words=["t'appelles"])  
    response(long.R_BAISE, ["on", "baise"], required_words=["baise"])  
    response(long.R_WHAT, ["tu", "es", "qui"], required_words=["qui"])  
    response(long.R_COLOR, ["quel", "est", "ta", "couleur", "préférée"], required_words=["couleur"])  
    response(long.R_VACANCES, ["vous", "etes", "ou", "en", "vacances"], required_words=["vacances"])  
    response(long.R_VACANCESRES, ["on", "est", "a", "en", "au"], required_words=["on"])  
    response(long.R_OUT, ["tu", "sors", "sort", "dehors"], single_response=True)
    response(long.R_HOUR, ["il", "est", "quelle", "heure"], single_response=True)
    response("super", ["moi", "ça", "va", "je", "vais", "bien"], single_response=True)
    

    # Insulte in long_responses.py
    response(long.R_INSULTE, [long.insultes], single_response=True)

    best_match = max(highest_prob_list, key=highest_prob_list.get)

    return long.unknow() if highest_prob_list[best_match] < 1 else best_match

def get_response(user_input):
    split_message = re.split(r"\s+|[,;?!.-]\s*", user_input.lower())
    response = check_all_messages(split_message)
    return response

while True:
    r  = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language="fr-FR")
        print("Moi: " + text)
    except sr.UnknownValueError:
        print("L'audio n'as pas été compris")
    except sr.RequestError as e:
        print("Le service Google Speech API ne fonctionne plus" + format(e))
    
    try:
        print("Bot: " + Dispatch("SAPI.SpVoice").Speak(get_response(text)))
    except:
        print('\n')
    # print("Bot: " + get_response(text))
    
