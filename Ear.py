import speech_recognition as sr   #pip install SpeechRecognition
import os                         # no need to install
import threading                  # no need to install
from mtranslate import translate  #pip install mtranslate
from colorama import Fore,Style,init #pip install colorama

init(autoreset=True) #Automatically reset Style After Each print

def print_loop():
    while True:
        print(Fore.LIGHTGREEN_EX + "I am Listning...",end="",flush=True)
        print(Style.RESET_ALL,end="",flush=True)
        print("",end="",flush=True)

def Trans_hindi_to_english(txt):
    english_txt = translate(txt,"en-in")
    return english_txt

def listen():
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = False
    recognizer.energy_threshold = 35000
    recognizer.dynamic_energy_adjustment_damping = 0.04  # less more active
    recognizer.dynamic_energy_ratio = 1.0
    recognizer.pause_threshold = 0.5
    recognizer.operation_timeout = None
    recognizer.pause_threshold = 0.2
    recognizer.non_speaking_duration = 0.1

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
            print(Fore.LIGHTGREEN_EX + "I am Listning...", end="", flush=True)
            try:
                audio = recognizer.listen(source,timeout=None)
                print("\r"+Fore.LIGHTYELLOW_EX + "Got it , Now Recognizing..",end="",flush=True)
                recognized_txt = recognizer.recognize_google(audio).lower()
                if recognized_txt:
                    translated_txt = Trans_hindi_to_english(recognized_txt)
                    print("\r"+Fore.BLUE + "Mr Zeno : " + translated_txt)
                    return translated_txt
                else:
                    return ""
            except sr.UnknownValueError:
                recognized_txt = ""
            finally:
                print("\r",end="",flush=True)

        os.system("cls" if os.name == "nt" else "clear")
        # threading part
        listen_thread = threading.Thread(target=listen)
        print_thread = threading.Thread(target=print_loop)
        listen_thread.start()
        print_thread.start()
        listen_thread.join()
        print_thread.join()



