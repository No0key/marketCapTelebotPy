import telebot
from telebot.types import Message
import json
import requests




token = 'Enter your token from @BotFather'                       #token for bot
bot = telebot.TeleBot(token)
ticker = 'https://api.coinmarketcap.com/v2/ticker/'
r = requests.get('https://api.coinmarketcap.com/v2/listings')

@bot.message_handler(content_types=['text'])
def user_req(message: Message):
    newReq = str(message.text)                                   #catch user request
    all_coins = json.loads(r.text)                               #get a list of all the coins to check if there is a coin
    for i in all_coins['data']:
         if newReq.upper() == i['symbol']:
             res = marketCall(i['id'])
             bot.reply_to(message, res)
         else:
             pass


def marketCall(req):                                            #function for gettin price of requested coin
    req_coin = requests.get(ticker + str(req))
    one_coin = json.loads(req_coin.text)
    coin = one_coin['data']['name']
    price = one_coin['data']['quotes']['USD']['price']
    change = one_coin['data']['quotes']['USD']['percent_change_24h']
    result = ("Price of " + str(coin) + " = " + str(price) + " and 24 hour % change = " + str(change))
    return (result)



bot.polling()
