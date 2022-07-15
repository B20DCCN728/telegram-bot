import time
from datetime import datetime

import requests
from bs4 import BeautifulSoup
from telegram import Update
from telegram.ext import *


print("Bot started =)) ĐỊT MẸ MÀY")

#funcion to check user's message
def sample_responses(input_text):
    user_message = input_text

    for res in user_message:
        if res in ("hello", "hi", "chào","chào"):
            return 1
        if res in ("địt","fuck","pusy","dick","lồn","đụ"):
            return 2

#funcion to reply message
def hand_message(update: Update, context: CallbackContext) -> None:
    text = str(update.message.text).lower()
    text = text.split(" ")
    for res in text:
        res.lower()

    responses = sample_responses(text)

    if responses == 1:
        update.message.reply_text("Hello, Fuck you baby <3")
    elif responses == 2 : 
        update.message.




#funcion return time 
def Time(update: Update, context: CallbackContext) -> None:
    now = datetime.now()
    date_time = now.strftime("%d/%m/%y, %H:%M:%S")
    update.message.reply_text(f'{date_time}')




#funcion get data of this web
def Get_News():
    list_news = []
    openweb = requests.get("https://vnexpress.net/the-gioi")

    soup = BeautifulSoup(openweb.text,'html.parser')

    mydivs = soup.find_all("h3", {"class": "title-news"})

    for news in mydivs:
        newdict = {}
        newdict["link"] = news.a.get("href")
        newdict["title"] =  news.a.get("title")
        list_news.append(newdict)
    return list_news



#funcion to get all news in the world of this web 
def News(update: Update, context: CallbackContext) -> None:
    data  = Get_News()
    str_1 = ""
    i = 1
    for res in data:
        str_1 += str(i) + " " + res["title"] + "\n" 
        i += 1 
    update.message.reply_text(f'{str_1}')




#funcion to get news and links in the web     
def New_link(update: Update , context: CallbackContext) ->None:
    data = Get_News()
    str_2 = ""
    i = 1
    for res in data:
        str_2 += str(i) + ". " + res["title"] + "\n" + " Watch new in link: " + res["link"] + "\n"
        i += 1
        if i == 10:
            return update.message.reply_text(f'{str_2}')




def main():
    APY_key = "5107648284:AAFrKRtrMwzBDbM11XXVBcHOSgYnqqdrzgw"
    updater = Updater(APY_key)
    hard = updater.dispatcher
    hard.add_handler(CommandHandler('shortnews', News))
    hard.add_handler(CommandHandler('watchnews', New_link))
    hard.add_handler(CommandHandler('time', Time))
    hard.add_handler(MessageHandler(Filters.text,hand_message))
    updater.start_polling(1) 
    updater.idle()

main()
