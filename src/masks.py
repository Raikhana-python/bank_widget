def mask_card_number(number: str) -> str:
    return f"{number[:4]} {number[4:6]}** **** {number[-4:]}"

def mask_account_number(number: str) -> str:
    return f"**{number[-4:]}"
