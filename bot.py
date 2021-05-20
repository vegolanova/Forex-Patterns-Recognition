from keyboards import start_keyboard,only_search_keyboard
import requests
from time import sleep
import json
import os
from UNEDITED.randomPatternRecognizer import raw_graph
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
                    message = {'callback_query':{'callback_query_id':callback_query_id,'data':callback_data,'chat_id':chat_id, 'chat_name': chat_name,'message_id':message_id}}

                    return message
                else:
                    return None
        except Exception as err:
            print(err)

    def send_message(self, chat_id, text, parse_mode=None, reply=None):
        params = {'chat_id': chat_id, 'text': text, 'parse_mode': parse_mode, 'reply_markup': reply}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def send_photo(self, chat_id, photo,caption=None,parse_mode=None,reply_markup=None):
        files = {'photo': open(photo, 'rb')}
        params = {'chat_id': chat_id, 'caption':caption, 'parse_mode': parse_mode,"reply_markup":reply_markup}
        method = 'sendPhoto'
        resp= requests.post(self.api_url+method, files=files, data=params)
        return resp

    def answer_callback_query(self, callback_query_id,text=None,show_alert=None,url=None,cache_time=None):
        params = {'callback_query_id': callback_query_id,'text':text,'show_alert':show_alert,'url':url,'cache_time':cache_time}
        method = 'answerCallbackQuery'
        resp = requests.post(self.api_url + method, params)
        return resp
    
    def edit_message_text(self, chat_id, message_id,text,parse_mode=None,reply=None):
        params = {'chat_id': chat_id, 'message_id': message_id,'text':text,'parse_mode':parse_mode,'reply_markup':reply}
        method = 'editMessageText'
        resp = requests.post(self.api_url + method, params)
        return resp



token = "1296005096:AAF9495V7dGFti8W8jGb37vqirAf2pARUTM"
bot = BotHandler(token)


def main():
    while True:
        try:
            last_update = bot.get_last_update()
            if last_update != None:
                if "message" in last_update:
                    message_data = last_update["message"]
                    if message_data["text"] == "/start":
                        chat_name = message_data["chat_name"]
                        try:
                            bot.send_message(message_data["chat_id"], 
                            f"<b>Приветствую {chat_name}</b>,\nНаш бот принимает Форекс bid/ask "\
                            "данные о паре валют и анализирует схожие между собой паттерны"\
                            "\nпрогнозируя прибыльные и убыточные исходы трейдинга.","HTML")
                            bot.send_message(message_data["chat_id"], "Выберите опцию:","HTML",json.dumps(start_keyboard))
                        except Exception as err:
                            print(err)
                    
                if "callback_query" in last_update:
                    callback_query = last_update["callback_query"]
                    print(callback_query)
                    if callback_query['data'] =="show_data":
                        try:
                            bot.edit_message_text(callback_query['chat_id'],callback_query['message_id'],"Выберите опцию:","HTML")
                            plt = raw_graph()
                            plt.savefig("data_plot.png", format='png')
                            bot.send_photo(callback_query['chat_id'],"data_plot.png",reply_markup=json.dumps(only_search_keyboard))
                            os.remove("data_plot.png")
                        except Exception as err:
                            print(err)
        except Exception as err:
            print(err)
                    
                    
                    

                    

                
        else:
            continue
        

        sleep(4)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
        


