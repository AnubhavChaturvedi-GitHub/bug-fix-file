from Head.Mouth import speak
from Data.dlg_data.dlg import *
import random

def welcome():
    welcome = random.choice(welcomedlg)
    speak(welcome)