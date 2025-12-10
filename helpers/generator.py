import random
import string


def generate_random_string(length):
    """
    Генерирует строку, состоящую только из букв нижнего регистра.
    Args:
        length: длина строки
    Returns:
        случайная строка из букв нижнего регистра
    """
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def generate_courier_data():
    """
    Генерирует данные курьера (логин, пароль, имя).
    Returns:
        словарь с ключами: login, password, first_name
    """
    return {
        "login": generate_random_string(10),
        "password": generate_random_string(10),
        "first_name": generate_random_string(10)
    }


def register_new_courier_and_return_login_password():
    """
    Метод регистрации нового курьера возвращает список из логина и пароля.
    Если регистрация не удалась, возвращает пустой список.
    Returns:
        список [login, password, first_name] при успешной регистрации,
        пустой список при неудаче
    """
    import requests
    from config import BASE_URL, ENDPOINTS
    
    # создаём список, чтобы метод мог его вернуть
    login_pass = []
    
    # генерируем данные курьера
    courier_data = generate_courier_data()
    
    # собираем тело запроса
    payload = {
        "login": courier_data["login"],
        "password": courier_data["password"],
        "firstName": courier_data["first_name"]
    }
    
    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post(f'{BASE_URL}{ENDPOINTS["courier"]}', json=payload)
    
    # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
    if response.status_code == 201:
        login_pass.append(courier_data["login"])
        login_pass.append(courier_data["password"])
        login_pass.append(courier_data["first_name"])
    
    # возвращаем список
    return login_pass
