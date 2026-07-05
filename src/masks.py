def get_mask_card_number(card_number: str) -> str:
    """
    Возвращает маску карты в формате XXXX XX** **** XXXX
    Пример: 7000792289606361 -> 7000 79** **** 6361
    """
    if not card_number or len(card_number) != 16:
        return "Неверный номер карты"
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """
    Возвращает маску счета в формате **XXXX
    Пример: 73654108430135874305 -> **4305
    """
    if not account_number or len(account_number) < 4:
        return "Неверный номер счета"
    return f"**{account_number[-4:]}"
