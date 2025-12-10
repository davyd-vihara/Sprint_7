def assert_insufficient_data_error(response):
    """Проверяет ошибку 'Недостаточно данных'"""
    message = response.json()["message"].lower()
    assert "недостаточно данных" in message, \
        f"Сообщение '{response.json()['message']}' не содержит ожидаемого текста 'Недостаточно данных'"


def assert_already_exists_error(response):
    """Проверяет ошибку 'уже используется'"""
    message = response.json()["message"].lower()
    assert "уже используется" in message, \
        f"Сообщение '{response.json()['message']}' не содержит ожидаемого текста 'уже используется'"


def assert_courier_not_found_error(response):
    """Проверяет ошибку 'курьер не найден' - вариант 'курьера с таким id нет'"""
    message = response.json()["message"].lower().rstrip('.')
    assert "курьера с таким id нет" in message, \
        f"Сообщение '{response.json()['message']}' не содержит ожидаемого текста 'курьера с таким id нет'"


def assert_courier_not_exists_error(response):
    """Проверяет ошибку 'курьер не найден' - вариант 'курьера с таким id не существует'"""
    message = response.json()["message"].lower()
    assert "курьера с таким id не существует" in message, \
        f"Сообщение '{response.json()['message']}' не содержит ожидаемого текста 'курьера с таким id не существует'"


def assert_order_not_found_error(response):
    """Проверяет ошибку 'заказ не найден'"""
    message = response.json()["message"].lower()
    assert "заказ не найден" in message, \
        f"Сообщение '{response.json()['message']}' не содержит ожидаемого текста 'заказ не найден'"


def assert_order_not_exists_error(response):
    """Проверяет ошибку 'заказ не найден' - вариант 'заказа с таким id не существует'"""
    message = response.json()["message"].lower()
    assert "заказа с таким id не существует" in message, \
        f"Сообщение '{response.json()['message']}' не содержит ожидаемого текста 'заказа с таким id не существует'"


def assert_account_not_found_error(response):
    """Проверяет ошибку 'учетная запись не найдена'"""
    message = response.json()["message"].lower()
    assert "учетная запись не найдена" in message, \
        f"Сообщение '{response.json()['message']}' не содержит ожидаемого текста 'учетная запись не найдена'"
