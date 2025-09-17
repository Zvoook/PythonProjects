

# 🐍 Руководство по pip и Poetry для VS Code

Этот документ поможет вам быстро переключаться между `pip` и `poetry`, а также правильно настроить современный Python-проект с помощью `pyproject.toml`.

---

## 🔄 Аналоги команд `pip` в `poetry`

| Задача | Команда `pip` | Команда `poetry` | Примечания |
|--------|---------------|------------------|------------|
| **Установить пакет** | `pip install requests` | `poetry add requests` | Добавляет пакет в `pyproject.toml` и `poetry.lock`, затем устанавливает его. |
| **Установить пакет для разработки** | `pip install pytest` | `poetry add --group dev pytest` | Добавляет пакет в группу `[tool.poetry.group.dev.dependencies]`. |
| **Установить все зависимости** | `pip install -r requirements.txt` | `poetry install` | Устанавливает зависимости из `pyproject.toml` + `poetry.lock`. |
| **Обновить пакет** | `pip install --upgrade requests` | `poetry update requests` | Обновляет пакет до последней версии в рамках ограничений. |
| **Обновить все пакеты** | `pip list --outdated` + ручное обновление | `poetry update` | Обновляет **все** пакеты. |
| **Удалить пакет** | `pip uninstall requests` | `poetry remove requests` | Удаляет пакет из проекта и `pyproject.toml`. |
| **Активировать окружение** | `source venv/bin/activate` | `poetry shell` | Создает и активирует виртуальное окружение. |
| **Показать зависимости** | `pip list` | `poetry show` | Показывает дерево зависимостей. |
| **Экспортировать в requirements.txt** | — | `poetry export -f requirements.txt -o requirements.txt` | Для деплоя на платформы без Poetry. |
| **Инициализировать проект** | — | `poetry init` | Создает интерактивно `pyproject.toml`. |
| **Запустить скрипт** | `python script.py` (в активированном окружении) | `poetry run python script.py` | Запускает команду в контексте окружения Poetry. |
| **Установить проект в режиме разработки** | `pip install -e .` | `poetry install` | Устанавливает текущий проект как "editable". |
| **Проверить устаревшие пакеты** | `pip list --outdated` | `poetry show --outdated` | Показывает, какие пакеты можно обновить. |

---

## 💡 Полезные советы по Poetry

### 1. Добавление пакетов с версией

```bash
poetry add requests@^2.28.0
poetry add "django>=4.0,<5.0"
```

### 2. Добавление пакетов для разработки

```bash
poetry add --group dev black isort flake8 pytest
```

В `pyproject.toml` создастся:

```toml
[tool.poetry.group.dev.dependencies]
black = "^24.0"
isort = "^5.13"
pytest = "^8.0"
```

### 3. Запуск скриптов без активации окружения

```bash
poetry run python your_script.py
poetry run pytest tests/
poetry run black .
```

### 4. Обновление lock-файла после ручного изменения `pyproject.toml`

```bash
poetry lock --no-update  # Обновляет lock без изменения версий
poetry install           # Устанавливает согласно обновленному lock
```

---

## 📄 Пример файла `pyproject.toml` (современный формат)

```toml
[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[project]
name = "my-awesome-project"
version = "0.1.0"
description = "A short description of your project."
authors = [
    { name = "Your Name", email = "you@example.com" },
]
requires-python = ">=3.8"
dependencies = [
    "requests>=2.25.0",
]

[project.optional-dependencies]
dev = [
    "black",
    "isort",
    "flake8",
    "pytest",
]

[project.urls]
Homepage = "https://github.com/yourname/my-awesome-project"
Repository = "https://github.com/yourname/my-awesome-project"
"Bug Tracker" = "https://github.com/yourname/my-awesome-project/issues"

[project.scripts]
myapp = "myapp:main"

[tool.poetry.group.dev.dependencies]
black = "^24.0"
isort = "^5.13"
flake8 = "^7.0"
pytest = "^8.0"

[tool.black]
line-length = 88
target-version = ['py38']

[tool.isort]
profile = "black"
line_length = 88

[tool.flake8]
max-line-length = 88
extend-ignore = ["E203", "W503"]
```

> **Примечание:** Начиная с Poetry 2.0, рекомендуется использовать таблицу `[project]` вместо `[tool.poetry]` для совместимости со стандартами. Однако текущая стабильная версия Poetry (1.x) всё ещё использует `[tool.poetry]`. Вы можете использовать оба формата.

---

## ✅ Почему Poetry лучше pip + requirements.txt?

- **Автоматическое управление версиями:** Создает `poetry.lock` для детерминированной сборки.
- **Группы зависимостей:** Четкое разделение на `main`, `dev`, `test`.
- **Встроенное управление виртуальными окружениями.**
- **Поддержка современного стандарта `pyproject.toml`.**

---

## 🧹 Очистка кешей (на всякий случай)

### Poetry кеш

```bash
# Показать кеш
poetry cache list

# Очистить кеш для PyPI
poetry cache clear pypi --all
```

### Pre-commit кеш (если используете)

```bash
pre-commit clean
```

---

Скопируйте этот документ в файл `README.md` или `GUIDE.md` в корне вашего проекта — и вы всегда будете иметь под рукой всю необходимую информацию!

Удачи в разработке! 🚀
