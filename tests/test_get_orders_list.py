import pytest


class TestGetOrdersList:
    """Тесты для получения списка заказов"""
    
    @pytest.mark.order
    def test_get_orders_list_returns_list(self, api_client):
        """Проверка, что в тело ответа возвращается список заказов"""
        response = api_client.get_orders_list()
        
        assert response.status_code == 200
        response_body = response.json()
        assert isinstance(response_body, dict)
        assert "orders" in response_body
        assert isinstance(response_body["orders"], list)
