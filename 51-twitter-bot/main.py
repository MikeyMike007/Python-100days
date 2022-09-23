# Following program determines download and upload speeds and if they are below a certain threshold,
# A tweet is sent to internetprovider

from internetspeedtwitterbot import InternetSpeedTwitterBot

PROMISED_DOWN = 1000
PROMISED_UP = 1000
PROVIDER = "@YOUR_INTERNET_PROVIDER"

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()

if float(bot.down) < PROMISED_DOWN or float(bot.up) < PROMISED_UP:
    message = f" \
    {PROVIDER} please increase my internet speed!\n \
    You promised me {PROMISED_UP} Mbps upward and {PROMISED_DOWN} Mbps down\n \
    I currently have {bot.up} Mbs upward and {bot.down} downward"

    print(message)

    bot.login()
    bot.tweet(message)
