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

## How to run / Как запустить
1. `git clone https://github.com`
2. `docker-compose up --build`