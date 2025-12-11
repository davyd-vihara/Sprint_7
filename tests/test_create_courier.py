import pytest
import allure

from helpers.assertions import assert_insufficient_data_error, assert_already_exists_error
from helpers.generator import generate_random_string


class TestCreateCourier:
    """Тесты для создания курьера"""
    
    @pytest.mark.courier
    @allure.title("Успешное создание курьера")
    @allure.description("Проверка успешного создания курьера с валидными данными")
    def test_create_courier_success(self, api_client, courier_data, delete_courier):
        """Проверка успешного создания курьера"""
        with allure.step("Создать курьера"):
            response = api_client.create_courier(
                courier_data["login"],
                courier_data["password"],
                courier_data["first_name"]
            )
        
        with allure.step("Получить ID курьера для удаления"):
            login_response = api_client.login_courier(
                courier_data["login"],
                courier_data["password"]
            )
            courier_id = login_response.json()["id"]
            delete_courier(courier_id)
        
        with allure.step("Проверить успешное создание"):
            assert response.status_code == 201
            assert response.json() == {"ok": True}
    
    @pytest.mark.courier
    @allure.title("Авторизация созданного курьера")
    @allure.description("Проверка, что созданный курьер может авторизоваться")
    def test_created_courier_can_login(self, api_client, courier_data, delete_courier):
        """Проверка, что созданный курьер может авторизоваться"""
        with allure.step("Создать курьера"):
            api_client.create_courier(
                courier_data["login"],
                courier_data["password"],
                courier_data["first_name"]
            )
        
        with allure.step("Авторизоваться курьером"):
            login_response = api_client.login_courier(
                courier_data["login"],
                courier_data["password"]
            )
            courier_id = login_response.json()["id"]
            delete_courier(courier_id)
        
        with allure.step("Проверить успешную авторизацию"):
            assert login_response.status_code == 200
            assert "id" in login_response.json()
            assert isinstance(login_response.json()["id"], int)
    
    @pytest.mark.courier
    @allure.title("Создание дубликата курьера")
    @allure.description("Проверка, что нельзя создать двух одинаковых курьеров")
    def test_create_duplicate_courier(self, api_client, created_courier):
        """Проверка, что нельзя создать двух одинаковых курьеров"""
        with allure.step("Попытаться создать курьера с теми же данными"):
            response = api_client.create_courier(
                created_courier["login"],
                created_courier["password"],
                created_courier["first_name"]
            )
        
        with allure.step("Проверить ошибку дубликата"):
            assert response.status_code == 409
            assert_already_exists_error(response)
    
    @pytest.mark.courier
    @allure.title("Создание курьера без поля login")
    @allure.description("Проверка создания курьера без обязательного поля login")
    def test_create_courier_without_login(self, api_client, courier_data):
        """Проверка создания курьера без поля login"""
        with allure.step("Создать курьера без поля login"):
            response = api_client.create_courier("", courier_data["password"], courier_data["first_name"])
        
        with allure.step("Проверить ошибку недостаточных данных"):
            assert response.status_code == 400
            assert_insufficient_data_error(response)
    
    @pytest.mark.courier
    @allure.title("Создание курьера без поля password")
    @allure.description("Проверка создания курьера без обязательного поля password")
    def test_create_courier_without_password(self, api_client, courier_data):
        """Проверка создания курьера без поля password"""
        with allure.step("Создать курьера без поля password"):
            response = api_client.create_courier(courier_data["login"], "", courier_data["first_name"])
        
        with allure.step("Проверить ошибку недостаточных данных"):
            assert response.status_code == 400
            assert_insufficient_data_error(response)
    
    @pytest.mark.courier
    @allure.title("Создание курьера без имени")
    @allure.description("Проверка создания курьера без имени (необязательное поле)")
    def test_create_courier_without_first_name(self, api_client, courier_data, delete_courier):
        """Проверка создания курьера без имени (необязательное поле)"""
        with allure.step("Создать курьера без имени"):
            response = api_client.create_courier(
                courier_data["login"],
                courier_data["password"],
                None
            )
        
        with allure.step("Получить ID курьера для удаления"):
            login_response = api_client.login_courier(
                courier_data["login"],
                courier_data["password"]
            )
            courier_id = login_response.json()["id"]
            delete_courier(courier_id)
        
        with allure.step("Проверить успешное создание"):
            assert response.status_code == 201
            assert response.json() == {"ok": True}
    
    @pytest.mark.courier
    @allure.title("Создание курьера с существующим логином")
    @allure.description("Проверка создания курьера с существующим логином, но другими данными")
    def test_create_courier_with_existing_login(self, api_client, created_courier):
        """Проверка создания курьера с существующим логином"""
        with allure.step("Попытаться создать курьера с тем же логином, но другими данными"):
            response = api_client.create_courier(
                created_courier["login"],
                generate_random_string(10),
                generate_random_string(10)
            )
        
        with allure.step("Проверить ошибку дубликата"):
            assert response.status_code == 409
            assert_already_exists_error(response)
    
    @pytest.mark.courier
    @allure.title("Проверка ответа при успешном создании курьера")
    @allure.description("Проверка, что успешный запрос возвращает {'ok': true}")
    def test_create_courier_returns_ok_true(self, api_client, courier_data, delete_courier):
        """Проверка, что успешный запрос возвращает {"ok": true}"""
        with allure.step("Создать курьера"):
            response = api_client.create_courier(
                courier_data["login"],
                courier_data["password"],
                courier_data["first_name"]
            )
        
        with allure.step("Получить ID курьера для удаления"):
            login_response = api_client.login_courier(
                courier_data["login"],
                courier_data["password"]
            )
            courier_id = login_response.json()["id"]
            delete_courier(courier_id)
        
        with allure.step("Проверить ответ с {'ok': true}"):
            assert response.status_code == 201
            assert response.json() == {"ok": True}
