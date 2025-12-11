import pytest

from helpers.assertions import assert_insufficient_data_error, assert_already_exists_error
from helpers.generator import generate_random_string


class TestCreateCourier:
    """Тесты для создания курьера"""
    
    @pytest.mark.courier
    def test_create_courier_success(self, api_client, courier_data, delete_courier):
        """Проверка успешного создания курьера"""
        # Создаём курьера
        response = api_client.create_courier(
            courier_data["login"],
            courier_data["password"],
            courier_data["first_name"]
        )
        
        # Регистрируем курьера для удаления после теста
        login_response = api_client.login_courier(
            courier_data["login"],
            courier_data["password"]
        )
        courier_id = login_response.json()["id"]
        delete_courier(courier_id)
        
        # Проверяем успешное создание
        assert response.status_code == 201
        assert response.json() == {"ok": True}
    
    @pytest.mark.courier
    def test_created_courier_can_login(self, api_client, courier_data, delete_courier):
        """Проверка, что созданный курьер может авторизоваться"""
        # Создаём курьера
        api_client.create_courier(
            courier_data["login"],
            courier_data["password"],
            courier_data["first_name"]
        )
        
        # Авторизуемся
        login_response = api_client.login_courier(
            courier_data["login"],
            courier_data["password"]
        )
        courier_id = login_response.json()["id"]
        delete_courier(courier_id)
        
        # Проверяем успешную авторизацию
        assert login_response.status_code == 200
        assert "id" in login_response.json()
        assert isinstance(login_response.json()["id"], int)
    
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
    def test_create_courier_without_login(self, api_client, courier_data):
        """Проверка создания курьера без поля login"""
        response = api_client.create_courier("", courier_data["password"], courier_data["first_name"])
        
        assert response.status_code == 400
        assert_insufficient_data_error(response)
    
    @pytest.mark.courier
    def test_create_courier_without_password(self, api_client, courier_data):
        """Проверка создания курьера без поля password"""
        response = api_client.create_courier(courier_data["login"], "", courier_data["first_name"])
        
        assert response.status_code == 400
        assert_insufficient_data_error(response)
    
    @pytest.mark.courier
    def test_create_courier_without_first_name(self, api_client, courier_data, delete_courier):
        """Проверка создания курьера без имени (необязательное поле)"""
        # Создаём курьера без имени
        response = api_client.create_courier(
            courier_data["login"],
            courier_data["password"],
            None
        )
        
        # Регистрируем курьера для удаления после теста
        login_response = api_client.login_courier(
            courier_data["login"],
            courier_data["password"]
        )
        courier_id = login_response.json()["id"]
        delete_courier(courier_id)
        
        assert response.status_code == 201
        assert response.json() == {"ok": True}
    
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
    def test_create_courier_returns_ok_true(self, api_client, courier_data, delete_courier):
        """Проверка, что успешный запрос возвращает {"ok": true}"""
        # Создаём курьера
        response = api_client.create_courier(
            courier_data["login"],
            courier_data["password"],
            courier_data["first_name"]
        )
        
        # Регистрируем курьера для удаления после теста
        login_response = api_client.login_courier(
            courier_data["login"],
            courier_data["password"]
        )
        courier_id = login_response.json()["id"]
        delete_courier(courier_id)
        
        assert response.status_code == 201
        assert response.json() == {"ok": True}
