import asyncio
import threading
import os
import edge_tts    # pip install edge-tts
import pygame      # pip install pygame
import sys
import time
from colorama import Fore,Style,init

init()
# init(autoreset=True)
VOICE = "en-AU-WilliamNeural"
BUFFER_SIZE = 1024

def print_animated_message(message, color=Fore.LIGHTGREEN_EX, speed=0.095):
    for char in message:
        sys.stdout.write(color + char + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(speed)
    print()
def remove_file(file_path):
    max_attempts = 3
    attempts = 0
    while attempts < max_attempts:
        try:
            with open(file_path, 'wb'):
                pass
            os.remove(file_path)
            break
        except Exception as e:
            print(f"Error removing file: {e}")
            attempts += 1

async def amain(TEXT, output_file) -> None:
    try:
        communicate = edge_tts.Communicate(TEXT, VOICE)
        await communicate.save(output_file)
        thread = threading.Thread(target=play_audio, args=(output_file,))
        thread.start()
        thread.join()
    except Exception as e:
        print(f"error: {e}")
    finally:
        remove_file(output_file)

def play_audio(file_path):
    try:
        pygame.init()
        pygame.mixer.init()
        sound = pygame.mixer.Sound(file_path)
        sound.play()

        while pygame.mixer.get_busy():
            pygame.time.Clock().tick(10)

        pygame.quit()

    except Exception as e:
        # Check if the error is related to the inability to connect to the host
        if "Cannot connect to host" in str(e) and "getaddrinfo failed" in str(e):
            print("Internet is not available. Ignoring the error.")
        else:
            # If it's a different error, print the error message
            print(f"Error: {e}")


def speak1(TEXT, output_file=None):
    if output_file is None:
        output_file = os.path.join(os.getcwd(), "speak.mp3")
    asyncio.run(amain(TEXT, output_file))

def speak(text):
    t1 = threading.Thread(target=speak1, args=(text,))
    t2 = threading.Thread(target=print_animated_message, args=(text,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
