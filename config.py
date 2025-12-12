"""Конфигурация проекта"""

BASE_URL = "https://qa-scooter.praktikum-services.ru"

ENDPOINTS = {
    "courier": "/api/v1/courier",
    "courier_login": "/api/v1/courier/login",
    "courier_delete": "/api/v1/courier/{courier_id}",
    "orders": "/api/v1/orders",
    "orders_accept": "/api/v1/orders/accept/{order_id}",
    "orders_track": "/api/v1/orders/track"
}

