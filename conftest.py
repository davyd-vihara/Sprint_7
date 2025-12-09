import pytest

from helpers.api_client import ScooterApiClient
from helpers.generator import generate_random_string


@pytest.fixture
def api_client():
    """Фикстура для создания API клиента"""
    return ScooterApiClient()


@pytest.fixture
def courier_data():
    """
    Фикстура для создания данных курьера.
    Возвращает словарь с login, password, first_name.
    """
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    
    return {
        "login": login,
        "password": password,
        "first_name": first_name
    }


@pytest.fixture
def created_courier(api_client, courier_data):
    """
    Фикстура для создания курьера перед тестом.
    После теста курьер удаляется.
    """
    # Создаём курьера
    response = api_client.create_courier(
        courier_data["login"],
        courier_data["password"],
        courier_data["first_name"]
    )
    
    # Проверяем успешное создание
    assert response.status_code == 201
    
    # Получаем ID курьера для удаления
    login_response = api_client.login_courier(
        courier_data["login"],
        courier_data["password"]
    )
    assert login_response.status_code == 200
    courier_id = login_response.json()["id"]
    
    yield {
        "login": courier_data["login"],
        "password": courier_data["password"],
        "first_name": courier_data["first_name"],
        "id": courier_id
    }
    
    # Удаляем курьера после теста
    api_client.delete_courier(courier_id)


@pytest.fixture
def order_data():
    """
    Фикстура для создания данных заказа.
    Возвращает словарь с данными заказа.
    """
    return {
        "first_name": "Иван",
        "last_name": "Иванов",
        "address": "Москва, ул. Ленина, д. 1",
        "metro_station": 4,
        "phone": "+79991234567",
        "rent_time": 5,
        "delivery_date": "2024-12-31",
        "comment": "Тестовый заказ"
    }


@pytest.fixture
def created_order(api_client, order_data):
    """
    Фикстура для создания заказа перед тестом.
    Возвращает словарь с track и order_id.
    """
    # Создаём заказ
    create_response = api_client.create_order(
        first_name=order_data["first_name"],
        last_name=order_data["last_name"],
        address=order_data["address"],
        metro_station=order_data["metro_station"],
        phone=order_data["phone"],
        rent_time=order_data["rent_time"],
        delivery_date=order_data["delivery_date"],
        comment=order_data["comment"]
    )
    
    assert create_response.status_code == 201
    track = create_response.json()["track"]
    
    # Получаем заказ по track, чтобы узнать его ID
    get_order_response = api_client.get_order_by_track(track)
    assert get_order_response.status_code == 200
    order_id = get_order_response.json()["order"]["id"]
    
    return {
        "track": track,
        "order_id": order_id
    }


@pytest.fixture
def courier_creation_response(api_client, courier_data):
    """
    Фикстура для создания курьера и получения response.
    После теста курьер автоматически удаляется через yield.
    """
    # Создаём курьера
    response = api_client.create_courier(
        courier_data["login"],
        courier_data["password"],
        courier_data["first_name"]
    )
    
    # Получаем ID курьера для удаления после теста
    # Проверяем успешное создание (для тестов, которые проверяют успешное создание)
    assert response.status_code == 201
    
    login_response = api_client.login_courier(
        courier_data["login"],
        courier_data["password"]
    )
    assert login_response.status_code == 200
    courier_id = login_response.json()["id"]
    
    # Возвращаем response для проверки в тесте
    yield response
    
    # Удаляем курьера после теста
    api_client.delete_courier(courier_id)
