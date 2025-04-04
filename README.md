# AccessPoint API

## Запуск проекта

### 1. Требования
- Docker
- Docker Compose

### 2. Быстрый старт
```bash
# Собрать и запустить контейнеры
docker-compose up --build

# Остановить (когда нужно завершить работу)
docker-compose down





# Запустить тесты
docker-compose exec app pytest accounts/tests.py -v

# Пример тестового запроса
curl -X POST http://localhost:8000/register/client/ \
  -H "Content-Type: application/json" \
  -d '{
    "login": "test_user",
    "password_hash": "Passw0rd!",
    "email": "test@example.com",
    "first_name": "Test",
    "last_name": "User",
    "phone": "+1234567890"
  }'




# Просмотр логов
docker-compose logs app

# Очистка (если возникают проблемы)
docker-compose down -v
sudo fuser -k 8000/tcp