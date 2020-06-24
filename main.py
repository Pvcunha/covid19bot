import time, threading
from tweet import TwitterHandler
from scrapper import get_data

WAIT_SECONDS = 180


def heavy_job():    
    text = get_data()
    bot = TwitterHandler()
    bot.post(text)

def main():
    ticker = threading.Event()
    while not ticker.wait(WAIT_SECONDS):
        heavy_job()

if __name__ == "__main__":
    main()