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

