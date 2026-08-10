import logging
import os

# Создаём папку logs, если её нет
LOG_DIR = 'logs'
os.makedirs(LOG_DIR, exist_ok=True)

# Настраиваем логгер для этого модуля
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Обработчик для записи в файл (режим 'w' — перезапись при каждом запуске)
log_file = os.path.join(LOG_DIR, f'{__name__}.log')
file_handler = logging.FileHandler(log_file, mode='w', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)

# Формат: время - имя модуля - уровень - сообщение
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)



"""Утилиты для работы с данными транзакций."""

def read_transactions_from_json(file_path: str) -> List[Dict[str, Any]]:
    logger.info(f"Чтение файла: {file_path}")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, list):
            logger.info(f"Успешно загружено {len(data)} транзакций")
            return data
        else:
            logger.warning("Файл содержит не список, возвращаем пустой список")
            return []
    except FileNotFoundError:
        logger.error(f"Файл не найден: {file_path}")
        return []
    except json.JSONDecodeError as e:
        logger.error(f"Ошибка парсинга JSON: {e}")
        return []
    except Exception as e:
        logger.error(f"Неизвестная ошибка: {e}")
        return []
