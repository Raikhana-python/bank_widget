- `mask_account_card()`
- `get_date()`
```python
from src.widget import mask_account_card, get_date

print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Счет 73654108430135874305"))
print(get_date("2024-03-11T02:26:18.671407"))

## Тестирование

### Запуск тестов

```bash
# Установка зависимостей для тестирования
pip install pytest pytest-cov

# Запуск всех тестов
pytest tests/ -v

# Запуск тестов с проверкой покрытия
pytest tests/ --cov=src --cov-report=html

# Просмотр отчёта о покрытии (Mac)
open htmlcov/index.html
