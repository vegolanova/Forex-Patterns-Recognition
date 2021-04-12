import requests
from time import sleep
import json


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
            current_update_id = last_update["update_id"]
            
            
            if self.last_update_id != current_update_id:
                self.last_update_id = current_update_id
                if "message" in last_update:
                    chat_id = last_update["message"]["chat"]["id"]
                    message_text = last_update["message"]["text"]
                    chat_name = last_update['message']['chat']['first_name']
                    message = {"message": {"chat_id": chat_id,
                            "text": message_text, "chat_name": chat_name}}
                    return message

                elif "callback_query" in last_update:
                    callback_query_id = last_update["callback_query"]["id"]
                    chat_id = last_update["callback_query"]["message"]["chat"]["id"]
                    callback_data = last_update["callback_query"]["data"]
                    chat_name = last_update["callback_query"]['message']['chat']['first_name']
                    message_id = last_update["callback_query"]['message']["message_id"]
                    message = {"callback_query":{"callback_query_id":callback_query_id,"data":callback_data,"chat_id":chat_id, "chat_name": chat_name,"message_id":message_id}}

                    return message
                else:
                    return None
        except err as Exception:
            print(err)

    def send_message(self, chat_id, text, reply=None):
        params = {'chat_id': chat_id, 'text': text, 'reply_markup': reply}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp
    
    def answer_callback_query(self, callback_query_id,text=None,show_alert=None,url=None,cache_time=None):
        params = {'callback_query_id': callback_query_id,'text':text,'show_alert':show_alert,'url':url,'cache_time':cache_time}
        method = 'answerCallbackQuery'
        resp = requests.post(self.api_url + method, params)
        return resp
    
    def edit_message_text(self, chat_id, message_id,text,reply=None):
        params = {'chat_id': chat_id, 'message_id': message_id,"text":text,"reply_markup":reply}
        method = 'editMessageText'
        resp = requests.post(self.api_url + method, params)
        return resp



token = "1296005096:AAH-RyXl6xoA57GdEPMwu9YIsGq4jly0WDo"
bot = BotHandler(token)


def main():
    while True:
        last_update = bot.get_last_update()
        if last_update != None:
            if "message" in last_update:
                chat_id = last_update["message"]["chat_id"]
                text = last_update["message"]["text"]
                chat_name = last_update["message"]["chat_name"]
                if text == "/start":
                    reply = json.dumps({'inline_keyboard':
                                    [
                                        [{'text': 'Crypto', 'callback_data': 'crypto'}],
                                        [{'text': 'Shares', 'callback_data': 'shares'}]
                                                                                        ],
                                        "resize_keyboard": True
                                                                                        })
                    bot.send_message(chat_id, f'Приветствую {chat_name} \n Выберите вид:', reply)
                if text == "Привет":
                    bot.send_message(chat_id, f'Приветствую')
            if "callback_query" in last_update:
                
                callback_query_id = last_update["callback_query"]["callback_query_id"]
                chat_id = last_update["callback_query"]["chat_id"]
                data = last_update["callback_query"]["data"]
                chat_name = last_update["callback_query"]["chat_name"]
                message_id = last_update["callback_query"]["message_id"]
                if data =="crypto":
                    reply = json.dumps({'inline_keyboard':
                                    [
                                        [{'text': 'BTC', 'callback_data': 'BTC'}],
                                        [{'text': 'ETH', 'callback_data': 'ETH'}],
                                        [{'text': 'XRP', 'callback_data': 'XRP'}],
                                        [{'text': 'ADA', 'callback_data': 'ADA'}],
                                        [{'text': 'DOT', 'callback_data': 'DOT'}],
                                        [{'text': 'UNI', 'callback_data': 'UNI'}]
                                                                                        ],
                                        "resize_keyboard": True
                                                                                        })
                    bot.edit_message_text(chat_id,message_id,"Вы выбрали криптовалюту!\nТеперь выберите паттерны какой криптовалюты вы бы хотели рассмотреть",reply)
                    
                    
                    

                if data =="shares":
                    bot.edit_message_text(chat_id,message_id,"Вы выбрали криптовалюту!/nТеперь выберите паттерны какой криптовалюты вы бы хотели рассмотреть",reply)
                    bot.send_message(chat_id, f'Вы выбрали shares')
        else:
            continue
        

        sleep(4)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
        
