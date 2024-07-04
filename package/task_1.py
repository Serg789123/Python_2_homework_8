__all__ = ['convert']

import json
from pathlib import Path

def convert(file: str | Path) -> None:
    my_dict = {}
    with open(file, 'r', encoding='UTF-8') as f:
        for line in f:
            name, number = line.split()
            my_dict[name.title()] = float(number)
    # print(file.stem)
    with open(f'{file.stem}.json', 'w', encoding='UTF-8') as f_write: # меняем расширение
        json.dump(my_dict, f_write, indent=2, ensure_ascii=False) # (словарь, файловый дескриптор,
        # количество отступов, норм рус язык)

if __name__ == '__main__':
    convert(Path('results.txt'))