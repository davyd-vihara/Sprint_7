import pytest

from helpers.assertions import assert_insufficient_data_error, assert_account_not_found_error
from helpers.generator import generate_random_string


class TestLoginCourier:
    """Тесты для логина курьера"""
    
    @pytest.mark.courier
    def test_login_courier_success(self, api_client, created_courier):
        """Проверка успешной авторизации курьера"""
        response = api_client.login_courier(
            created_courier["login"],
            created_courier["password"]
        )
        
        assert response.status_code == 200
        response_body = response.json()
        assert "id" in response_body
        assert isinstance(response_body["id"], int)
    
    @pytest.mark.courier
    def test_login_courier_without_login(self, api_client, created_courier):
        """Проверка авторизации без поля login"""
        response = api_client.login_courier("", created_courier["password"])
        
        assert response.status_code == 400
        assert_insufficient_data_error(response)
    
    @pytest.mark.courier
    def test_login_courier_without_password(self, api_client, created_courier):
        """Проверка авторизации без поля password"""
        response = api_client.login_courier(created_courier["login"], "")
        
        assert response.status_code == 400
        assert_insufficient_data_error(response)
    
    @pytest.mark.courier
    @pytest.mark.parametrize("wrong_field", ["login", "password"])
    def test_login_courier_with_wrong_credentials(self, api_client, created_courier, wrong_field):
        """Проверка авторизации с неверными данными"""
        login = generate_random_string(10) if wrong_field == "login" else created_courier["login"]
        password = generate_random_string(10) if wrong_field == "password" else created_courier["password"]
        
        response = api_client.login_courier(login, password)
        
        assert response.status_code == 404
        assert_account_not_found_error(response)
    
    @pytest.mark.courier
    def test_login_nonexistent_courier(self, api_client):
        """Проверка авторизации несуществующего курьера"""
        response = api_client.login_courier(
            generate_random_string(10),
            generate_random_string(10)
        )
        
        assert response.status_code == 404
        assert_account_not_found_error(response)
