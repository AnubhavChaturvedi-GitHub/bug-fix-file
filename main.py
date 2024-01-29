import random
from Head.Ear import *
from Traning_Model.model import mind
from Function.wish import wish
from Function.welcome import welcome
from Data.dlg_data.dlg import *
from Head.Mouth import speak
from Automations.open import open
from Automations.close import close
from Function.check_online_ofline import is_online
from friday.Fspeak import fspeak


def jarvis():
    wish()
    while True:
        text = listen().lower()
        if text in wake_key_word:
            welcome()
        elif text in bye_key_word:
            res_random = random.choice(res_bye)
            speak(res_random)
            break
        elif text.startswith(("jarvis","buddy","jar")):
            text = text.replace("jarvis","")
            text = text.replace("vis","")
            text = text.replace("buddy","")
            text = text.replace("jar","")
            text = text.strip()
            text = mind(text)
            speak(text)
        elif text.endswith(("jarvis","buddy","jar"," jarvis"," buddy"," jar")):
            text = text.replace("jarvis","")
            text = text.replace("vis","")
            text = text.replace("buddy","")
            text = text.replace("jar","")
            text = text.strip()
            text = mind(text)
            speak(text)
        elif text.startswith(("open","kholo","show me")):
            text = text.replace("kholo", "")
            text = text.replace("show me", "")
            text = text.strip()
            open(text)
        elif text in open_input :
            text = text.replace("big", "")
            text = text.replace("khologe", "")
            text = text.replace("kholo", "")
            text = text.strip()
            open(text)

        elif text in close_input:
            close()

        else:
            pass





def check_jarvis():
    if is_online():
        x = random.choice(online_dlg)
        fspeak(x)
        jarvis()
    else:
        x = random.choice(ofline_dlg)
        fspeak(x)


check_jarvis()
