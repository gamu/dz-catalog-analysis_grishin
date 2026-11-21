# Анализ каталога фильмов

Домашнее задание по Python: набор функций для анализа небольшого каталога фильмов. Каждый этап отрабатывает отдельную тему языка, а итоговая функция `build_report` собирает результаты в консольный отчет.

## Требования

- [uv](https://docs.astral.sh/uv/)
- Python 3.12+ (uv сам установит нужную версию по файлу `.python-version`)

## Запуск

```bash
uv run catalog_analysis.py
```

Сначала выводится итоговый отчет по каталогу, затем демонстрации циклов (этап 3) и генераторов (этап 8).

## Проверка стиля

```bash
uv run ruff check .
```

## Что реализовано

| Этап | Тема | Функции |
|---|---|---|
| 1 | Числа и `math` | `average_rating`, `catalog_age_stats`, `duration_in_hours` |
| 2 | Условия и `match` | `rating_tier`, `decade_label` |
| 3 | Циклы | `print_non_comedies`, `find_first_masterpiece`, `count_long_movies` |
| 4 | Строки | `normalize_title`, `make_slug`, `format_report_line` |
| 5 | Списки | `titles_sorted_by_rating`, `top_n_by_rating` |
| 6 | Словари | `count_by_genre`, `actor_filmography`, `movies_above_average` |
| 7 | Множества | `all_genres`, `common_actors`, `genres_only_in_one` |
| 8 | Итераторы и генераторы | `iter_high_rated`, `print_high_rated`, `total_duration_high_rated` |
| 9 | Итоговый отчет | `build_report` |

## Структура

```
├── catalog_analysis.py   # данные каталога и все функции
├── pyproject.toml        # настройки проекта и ruff
├── uv.lock               # зафиксированные версии зависимостей
├── .python-version       # версия Python для uv
├── README.md
└── .gitignore
```
