import pytest
import allure

from helpers.assertions import assert_courier_not_found_error
from helpers.generator import register_new_courier_and_return_login_password


class TestDeleteCourier:
    """Тесты для удаления курьера"""
    
    @pytest.mark.courier
    @allure.title("Успешное удаление курьера")
    @allure.description("Проверка успешного удаления курьера")
    def test_delete_courier_success(self, api_client):
        """Проверка успешного удаления курьера"""
        with allure.step("Создать курьера для теста"):
            courier_data = register_new_courier_and_return_login_password()
            assert len(courier_data) == 3, "Курьер не был создан"
            login = courier_data[0]
            password = courier_data[1]
        
        with allure.step("Получить ID курьера"):
            login_response = api_client.login_courier(login, password)
            courier_id = login_response.json()["id"]
        
        with allure.step("Удалить курьера"):
            response = api_client.delete_courier(courier_id)
        
        with allure.step("Проверить успешное удаление"):
            assert response.status_code == 200
            assert response.json() == {"ok": True}
    
    @pytest.mark.courier
    @allure.title("Удаление курьера с пустым ID")
    @allure.description("Проверка удаления курьера с пустым ID, ожидается статус 404")
    def test_delete_courier_with_empty_id(self, api_client):
        """Проверка удаления курьера с пустым ID, ожидается статус 404"""
        with allure.step("Попытаться удалить курьера с пустым ID"):
            response = api_client.delete_courier("")
        
        with allure.step("Проверить ошибку 404"):
            assert response.status_code == 404
    
    @pytest.mark.courier
    @allure.title("Удаление несуществующего курьера")
    @allure.description("Проверка удаления несуществующего курьера")
    def test_delete_nonexistent_courier(self, api_client):
        """Проверка удаления несуществующего курьера"""
        with allure.step("Попытаться удалить несуществующего курьера"):
            fake_id = 999999999
            response = api_client.delete_courier(fake_id)
        
        with allure.step("Проверить ошибку не найденного курьера"):
            assert response.status_code == 404
            assert_courier_not_found_error(response)
