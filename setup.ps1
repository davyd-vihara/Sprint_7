# Скрипт для настройки проекта Sprint_7

Write-Host "Создание виртуального окружения..." -ForegroundColor Green
python -m venv venv

Write-Host "Активация виртуального окружения..." -ForegroundColor Green
& .\venv\Scripts\Activate.ps1

Write-Host "Установка зависимостей..." -ForegroundColor Green
pip install --upgrade pip
pip install -r requirements.txt

Write-Host "`nГотово! Виртуальное окружение активировано." -ForegroundColor Green
Write-Host "Теперь вы можете запустить тесты командой: pytest" -ForegroundColor Yellow

