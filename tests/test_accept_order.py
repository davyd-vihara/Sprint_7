import pytest

from helpers.assertions import assert_insufficient_data_error, assert_courier_not_exists_error, assert_order_not_exists_error


class TestAcceptOrder:
    """Тесты для принятия заказа"""
    
    @pytest.mark.order
    def test_accept_order_success(self, api_client, created_courier, created_order):
        """Проверка успешного принятия заказа"""
        courier_id = created_courier["id"]
        order_id = created_order["order_id"]
        
        accept_response = api_client.accept_order(order_id, courier_id)
        
        assert accept_response.status_code == 200
        assert accept_response.json() == {"ok": True}
    
    @pytest.mark.order
    def test_accept_order_without_courier_id(self, api_client, created_order):
        """Проверка принятия заказа без ID курьера"""
        order_id = created_order["order_id"]
        
        response = api_client.accept_order(order_id, "")
        
        assert response.status_code == 400
        assert_insufficient_data_error(response)
    
    @pytest.mark.order
    def test_accept_order_with_wrong_courier_id(self, api_client, created_order):
        """Проверка принятия заказа с неверным ID курьера"""
        order_id = created_order["order_id"]
        fake_courier_id = 999999999
        
        response = api_client.accept_order(order_id, fake_courier_id)
        
        assert response.status_code == 404
        assert_courier_not_exists_error(response)
    
    @pytest.mark.order
    def test_accept_order_without_order_id(self, api_client, created_courier):
        """Проверка принятия заказа без ID заказа"""
        courier_id = created_courier["id"]
        
        response = api_client.accept_order("", courier_id)
        
        assert response.status_code in [400, 404]
    
    @pytest.mark.order
    def test_accept_order_with_wrong_order_id(self, api_client, created_courier):
        """Проверка принятия заказа с неверным ID заказа"""
        courier_id = created_courier["id"]
        fake_order_id = 999999999
        
        response = api_client.accept_order(fake_order_id, courier_id)
        
        assert response.status_code == 404
        assert_order_not_exists_error(response)
