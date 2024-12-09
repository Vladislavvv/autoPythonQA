import pytest
import requests
import time
from employee import Employer, Company
from url import X_client_URL

# Константы
LOGIN_URL = 'https://x-clients-be.onrender.com/auth/login'
MAX_RETRIES = 3
RETRY_DELAY = 60  # 60 секунд

CREDENTIALS = {
    "login": "raphael",
    "password": "cool-but-crude"
}

employer = Employer()
company = Company()

@pytest.fixture(scope="session")
def auth_token():
    for attempt in range(MAX_RETRIES):
        response = requests.post(LOGIN_URL, json=CREDENTIALS)
        if response.status_code == 200:
            return response.json()["token"]
        elif attempt < MAX_RETRIES - 1:
            print(f"Auth failed with status code {response.status_code}. Retrying in {RETRY_DELAY} seconds...")
            time.sleep(RETRY_DELAY)
        else:
            print(f"Auth failed after {MAX_RETRIES} attempts with status code {response.status_code}")
            print("Response:", response.text)
            pytest.fail("Authorization failed after retries")


def test_authorization(auth_token):
    """Удостоверяемся, что токен не пустой"""
    assert auth_token is not None
    """Удостоверяемся, что токен имеет строковый формат"""
    assert isinstance(auth_token, str)


def test_getcompany_id(auth_token):
    company_id = company.last_active_company_id()
    """Удостоверяемся, что ID не пустой"""
    assert company_id is not None
    """Проверяем, что ID компании состоит только из цифр"""
    assert str(company_id).isdigit()


def test_add_employer(auth_token):
    token = str(auth_token)
    com_id = company.last_active_company_id()
    body_employer = {
        'id': 0,
        'firstName': 'John',
        'lastName': 'Doe',
        'middleName': 'Smith',
        'companyId': com_id,
        'email': 'john.doe@example.com',
        'url': 'https://example.com',
        'phone': '+1234567890',
        'birthdate': '1990-01-01T00:00:00Z',
        'isActive': 'true'
    }

    response = employer.create(token, body_employer)
    """Проверяем успешное создание сотрудника"""
    assert "id" in response
    new_employer_id = response['id']

    # Удостоверяемся, что ID сотрудника не пустой
    assert new_employer_id is not None

    # Проверяем, что ID сотрудника состоит только из цифр
    assert str(new_employer_id).isdigit()

    # Получаем информацию о добавленном сотруднике
    info = employer.get_info(new_employer_id)

    # Сравниваем ID сотрудника из полученной информации с ID сотрудника, которое появилось при создании
    assert info.json()['id'] == new_employer_id

    # Проверяем, что код ответа == 200
    assert info.status_code == 200


@pytest.mark.parametrize("missing_field", ["firstName", "lastName", "phone"])
def test_create_employee_missing_fields(auth_token, missing_field):
    token = str(auth_token)
    com_id = company.last_active_company_id()
    body_employer = {
        "companyId": com_id,
        "firstName": "John",
        "lastName": "Doe",
        "phone": "+1234567890"
    }
    body_employer.pop(missing_field)
    response = requests.post(f'{X_client_URL}/employee', headers={'x-client-token': token}, json=body_employer)
    """Проверяем, что при отсутствии обязательного поля запрос возвращает ошибку 400"""
    assert response.status_code == 400


def test_get_employee_by_id(auth_token):
    token = str(auth_token)
    employee_id = 1  # Используйте существующий ID для этого теста
    response = employer.get_by_id(token, employee_id)
    """Проверяем успешное получение сотрудника по ID"""
    assert response["id"] == employee_id


def test_update_employee(auth_token):
    token = str(auth_token)
    employee_id = 1  # Используйте существующий ID для этого теста
    updated_data = {
        "firstName": "Jane",
        "lastName": "Doe",
        "phone": "+0987654321"
    }
    response = employer.update(token, employee_id, updated_data)
    """Проверяем успешное обновление данных сотрудника"""
    assert response["firstName"] == "Jane"
    assert response["phone"] == "+0987654321"


def test_get_employees(auth_token):
    token = str(auth_token)
    response = employer.get_all(token)
    """Проверяем успешное получение списка сотрудников"""
    assert isinstance(response, list)
    assert len(response) > 0  # Проверка, что список не пуст