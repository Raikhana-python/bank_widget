from src.masks import mask_card_number, mask_account_number

def mask_account_card(card_info: str) -> str:
    parts = card_info.split()
    number = parts[-1]
    if len(number) == 16:
        masked = mask_card_number(number)
        return ' '.join(parts[:-1] + [masked])
    elif len(number) == 20:
        masked = mask_account_number(number)
        return ' '.join(parts[:-1] + [masked])
    return card_info

def get_date(date_string: str) -> str:
    date_part = date_string.split('T')[0]
    year, month, day = date_part.split('-')
    return f"{day}.{month}.{year}"
