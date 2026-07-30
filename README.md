- `mask_account_card()`
- `get_date()`
```python
from src.widget import mask_account_card, get_date

print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Счет 73654108430135874305"))
print(get_date("2024-03-11T02:26:18.671407"))
### Генераторы для работы с транзакциями

```python
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

# Фильтрация по валюте (возвращает итератор)
transactions = [
    {'id': 1, 'operationAmount': {'currency': {'code': 'USD'}}},
    {'id': 2, 'operationAmount': {'currency': {'code': 'EUR'}}},
    {'id': 3, 'operationAmount': {'currency': {'code': 'USD'}}},
]

for transaction in filter_by_currency(transactions, 'USD'):
    print(transaction['id'])  # 1, 3

# Описания транзакций
descriptions = transaction_descriptions(transactions)
for desc in descriptions:
    print(desc)

# Генерация номеров карт
for card in card_number_generator(1, 5):
    print(card)
# 0000 0000 0000 0001
# 0000 0000 0000 0002
# ...
