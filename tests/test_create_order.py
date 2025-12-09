import pytest


class TestCreateOrder:
    """Тесты для создания заказа"""
    
    @pytest.mark.order
    @pytest.mark.parametrize("color", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        None
    ])
    def test_create_order_with_different_colors(self, api_client, order_data, color):
        """Проверка создания заказа с разными цветами (BLACK, GREY, оба, без цвета)"""
        response = api_client.create_order(
            first_name=order_data["first_name"],
            last_name=order_data["last_name"],
            address=order_data["address"],
            metro_station=order_data["metro_station"],
            phone=order_data["phone"],
            rent_time=order_data["rent_time"],
            delivery_date=order_data["delivery_date"],
            comment=order_data["comment"],
            color=color
        )
        
        assert response.status_code == 201
        response_body = response.json()
        assert "track" in response_body
        assert isinstance(response_body["track"], int)
        assert response_body["track"] > 0
