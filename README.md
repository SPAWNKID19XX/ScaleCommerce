# ScaleCommerce
# High-Load Marketplace Engine (DRF)

Этот проект представляет собой высоконагруженный движок маркетплейса с системой динамического ценообразования и асинхронной обработкой заказов.

---

## 🌍 Language / Язык
- [English Description](#english-version)
- [Описание на русском](#russian-version)

---

<a name="english-version"></a>
## 🇺🇸 English Version

### Project Overview
A scalable backend for an e-commerce platform designed with a focus on performance, asynchronous tasks, and complex business logic.

### 🛠 Tech Stack
*   **Framework:** Django REST Framework (DRF)
*   **Async Processing:** Celery + Redis
*   **Database:** PostgreSQL + Redis (Caching)
*   **Search:** PostgreSQL Full-text search
*   **Testing:** Pytest
*   **DevOps:** Docker & Docker Compose

### 🚀 Key Features
1.  **Dynamic Pricing Engine:** Automatic price adjustments based on demand and conversion rates via Celery Beat.
2.  **Asynchronous Order Management:** Non-blocking order processing with background stock validation.
3.  **Performance Optimization:** Solved N+1 problems, implemented caching for hot data, and Service Layer pattern.
4.  **Advanced Filtering:** Complex search and filtering systems.

## How to run
### Installation and Setup 

Follow these steps to get the project up and running:

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd ScaleCommerce

2. **Apply migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate

3. **Create a superuser:**
   ```bash
   python manage.py createsuperuser

---
# Test Data Generation
If you need to populate the database with random data, use the following custom management commands:

1. **Create 10 test users:**
   ```bash
   python manage.py new_users
All generated users have the password: admin

2. **Create 500 test products:**
   ```bash
   python manage.py new_products

3. **Create 5000 test orders:**
   ```bash
   python manage.py new_orders


4. **Create  test order_items for each of order:**
   ```bash
   python manage.py new_order_item
   
# 🚀 Vortex Marketplace API Documentation (v1.0)

- **BASE URL**: http://localhost:8000/
- **Data Format**: JSON
- **Authentication**: JWT (Bearer Token)

## 🔐 1. Authentication (Users)

| Метод | Эндпоинт                                  | Описание                              |
| :--- |:------------------------------------------|:--------------------------------------|
| GET  | users/api/v1/                             | Users list(just for admin).           |
| POST | users/api/v1/sign-up/                     | SignUp new user                       |
| POST | users/api/v1/token/                       | Login (get Access and Refresh tokens) |
| POST | users/api/v1/token/refresh/               | Refresh Access token                  |
| POST | users/api/v1/token/verify/                | Validation token                      |

## 📦 2. Products (Products)
### 📦 Product Management (Products)

| Method | Endpoint                | Description                      | Access                   |
| :--- |:------------------------|:------------------------------|:-------------------------|
| **GET** | `products/api/v1/`      | Activ products list (filtred) | AlowAny                  |
| **POST** | `products/api/v1/`      | Create ne product             | Just authenticated users |
| **GET** | `products/api/v1/{id}/` | Product detail (count_viewed) | AlowAny                  |
| **PUT/PATCH** | `products/api/v1/{id}/` | Update product                | Owner                    |
| **DELETE** | `products/api/v1/{id}/` | Delete product                | Owner                    |

### Peculiarities of POST requests:
When creating a product, you need to pass the category_id. The seller field will be filled in automatically.
```json
{
        "id": 1,
        "name": "article",
        "brand": "leave",
        "price": "6.21",
        "description": "And north ago least memory bed individual.",
        "category": {
            "id": 9,
            "name": "beauty_health"
        },
        "seller": {
            "first_name": "Kara",
            "last_name": "Sexton",
            "email": "matthewwade@example.com"
        },
        "stock": 87,
        "is_active": true,
        "created_at": "2026-01-20T22:20:27.552966Z",
        "count_viewed": 0
    }
```
## 🛒 3. Orders (Orders)

| Method | Endpoint                | Description                      | Access |
| :--- |:-----------------| :--- | :--- |
| **GET** | `orders/api/v1/` | Current user's order history | Logged in |
| **POST** | `orders/api/v1/` | **Create an Order** (Atomic Transaction) | Logged in |

### Order creation format (Nested JSON):
When creating an order, you must provide a list of products and their quantity.

```json
{
  "order_item": [
    {
      "product": 1, 
      "quantity": 2
    },
    {
      "product": 5, 
      "quantity": 1
    }
  ]
}
```

## 📊 4. Analytics (Seller Dashboard)
| Method | Endpoint                | Description                      | Access        |
| :--- |:--------------------------------| :--- |:--------------|
| **GET** | `products/api/v1/seller-stats/` | Statistics: revenue, views, top products | Authenticated |
```json

{
    "total_views": 438,
    "avg_views": 0.2255406797116375,
    "total_products": 1942,
    "totat_sold": 492013.34
}
```

## 🛠 Backend technical features (for interviews):
1. Race Condition Protection: Product write-offs are protected via select_for_update.
2. Database Optimization: All lists use select_related and prefetch_related (N+1 issue resolved).
3. High-load ready: Bulk operations are performed via bulk_create and bulk_update.
4. Price Consistency: Price history is saved automatically when the price field is changed.

---

<a name="russian-version"></a>
## 🇷🇺 Russian Version

### Описание проекта
Масштабируемый backend для маркетплейса, разработанный с акцентом на производительность, асинхронность и сложную бизнес-логику.

### 🛠 Технологический стек
*   **Фреймворк:** Django REST Framework (DRF)
*   **Фоновые задачи:** Celery + Redis
*   **База данных:** PostgreSQL + Redis (Кэширование)
*   **Поиск:** Полнотекстовый поиск PostgreSQL
*   **Тестирование:** Pytest
*   **DevOps:** Docker и Docker Compose

### 🚀 Основной функционал
1.  **Движок динамических цен:** Автоматическое изменение стоимости товаров в зависимости от спроса через Celery Beat.
2.  **Асинхронные заказы:** Неблокирующая архитектура создания заказов с фоновой проверкой склада.
3.  **Оптимизация производительности:** Решение проблемы N+1, кэширование популярных данных и паттерн Service Layer.
4.  **Продвинутая фильтрация:** Сложные системы поиска и фильтрации товаров.

---

##  Как запустить
### Инструкция по запуску


Выполните следующие шаги для установки и запуска проекта:

1. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com/SPAWNKID19XX/ScaleCommerce.git
   cd ScaleCommerce

2. **Выполните миграции:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate

3. **Создайте администратора:**
   ```bash
   python manage.py createsuperuser

---
# Наполнение тестовыми данными
Если вам нужно заполнить базу данных тестовыми данными, воспользуйтесь следующими командами:
1. **Создать 10 пользователей:**
   ```bash
   python manage.py new_users
У всех созданных пользователей пароль: admin

2. **Создать 500 товаров:**
   ```bash
   python manage.py new_products
   
3. **Создать 5000 заказов:**
   ```bash
   python manage.py new_orders


4. **Создать  order_items для каждого заказа:**
   ```bash
   python manage.py new_order_item
   

# 🚀 Vortex Marketplace API Documentation (v1.0)

- **Базовый URL**: http://localhost:8000/
- **Формат данных**: JSON
- **Авторизация**: JWT (Bearer Token)

## 🔐 1. Аутентификация (Users)

| Метод | Эндпоинт                                  | Описание                                   |
| :--- |:------------------------------------------|:-------------------------------------------|
| GET  | users/api/v1/                             | Список пользователей(админ).               |
| POST | users/api/v1/sign-up/                     | Регистрация нового пользователя            |
| POST | users/api/v1/token/                       | Логин (получение Access и Refresh токенов) |
| POST | users/api/v1/token/refresh/               | Обновление Access токена                   |
| POST | users/api/v1/token/verify/                | Проверка валидности токена                 |

## 📦 2. Товары (Products)
### 📦 Управление товарами (Products)

| Метод | Эндпоинт                | Описание | Доступ |
| :--- |:------------------------| :--- | :--- |
| **GET** | `products/api/v1/`      | Список активных товаров (с фильтрацией) | Всем |
| **POST** | `products/api/v1/`      | Создание нового товара | Только Seller |
| **GET** | `products/api/v1/{id}/` | Детали товара (+1 к просмотру) | Всем |
| **PUT/PATCH** | `products/api/v1/{id}/` | Редактирование товара | Только Владелец |
| **DELETE** | `products/api/v1/{id}/` | Удаление товара | Только Владелец |

### Особенность POST запроса:
При создании товара нужно передавать category_id. Поле seller заполнится автоматически.
```json
{
  "name": "iPhone 15",
  "category_id": 5,
  "price": "999.00",
  "stock": 10
}
```
## 🛒 3. Заказы (Orders)

| Метод | Эндпоинт         | Описание | Доступ |
| :--- |:-----------------| :--- | :--- |
| **GET** | `orders/api/v1/` | История заказов текущего пользователя | Авторизован |
| **POST** | `orders/api/v1/` | **Создание заказа** (Атомарная транзакция) | Авторизован |

### Формат создания заказа (Nested JSON):
При создании заказа необходимо передать список товаров и их количество.

```json
{
  "order_item": [
    {
      "product": 1, 
      "quantity": 2
    },
    {
      "product": 5, 
      "quantity": 1
    }
  ]
}
```

## 📊 4. Аналитика (Seller Dashboard)
| Метод | Эндпоинт                        | Описание | Доступ |
| :--- |:--------------------------------| :--- | :--- |
| **GET** | `products/api/v1/seller-stats/` | Статистика: выручка, просмотры, топ-товары | Только Seller |
```json

{
  "total_products": 142,
  "total_views": 8540,
  "avg_views": 60.1,
  "total_revenue": "1250450.50"
}
```

## 🛠 Технические особенности бэкенда (для собеседований):
1. Race Condition Protection: Списание товара защищено через select_for_update.
2. Database Optimization: Все списки используют select_related и prefetch_related (решена проблема N+1).
3. High-load ready: Массовые операции выполняются через bulk_create и bulk_update.
4. Price Consistency: История цен сохраняется автоматически при изменении поля price.
