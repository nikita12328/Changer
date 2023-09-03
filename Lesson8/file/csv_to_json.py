import csv
import json
import os
from pathlib import Path


def csv_to_json(csv_file, json_file):
    if not os.path.isfile(Path.cwd() / csv_file):
        print(f'Файл {csv_file} не найден')
        return
    json_list = []
    with open(Path.cwd() / csv_file, 'r', encoding='utf-8') as csv_f:
        reader = csv.reader(csv_f)
        for i, row in enumerate(reader):
            if i == 0:
                continue
            json_dict = {}
            level, user_id, name = row
            json_dict['level'] = int(level)
            json_dict['id'] = user_id.zfill(10)
            json_dict['name'] = name.title()
            json_dict['hash'] = hash(f'{user_id}{name}')
            json_list.append(json_dict)

    with open(Path.cwd() / json_file, 'w', encoding='utf-8') as json_f:
        json.dump(json_list, json_f, indent=2)

    print(f'данные сконвертированы с {csv_file} в {json_file}')
