import pytest

from helpers.assertions import assert_insufficient_data_error, assert_not_found_error


class TestGetOrderByTrack:
    """Тесты для получения заказа по номеру"""
    
    @pytest.mark.order
    def test_get_order_by_track_success(self, api_client, created_order):
        """Проверка успешного получения заказа по номеру"""
        track = created_order["track"]
        
        get_response = api_client.get_order_by_track(track)
        
        assert get_response.status_code == 200
        response_body = get_response.json()
        assert "order" in response_body
        assert isinstance(response_body["order"], dict)
        assert response_body["order"]["track"] == track
    
    @pytest.mark.order
    def test_get_order_by_track_without_track(self, api_client):
        """Проверка получения заказа без номера"""
        response = api_client.get_order_by_track("")
        
        assert response.status_code == 400
        assert_insufficient_data_error(response)
    
    @pytest.mark.order
    def test_get_order_by_nonexistent_track(self, api_client):
        """Проверка получения заказа с несуществующим номером"""
        fake_track = 999999999
        response = api_client.get_order_by_track(fake_track)
        
        assert response.status_code == 404
        assert_not_found_error(response, "заказ")
