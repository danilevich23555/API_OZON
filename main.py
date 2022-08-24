from ozonClass import OZON_API
from settings import token, client_id

if __name__ == '__main__':
        ozon=OZON_API(token, client_id)
        print(ozon.GET_Actions())
        print(ozon.GET_Candidates())