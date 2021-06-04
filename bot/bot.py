from keyboards import start_keyboard, only_search_keyboard, continue_keyboard, choice_keyboard
import requests
from time import sleep
import json
import os
import numpy as np
import matplotlib.dates as mdates
from main.randomPatternRecognizer import raw_graph, pattern_recognizer, pattern_storage, current_pattern

TOKEN = ""
similarity_percentage = 50
date, bid, ask = np.recfromtxt('GBPUSD1d.txt', unpack=True,
                    delimiter=',', converters={0: lambda x: mdates.datestr2num(x.decode('utf8'))})
length_of_data = int(bid.shape[0])
all_data = ((bid + ask) / 2)
average_line = ((bid + ask) / 2)
to_what = 37000

class BotHandler:

    def __init__(self, token):
        self.token = token
        self.api_url = f"https://api.telegram.org/bot{token}/"
        self.last_update_id = 0

    def get_updates(self, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout}
        response = requests.get(self.api_url + method, params)
        result_json = response.json()['result']
        return result_json

    def get_last_update(self):
        try:

            data = self.get_updates()
            last_update = data[-1]
            current_update_id = last_update['update_id']
            if self.last_update_id != current_update_id:
                self.last_update_id = current_update_id
                if "message" in last_update:
                    message_data = last_update['message']
                    chat_id = message_data['chat']['id']
                    message_text = message_data['text']
                    chat_name = message_data['chat']['first_name']
                    message = {'message': {'chat_id': chat_id,
                                           'text': message_text, 'chat_name': chat_name}}
                    return message

                elif "callback_query" in last_update:
                    callback_message_data = last_update['callback_query']
                    callback_query_id = callback_message_data['id']
                    chat_id = callback_message_data['message']['chat']['id']
                    callback_data = callback_message_data['data']
                    chat_name = callback_message_data['message']['chat']['first_name']
                    message_id = callback_message_data['message']['message_id']
                    message = {'callback_query': {'callback_query_id': callback_query_id, 'data': callback_data,
                                                  'chat_id': chat_id, 'chat_name': chat_name, 'message_id': message_id}}

                    return message
                else:
                    return None
        except Exception as err:
            print(err)

    def send_message(self, chat_id, text, parse_mode=None, reply=None):
        if reply is None:
            pass
        else:
            reply = json.dumps(reply)
        params = {'chat_id': chat_id, 'text': text,
                  'parse_mode': parse_mode, 'reply_markup': reply}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def send_photo(self, chat_id, photo, caption=None, parse_mode=None, reply=None):
        if reply is None:
            pass
        else:
            reply = json.dumps(reply)
        files = {'photo': open(photo, 'rb')}
        params = {'chat_id': chat_id, 'caption': caption,
                  'parse_mode': parse_mode, "reply_markup": reply}
        method = 'sendPhoto'
        resp = requests.post(self.api_url+method, files=files, data=params)
        return resp

    def edit_message_caption(self, chat_id, message_id, caption, parse_mode=None, reply=None):
        if reply is None:
            pass
        else:
            reply = json.dumps(reply)
        params = {'chat_id': chat_id, 'message_id': message_id,
                  'caption': caption, 'parse_mode': parse_mode, 'reply_markup': reply}
        method = 'editMessageCaption'
        resp = requests.post(self.api_url + method, params)
        return resp

    def edit_message_reply_markup(self, chat_id, message_id, reply):
        if reply is None:
            pass
        else:
            reply = json.dumps(reply)
        params = {'chat_id': chat_id,
                  'message_id': message_id, 'reply_markup': reply}
        method = 'editMessageReplyMarkup'
        resp = requests.post(self.api_url + method, params)
        return resp


bot = BotHandler(TOKEN)


def plot_decorator(chat_id, reply_markup, caption=None):
    def inner(func):
        def send_plot(*args):
            plt = func(*args)
            if plt is True:
                bot.send_message(
                    chat_id, "Паттерны закончились поменяйте процент схожести", parse_mode=None, reply=start_keyboard)
            else:
                plt.savefig("data_plot.png", format='png')
                bot.send_photo(chat_id, "data_plot.png",
                               reply=reply_markup, caption=caption)
                os.remove("data_plot.png")
        return send_plot
    return inner


def last_update_message(message_data):
    if message_data["text"] == "/start":
        count = 0
        for message in bot.get_updates():
            try:
                if message["message"]["text"] == "/start":
                    count += 1
            except:
                pass
            if count > 2:
                continue
        if count == 1:
            chat_name = message_data["chat_name"]
            bot.send_message(message_data["chat_id"],
                                f"<b>Приветствую {chat_name}</b>,\nНаш бот принимает Форекс bid/ask "
                                "данные о паре валют и анализирует схожие между собой паттерны"
                                "\nпрогнозируя прибыльные и убыточные исходы трейдинга.", "HTML")
            bot.send_message(
                message_data["chat_id"], "Выберите опцию:", "HTML", start_keyboard)
    if message_data["text"] == "/commands":
        bot.send_message(
            message_data["chat_id"], "Выберите опцию:", "HTML", start_keyboard)


def show_data(callback_query):
    bot.edit_message_reply_markup(
        callback_query['chat_id'], callback_query['message_id'], reply=None)
    return plot_decorator(callback_query['chat_id'], only_search_keyboard)(
        raw_graph)()


def pattern_search(callback_query):
    bot.edit_message_reply_markup(
        callback_query['chat_id'], callback_query['message_id'], reply=None)
    bot.send_message(
        callback_query["chat_id"], "<i>Анализируем данные...</i>", parse_mode="HTML", reply=None)
    global average_line
    average_line = average_line[:to_what]
    pattern_list = []
    performance_list = []
    pattern_storage(average_line, pattern_list, performance_list)
    bot.send_message(
        callback_query["chat_id"], "<i>Ещё немного...</i>", parse_mode="HTML", reply=None)
    pattern_for_recognition = current_pattern(average_line)
    return plot_decorator(callback_query['chat_id'], continue_keyboard, 
                    f"Процент схожести паттернов - {similarity_percentage}%")(
                    pattern_recognizer)(pattern_list, pattern_for_recognition, 
                    performance_list, all_data, to_what, similarity_percentage)


def similarity_count(callback_query):
    bot.edit_message_reply_markup(
        callback_query['chat_id'], callback_query['message_id'], reply=None)
    while True:
        bot.send_message(
            callback_query["chat_id"], "<b>Введите процент схожести от 1 до 100:</b>", parse_mode="HTML", reply=None)
        last_update = bot.get_last_update()
        if last_update != None:
            if "message" in last_update:
                message_data = last_update["message"]["text"]
                try:
                    if int(message_data)<1 or int(message_data)>100:
                        continue 
                except:
                    continue
                if 1<=int(message_data)<=100:
                    return similarity_accept(callback_query,int(message_data))


def similarity_accept(callback_query,given_similarity):
    bot.send_message(callback_query["chat_id"],f"<b>Вы указали -</b> {given_similarity}%",parse_mode="HTML",reply=choice_keyboard)
    while True:
        last_update = bot.get_last_update()
        if last_update != None:
            if "callback_query" in last_update:
                callback_query = last_update["callback_query"]
                if callback_query["data"] == "right_percent":
                    bot.edit_message_reply_markup(
                        callback_query['chat_id'], callback_query['message_id'], reply=None)
                    global similarity_percentage
                    similarity_percentage = int(
                        given_similarity)
                    return similarity_percentage
                elif callback_query["data"] == "wrong_percent":
                    bot.edit_message_reply_markup(
                        callback_query['chat_id'], callback_query['message_id'], reply=None)
                    return similarity_percentage(callback_query=callback_query)


def continue_search(callback_query):
    global to_what,average_line
    if (to_what+1) >= length_of_data:
        bot.edit_message_reply_markup(
            callback_query['chat_id'], callback_query['message_id'], reply=None)
        bot.send_message(
            callback_query["chat_id"], "Паттерны закончились", parse_mode="HTML", reply=start_keyboard)
    else:
        bot.edit_message_caption(
            callback_query['chat_id'], callback_query['message_id'], caption=None)
        bot.edit_message_reply_markup(
            callback_query['chat_id'], callback_query['message_id'], reply=None)
        bot.send_message(
            callback_query["chat_id"], "<i>Анализируем данные...</i>", parse_mode="HTML", reply=None)
        to_what += 1
        average_line = average_line[:to_what]
        pattern_list = []
        performance_list = []
        pattern_storage(
            average_line, pattern_list, performance_list)
        bot.send_message(
            callback_query["chat_id"], "<i>Ещё немного...</i>", parse_mode="HTML", reply=None)
        pattern_for_recognition = current_pattern(
            average_line)
        return plot_decorator(callback_query['chat_id'], continue_keyboard, f"Процент схожести паттернов - {similarity_percentage}%")(
            pattern_recognizer)(pattern_list, pattern_for_recognition, performance_list, all_data, to_what, similarity_percentage)


def stop_search(callback_query):
    bot.edit_message_reply_markup(
        callback_query['chat_id'], callback_query['message_id'], reply=None)
    bot.send_message(
        callback_query["chat_id"], "Вы остановили поиск", parse_mode="HTML", reply=start_keyboard)


def last_update_callback(callback):
    if callback['data'] == "show_data":
        return show_data(callback)
    elif callback['data'] == "pattern_search":
        return pattern_search(callback)
    elif callback['data'] == "similarity_percentage":
        return similarity_count(callback)
    elif callback['data'] == "continue_search":
        return continue_search(callback)
    elif callback['data'] == "stop_search":
        return stop_search(callback)


def main():
    try:
        while True:
            last_update = bot.get_last_update()
            if last_update is not None:
                if "message" in last_update:
                    message = last_update["message"]
                    last_update_message(message)

                if "callback_query" in last_update:
                    callback_query = last_update["callback_query"]
                    last_update_callback(callback_query)
    except Exception as err:
        pass


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
