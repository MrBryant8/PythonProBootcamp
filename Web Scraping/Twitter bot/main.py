import os
from Bot import InternetSpeedTwitterBot

PROMISED_UP = 10
PROMISED_DOWN = 150
EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")
CHROME_DRIVER_PATH = "CHROME_DRIVER_PATH"


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider(PASSWORD, EMAIL, PROMISED_DOWN, PROMISED_UP)
