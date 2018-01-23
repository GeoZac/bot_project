import requests

class Bot:
    """All telegram methods are to be included in class definition"""

    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        print(self.api_url + method, params)
        return resp

    def send_reply(self, chat_id, text, reply_to):
        params = {'chat_id': chat_id, 'text': text, 'reply_to_message_id': reply_to}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        print(self.api_url + method, params)
        return resp

    def get_last_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result[len(get_result)]

        return last_update

    def get_admins(self, chat_id):
        params = {'chat_id': chat_id}
        method = 'getChatAdministrators'
        resp = requests.post(self.api_url + method, params)
        resp = resp.json()['result']
        return resp

    def delete_msg(self, chat_id, msg_id):
        params = {'chat_id': chat_id, 'message_id': msg_id}
        method = 'deleteMessage'
        requests.post(self.api_url + method, params)

sasi_bot = Bot("my_super_secret_bot_key")

def main():
    new_offset = None
    while True:
        unconv_bot.get_updates(new_offset)
        last_update = unconv_bot.get_last_update()
        last_update_id = last_update['update_id']
        last_message = last_update['message']
        last_message_id = last_update['message']['message_id']
        last_chat_id = last_update['message']['chat']['id']
        last_chat = last_update['message']['chat']

        new_offset = last_update_id + 1

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
