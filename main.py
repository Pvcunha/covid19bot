import time, threading
import datetime
from tweet import TwitterHandler
import scrapper

WAIT_SECONDS = 1500


class App():

    def __init__(self):        
        self.posted = {}
        self.posted_time = datetime.date.today()
        self.th = TwitterHandler()

    def heavy_job(self):    
        
        driver = scrapper.open_browser()
        cases = scrapper.get_data(driver)
        print("O postado é:", self.posted )
        print("Os casos são:", cases)
        if(self.posted != cases):
            print('Houve atualizacao no site')
            self.posted = cases.copy()
            text = scrapper.build_text(cases)
            self.th.post(text)

        else:
            print('Não houve alteração')

    def app(self):
        ticker = threading.Event()
        while not ticker.wait(WAIT_SECONDS):
            self.heavy_job()


bot = App()
bot.app()