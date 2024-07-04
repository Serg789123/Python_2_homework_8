__all__ = ['set_users']

import json
from pathlib import Path

def set_users(file: Path) -> None:
    u_isd = set()
    if not file.is_file(): # если файла ещё не существует
        data = {str(i): {} for i in range(1, 7+1)} # генератор словаря
    else:
        with open(file, 'r', encoding='UTF-8') as f_read:
            data = json.load(f_read)
        for value in data.values():
            u_isd.update(value.keys())
    while True:
        name = input('Введите имя: ')
        if not name:
            break
        id = input('Введите id: ')

        lvl = input('Введите уровень от 1 до 7: ')
        if ~ (id in u_isd and data[lvl].get(id) is None): # '~' - отрицание
            data[lvl].update({id: name}) # .update({id: name}) - добавление словаря
            with open(file, 'w', encoding='UTF-8') as f_write:
                json.dump(data, f_write, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    set_users(Path('user.json'))