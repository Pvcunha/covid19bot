import time, threading
from tweet import TwitterHandler
from scrapper import build_text

WAIT_SECONDS = 180


def heavy_job():    
    text = build_text()
    print(text)
    #bot = TwitterHandler()
    #bot.post(text)

def teste():
    print("testando")

ticker = threading.Event()
while not ticker.wait(WAIT_SECONDS):
    heavy_job()
