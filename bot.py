from tweet import TwitterHandler
from scrapper import get_data

text = get_data()
bot = TwitterHandler()
bot.post(text)
