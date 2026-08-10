import logging
import os

# Создаём папку logs, если её нет
LOG_DIR = 'logs'
os.makedirs(LOG_DIR, exist_ok=True)

# Настраиваем логгер для этого модуля
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Обработчик для записи в файл (перезапись при каждом запуске)
log_file = os.path.join(LOG_DIR, f'{__name__}.log')
file_handler = logging.FileHandler(log_file, mode='w', encoding='utf-8')
file_handler.setLevel(logging.INFO)

# Формат: время - имя модуля - уровень - сообщение
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)



def get_mask_card_number(card_number: str) -> str:
    logger.info(f"Маскировка номера карты: {card_number[:4]}...")
    if not card_number or len(card_number) != 16:
        logger.error("Неверный номер карты (длина != 16 или пустой)")
        return "Неверный номер карты"
    result = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    logger.info(f"Результат маскировки карты: {result}")
    return result

def get_mask_account(account_number: str) -> str:
    logger.info(f"Маскировка номера счёта: ...{account_number[-4:] if account_number else ''}")
    if not account_number or len(account_number) < 4:
        logger.error("Неверный номер счёта (меньше 4 символов или пустой)")
        return "Неверный номер счета"
    result = f"**{account_number[-4:]}"
    logger.info(f"Результат маскировки счёта: {result}")
    return result
