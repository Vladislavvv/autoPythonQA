import requests
import json
from url import X_client_URL

path = '/employee/'

class Company:
    def __init__(self, url=X_client_URL):
        self.url = url

    # Создание компании
    def create(self, token: str, body: json):
        headers = {'x-client-token': token}
        response = requests.post(f'{self.url}/company', headers=headers, params=body)
        return response.json()

    # Последняя созданная активная компания
    def last_active_company_id(self):
        active_params = {'active': 'true'}
        response = requests.get(f'{self.url}/company', params=active_params)
        companies = response.json()

        if companies:
            return companies[-1]['id']
        else:
            raise ValueError("No active companies found")


class Employer:
    def __init__(self, url=X_client_URL):
        self.url = url

    # Создание сотрудника
    def create(self, token: str, body: json):
        headers = {'x-client-token': token}
        response = requests.post(f'{self.url}/employee', headers=headers, json=body)
        return response.json()

    # Получение сотрудника по ID
    def get_by_id(self, token: str, employee_id: int):
        headers = {'x-client-token': token}
        response = requests.get(f'{self.url}/employee/{employee_id}', headers=headers)
        return response.json()

    # Обновление сотрудника
    def update(self, token: str, employee_id: int, body: json):
        headers = {'x-client-token': token}
        response = requests.patch(f'{self.url}/employee/{employee_id}', headers=headers, json=body)
        return response.json()

    # Получение всех сотрудников
    def get_all(self, token: str):
        headers = {'x-client-token': token}
        response = requests.get(f'{self.url}/employee', headers=headers)
        return response.json()