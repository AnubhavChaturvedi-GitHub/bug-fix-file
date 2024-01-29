import asyncio
import threading
import os
import edge_tts    #pip install edge-tts
import pygame      #pip install pygame

# VOICE = "en-AU-WilliamNeural"
VOICE = "en-US-JennyNeural"
BUFFER_SIZE = 1024

def remove_file(file_path):
    max_attempts = 3
    attempts = 0
    while attempts < max_attempts:
        try:
            with open(file_path,'wb'):
                pass
            os.remove(file_path)
            break
        except Exception as e:
            print(f"Error removing file: {e}")
            attempts += 1
async def amain(TEXT,output_file) -> None:
    try:
        communicate = edge_tts.Communicate(TEXT,VOICE)
        await communicate.save(output_file)
        thread = threading.Thread(target=play_audio,args=(output_file,))
        thread.start()
        thread.join()
    except Exception as e:
            print(f"error : {e}")
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
        print(f"Error during audio playback: {e}")


def f2speak(TEXT,output_file=None):
    if output_file is None:
        output_file = f"{os.getcwd()}/speak.mp3"
    asyncio.run(amain(TEXT,output_file))
