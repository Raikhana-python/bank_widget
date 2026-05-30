from src.masks import get_mask_card_number, get_mask_account
from datetime import datetime

def mask_account_card(card_info: str) -> str:
    if not card_info or not isinstance(card_info, str):
        return "Ошибка: пустая строка или неверный тип данных"
    
    parts = card_info.split()
    
    if len(parts) < 2:
        return "Ошибка: некорректный формат ввода"
    
    number = parts[-1]
    
    if not number.isdigit():
        return "Ошибка: номер должен содержать только цифры"
    
    if len(number) == 16:
        masked_number = get_mask_card_number(number)
    elif len(number) == 20:
        masked_number = get_mask_account(number)
    else:
        return f"Ошибка: номер должен содержать 16 или 20 цифр (получено {len(number)})"
    
    return ' '.join(parts[:-1] + [masked_number])

def get_date(date_string: str) -> str:
    if not date_string or not isinstance(date_string, str):
        return "Ошибка: пустая строка или неверный тип данных"
    
    try:
        date_obj = datetime.fromisoformat(date_string)
        return date_obj.strftime("%d.%m.%Y")
    except ValueError:
        return "Ошибка: некорректный формат даты"
