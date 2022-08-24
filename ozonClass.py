import requests
import os
import datetime

class OZON_API:

    def __init__(self, token, client_id):
        self.token = token
        self.client_id = client_id

    def write_log_file(self, res_status, res_method, res_url, client_id):
        now = datetime.datetime.now()
        name_file = 'log-file' + f'{now.strftime("%d-%m-%Y")}' + '.txt'
        path = os.path.os.getcwd() + '/log'
        with open(os.path.join(path, name_file), 'a') as log:
            log.write(
                f'{now.strftime("%d-%m-%Y %H:%M:%S")}' + ' | ' + f'Ошибка, код ответа: {res_status}' + ' | '
                + f'{res_method}' + ' | ' + f'{res_url}' + ' | ' + f'{client_id}''\n')


    def get_headers(self):
        return {
            'Api-Key': format(self.token),
            'Client-Id': format(self.client_id),
            'Content-type': 'application/json'
        }

    def GET_Actions(self):
        url = 'https://api-seller.ozon.ru/v1/actions'
        HEADERS = self.get_headers()
        temp = []
        try:
            response = requests.get(url=url, headers=HEADERS)
            if response.status_code == 200:
                [temp.append(x['id']) for x in (response.json())['result']]
                return temp
            else:
                self.write_log_file(response.status_code, response.request.method, response.url, format(self.client_id))
        except TypeError:
            return print('Ошибка, посмотрите log-file')

    def GET_Candidates(self):
        url = 'https://api-seller.ozon.ru/v1/actions/candidates'
        temp = []
        pere = self.GET_Actions()
        try:
            [temp.append({"action_id": x, "limit": 0, "offset": 0}) for x in pere]
            temp1 = []
            for y in range(len(pere)):
                response = requests.post(url=url, headers=self.get_headers(), json=temp[y])
                if response.status_code == 200:
                    temp1.append({pere[y]: response.json()['result']['products']})
                else:
                    self.write_log_file(response.status_code, response.request.method, response.url, format(self.client_id))
            return temp1
        except TypeError:
            return print('Ошибка, посмотрите log-file')
