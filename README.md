# Sprint_7 - Тестирование API Яндекс Самокат

Проект для тестирования API учебного сервиса Яндекс Самокат.

## Документация API
https://qa-scooter.praktikum-services.ru/docs/

## Установка

### Быстрая установка (рекомендуется)

Выполните в PowerShell:
```powershell
.\setup.ps1
```

Если возникает ошибка выполнения скриптов, сначала выполните:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Ручная установка

1. Создайте виртуальное окружение:
```powershell
python -m venv venv
```

2. Активируйте виртуальное окружение:
```powershell
# Windows PowerShell
.\venv\Scripts\Activate.ps1

# Если возникает ошибка выполнения скриптов, выполните:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
# Затем снова активируйте окружение:
.\venv\Scripts\Activate.ps1

# Альтернатива для Windows CMD:
# venv\Scripts\activate.bat
```

3. Установите зависимости:
```powershell
pip install -r requirements.txt
```

**Примечание:** После активации виртуального окружения в начале строки PowerShell должно появиться `(venv)`.

## Запуск тестов

**Важно:** Убедитесь, что виртуальное окружение активировано (должно быть `(venv)` в начале строки).

```powershell
# Запуск всех тестов
pytest

# Запуск с подробным выводом
pytest -v

# Запуск конкретного теста
pytest tests/test_create_courier.py

# Запуск конкретного класса тестов
pytest tests/test_create_courier.py::TestCreateCourier
```

## Генерация Allure отчёта

```bash
# Запуск тестов с генерацией Allure результатов
pytest --alluredir=target/allure-results

# Генерация HTML отчёта
allure generate target/allure-results -o target/allure-report --clean

# Открытие отчёта в браузере
allure open target/allure-report
```

## Отправка Allure отчёта в репозиторий

Для отправки результатов Allure в репозиторий выполните:

```bash
# Добавляем папку с результатами Allure
git add -f target/allure-results/

# Коммитим
git commit -m "add allure report"

# Отправляем в удалённый репозиторий
git push
```