# Диаграмма последовательности: Создание заказа и подбор курьера

```mermaid
sequenceDiagram
    autonumber
    actor Customer as Клиент (Магазин)
    participant API as API Gateway
    participant DeliverySys as Сервис Доставки
    participant GeoSys as Гео-Сервис (Карты)
    participant DB as База Данных

    Customer->>API: POST /api/v1/deliveries (Данные заказа)
    API->>DeliverySys: Валидация и передача запроса
    
    critical Расчет геокоординат и дистанции
        DeliverySys->>GeoSys: Запрос координат адресов (Геокодирование)
        GeoSys-->>DeliverySys: Координаты (Широта/Долгота)
        DeliverySys->>GeoSys: Расчет оптимального маршрута и матрицы расстояний
        GeoSys-->>DeliverySys: Дистанция (км) и время (мин)
    end

    DeliverySys->>DeliverySys: Расчет стоимости по тарификатору
    DeliverySys->>DB: Сохранение заказа (Статус: Created)
    DB-->>DeliverySys: ID заказа сохранен
    
    DeliverySys->>DB: Поиск ближайших свободных курьеров в радиусе 3 км
    DB-->>DeliverySys: Список подходящих курьеров
    
    DeliverySys-->>Customer: Ответ 201 Created (ID, Стоимость, Ссылка на трекинг)
```

# Sequence Diagram — автоматическое переназначение заказа

```mermaid
sequenceDiagram
    participant K1 as Курьер 1
    participant K2 as Курьер 2
    participant S as Система
    participant O as Оператор

    K1->>S: Отмечает "В пути"
    S->>S: Запускает таймер критического времени

    alt Время истекло
        S->>S: Ищет свободного курьера в радиусе 3 км
        alt Свободный курьер найден
            S->>K2: Предложение взять заказ
            K2->>S: Принимает заказ
            S->>K1: Уведомление об отмене (время истекло)
            S->>O: Уведомление о переназначении
            S->>K2: Детали заказа и маршрут
        else Свободный курьер не найден
            S->>O: Эскалация: заказ рискует остыть
            S->>K1: Уведомление: "Поторопитесь!"
        end
    else Время в норме
        S->>K1: Статус: "В пути"
    end
