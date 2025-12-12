import requests

from config import BASE_URL, ENDPOINTS


class ScooterApiClient:
    """Клиент для работы с API Яндекс Самокат"""
    
    def __init__(self):
        self.base_url = BASE_URL
    
    def create_courier(self, login, password, first_name=None):
        """
        Создание курьера.
        Args:
            login: логин курьера
            password: пароль курьера
            first_name: имя курьера (опционально)
        Returns:
            объект Response
        """
        payload = {
            "login": login,
            "password": password
        }
        if first_name is not None:
            payload["firstName"] = first_name
        return requests.post(f'{self.base_url}{ENDPOINTS["courier"]}', json=payload)
    
    def login_courier(self, login, password):
        """
        Авторизация курьера.
        Args:
            login: логин курьера
            password: пароль курьера
        Returns:
            объект Response
        """
        payload = {
            "login": login,
            "password": password
        }
        return requests.post(f'{self.base_url}{ENDPOINTS["courier_login"]}', json=payload)
    
    def delete_courier(self, courier_id):
        """
        Удаление курьера.
        Args:
            courier_id: ID курьера
        Returns:
            объект Response
        """
        endpoint = ENDPOINTS["courier_delete"].format(courier_id=courier_id)
        return requests.delete(f'{self.base_url}{endpoint}')
    
    def create_order(self, first_name, last_name, address, metro_station, phone, rent_time, delivery_date, comment):
        """
        Создание заказа без указания цвета.
        Args:
            first_name: имя
            last_name: фамилия
            address: адрес
            metro_station: станция метро
            phone: телефон
            rent_time: время аренды
            delivery_date: дата доставки
            comment: комментарий
        Returns:
            объект Response
        """
        payload = {
            "firstName": first_name,
            "lastName": last_name,
            "address": address,
            "metroStation": metro_station,
            "phone": phone,
            "rentTime": rent_time,
            "deliveryDate": delivery_date,
            "comment": comment
        }
        return requests.post(f'{self.base_url}{ENDPOINTS["orders"]}', json=payload)
    
    def create_order_with_color(self, first_name, last_name, address, metro_station, phone, rent_time, delivery_date, comment, color):
        """
        Создание заказа с указанием цвета.
        Args:
            first_name: имя
            last_name: фамилия
            address: адрес
            metro_station: станция метро
            phone: телефон
            rent_time: время аренды
            delivery_date: дата доставки
            comment: комментарий
            color: цвет самоката (BLACK, GREY или список)
        Returns:
            объект Response
        """
        payload = {
            "firstName": first_name,
            "lastName": last_name,
            "address": address,
            "metroStation": metro_station,
            "phone": phone,
            "rentTime": rent_time,
            "deliveryDate": delivery_date,
            "comment": comment,
            "color": color
        }
        return requests.post(f'{self.base_url}{ENDPOINTS["orders"]}', json=payload)
    
    def get_orders_list(self):
        """
        Получение списка заказов.
        Returns:
            объект Response
        """
        return requests.get(f'{self.base_url}{ENDPOINTS["orders"]}')
    
    def accept_order(self, order_id, courier_id):
        """
        Принять заказ.
        Args:
            order_id: ID заказа
            courier_id: ID курьера
        Returns:
            объект Response
        """
        endpoint = ENDPOINTS["orders_accept"].format(order_id=order_id)
        return requests.put(
            f'{self.base_url}{endpoint}',
            params={"courierId": courier_id}
        )
    
    def get_order_by_track(self, track):
        """
        Получить заказ по его номеру.
        Args:
            track: номер заказа
        Returns:
            объект Response
        """
        return requests.get(
            f'{self.base_url}{ENDPOINTS["orders_track"]}',
            params={"t": track}
        )
