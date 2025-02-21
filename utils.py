import json
from json_db_lite import JSONDatabase

# Инициализирует объект
small_db = JSONDatabase(file_path='users.json')

# Получает записи с JSON файла
def jsondb_to_dict_list():
    return small_db.get_all_records()

# Добавляет пользователя
def add_user(user: dict):
    small_db.add_records(user)
    return True

# Обновляет данные по пользователю
def upd_user(upd_filter: dict, new_data: dict):
    small_db.update_record_by_key(upd_filter, new_data)
    return True

# Удаляет пользователя
def delete_user(key: str, value: str):
    small_db.delete_record_by_key(key, value)
    return True

def dict_list_to_json(dict_list, filename):
    """
    Преобразует список словарей в JSON-строку и сохраняет её в файл.

    :param dict_list: Список словарей
    :param filename: Имя файла для сохранения JSON-строки
    :return: JSON-строка или None в случае ошибки
    """
    try:
        json_str = json.dumps(dict_list, ensure_ascii=False)
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(json_str)
        return json_str
    except (TypeError, ValueError, IOError) as e:
        print(f"Ошибка при преобразовании списка словарей в JSON или записи в файл: {e}")
        return None

def json_to_dict_list(filename):
    """
    Преобразует JSON-строку из файла в список словарей.

    :param filename: Имя файла с JSON-строкой
    :return: Список словарей или None в случае ошибки
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            json_str = file.read()
            dict_list = json.loads(json_str)
        return dict_list
    except (TypeError, ValueError, IOError) as e:
        print(f"Ошибка при чтении JSON из файла или преобразовании в список словарей: {e}")
        return None

