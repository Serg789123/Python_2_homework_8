"""Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов."""

from package.task_1 import convert
from package.task_2 import set_users
from package.task_3 import json_to_csv
from package.task_4 import csv_to_json
from package.task_5 import json_to_pickle
from package.task_6 import pickle_to_csv
from package.task_7 import csv_to_pickle
from task8_1 import directory_walker

if __name__ == '__main__':
    directory_walker("./package")
