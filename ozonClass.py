import requests


class OZON_API:

    def __init__(self, token, client_id):
        self.token = token
        self.client_id = client_id

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
        response = requests.get(url=url, headers=HEADERS)
        [temp.append(x['id']) for x in (response.json())['result']]
        return temp

    def GET_Candidates(self):
        url = 'https://api-seller.ozon.ru/v1/actions/candidates'
        temp = []
        pere = self.GET_Actions()
        [temp.append({"action_id": x, "limit": 0, "offset": 0}) for x in pere]
        temp1 = []
        for y in range(len(pere)):
            response = requests.post(url=url, headers=self.get_headers(), json=temp[y])
            temp1.append({pere[y]: response.json()['result']['products']})
        return temp1
