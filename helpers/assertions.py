def assert_error_message_contains(response, expected_texts):
    """
    Проверяет, что сообщение об ошибке содержит один из ожидаемых текстов.
    Args:
        response: объект Response от requests
        expected_texts: список строк для поиска в сообщении
    """
    message = response.json()["message"].lower()
    assert any(text.lower() in message for text in expected_texts), \
        f"Сообщение '{response.json()['message']}' не содержит ни одного из ожидаемых текстов: {expected_texts}"


def assert_insufficient_data_error(response):
    """Проверяет ошибку 'Недостаточно данных'"""
    assert_error_message_contains(response, ["Недостаточно данных", "required"])


def assert_already_exists_error(response):
    """Проверяет ошибку 'уже используется'"""
    assert_error_message_contains(response, ["уже используется", "already exists"])


def assert_not_found_error(response, entity_type="объект"):
    """
    Проверяет ошибку 'не найдено'.
    Args:
        response: объект Response от requests
        entity_type: тип объекта для более точной проверки ("курьер", "заказ", "учетная запись")
    """
    if entity_type == "курьер":
        expected_texts = ["курьера с таким id нет", "курьера с таким id не существует", "not found"]
    elif entity_type == "заказ":
        expected_texts = ["заказа с таким id не существует", "заказ не найден", "not found"]
    elif entity_type == "учетная запись":
        expected_texts = ["учетная запись не найдена", "not found"]
    else:
        expected_texts = ["не найдено", "not found"]
    
    assert_error_message_contains(response, expected_texts)
