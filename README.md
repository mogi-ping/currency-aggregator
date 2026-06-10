Учебный проект по конкурентному программированию на Python.

## Используемые технологии

- asyncio
- aiohttp
- ProcessPoolExecutor
- ThreadPoolExecutor
- SQLite
- numpy

## Архитектура

Этап 1 — сбор данных через asyncio и aiohttp.

Этап 2 — обработка данных в ProcessPoolExecutor.

Этап 3 — сохранение результатов в SQLite через ThreadPoolExecutor.

Для передачи данных используются:

- asyncio.Queue
- multiprocessing.Queue

## Установка

```bash
pip install -r requirements.txt
```

## Запуск

```bash
python main.py
```

## База данных

Создаётся файл:

```text
currency_data.db
```

Таблица:

```sql
rates(
    id,
    timestamp,
    currency_pair,
    average_rate,
    std_dev,
    source
)
```

## Проверка

Запуск бенчмарка:

```bash
python benchmark.py
```

Проверка количества записей:

```python
import sqlite3

conn = sqlite3.connect("currency_data.db")
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM rates")
print(cursor.fetchone())
```