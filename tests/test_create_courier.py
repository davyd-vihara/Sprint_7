import pytest

from helpers.assertions import assert_insufficient_data_error, assert_already_exists_error
from helpers.generator import generate_random_string


class TestCreateCourier:
    """Тесты для создания курьера"""
    
    @pytest.mark.courier
    def test_create_courier_success(self, api_client, created_courier):
        """Проверка успешного создания курьера"""
        # Курьер уже создан через фикстуру created_courier
        # Проверяем, что он был создан успешно
        assert created_courier["id"] is not None
        
        # Проверяем, что можем авторизоваться
        login_response = api_client.login_courier(
            created_courier["login"],
            created_courier["password"]
        )
        assert login_response.status_code == 200
        assert "id" in login_response.json()
    
    @pytest.mark.courier
    def test_create_duplicate_courier(self, api_client, created_courier):
        """Проверка, что нельзя создать двух одинаковых курьеров"""
        # Пытаемся создать курьера с теми же данными
        response = api_client.create_courier(
            created_courier["login"],
            created_courier["password"],
            created_courier["first_name"]
        )
        
        assert response.status_code == 409
        assert_already_exists_error(response)
    
    @pytest.mark.courier
    @pytest.mark.parametrize("missing_field,field_value", [
        ("login", ""),
        ("password", ""),
    ])
    def test_create_courier_without_required_fields(self, api_client, courier_data, missing_field, field_value):
        """Проверка создания курьера без обязательных полей"""
        login = field_value if missing_field == "login" else courier_data["login"]
        password = field_value if missing_field == "password" else courier_data["password"]
        first_name = courier_data["first_name"]
        
        response = api_client.create_courier(login, password, first_name)
        
        assert response.status_code == 400
        assert_insufficient_data_error(response)
    
    @pytest.mark.courier
    def test_create_courier_without_first_name(self, api_client, courier_data):
        """Проверка создания курьера без имени (необязательное поле)"""
        # Передаём None, чтобы поле вообще не было в запросе
        response = api_client.create_courier(
            courier_data["login"],
            courier_data["password"],
            None
        )
        
        # API принимает курьера без firstName (поле необязательное)
        assert response.status_code == 201
        assert response.json() == {"ok": True}
        
        # Удаляем созданного курьера
        login_response = api_client.login_courier(
            courier_data["login"],
            courier_data["password"]
        )
        assert login_response.status_code == 200
        courier_id = login_response.json()["id"]
        api_client.delete_courier(courier_id)
    
    @pytest.mark.courier
    def test_create_courier_with_existing_login(self, api_client, created_courier):
        """Проверка создания курьера с существующим логином"""
        # Пытаемся создать курьера с тем же логином, но другими данными
        response = api_client.create_courier(
            created_courier["login"],
            generate_random_string(10),
            generate_random_string(10)
        )
        
        assert response.status_code == 409
        assert_already_exists_error(response)
    
    @pytest.mark.courier
    def test_create_courier_returns_ok_true(self, courier_creation_response):
        """Проверка, что успешный запрос возвращает {"ok": true}"""
        response = courier_creation_response
        
        # Проверяем согласно заданию
        assert response.status_code == 201
        assert response.json() == {"ok": True}
