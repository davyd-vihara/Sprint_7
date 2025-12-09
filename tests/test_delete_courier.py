import pytest

from helpers.assertions import assert_not_found_error
from helpers.generator import register_new_courier_and_return_login_password


class TestDeleteCourier:
    """Тесты для удаления курьера"""
    
    @pytest.mark.courier
    def test_delete_courier_success(self, api_client):
        """Проверка успешного удаления курьера"""
        # Создаём курьера для теста
        courier_data = register_new_courier_and_return_login_password()
        assert len(courier_data) == 3, "Курьер не был создан"
        
        login = courier_data[0]
        password = courier_data[1]
        
        # Получаем ID курьера
        login_response = api_client.login_courier(login, password)
        assert login_response.status_code == 200
        courier_id = login_response.json()["id"]
        
        # Удаляем курьера
        response = api_client.delete_courier(courier_id)
        
        assert response.status_code == 200
        assert response.json() == {"ok": True}
    
    @pytest.mark.courier
    def test_delete_courier_without_id(self, api_client):
        """Проверка удаления курьера без ID"""
        response = api_client.delete_courier("")
        
        assert response.status_code in [400, 404]
    
    @pytest.mark.courier
    def test_delete_nonexistent_courier(self, api_client):
        """Проверка удаления несуществующего курьера"""
        fake_id = 999999999
        response = api_client.delete_courier(fake_id)
        
        assert response.status_code == 404
        assert_not_found_error(response, "курьер")
