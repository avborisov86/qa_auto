"""
School: OTUS "QA Automation"
Task 7: Writing parser for collecting data from *.log file
"""

import re
import json
from collections import Counter


# Считываем данные из файла
def reader(path_to_filename: str):
    with open(path_to_filename) as f:
        log = f.read()
    return log


# Создать пустой файл parsing_results.json
def create_json():
    json_data = []
    with open('parsing_results.json', 'w') as file:
        file.write(json.dumps(json_data, indent=2, ensure_ascii=False))


# Добавляем данные в формате json в созданный ранее файл parsing_results.json
def add_to_json(json_data: object):
    data = json.load(open("parsing_results.json"))
    data.append(json_data)
    with open("parsing_results.json", "w") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


# Получить количество запросов в искомом файле (дополнительные параметры: 'all_requests', 'get_requests', 'post_requests', 'head_requests')
def get_requests_quantity(path_to_filename: str, param: str):
    # Считаем общее количество выполненных запросов
    if param == 'all_requests':
        regexp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        requests_list = re.findall(regexp, reader(path_to_filename))
        all_req_quant = len(requests_list)
        json_data = {
            "Общее количество выполненных запросов": all_req_quant
        }
        # Записываем найденные данные в json файл
        add_to_json(json_data)
        # Выводим в терминал данные об общем количестве выполненных запросов
        print('Общее количество выполненных запросов: ', all_req_quant)
        return all_req_quant
    # Считаем общее количество выполненных GET запросов
    elif param == 'get_requests':
        regexp = r'GET'
        requests_list = re.findall(regexp, reader(path_to_filename))
        get_req_quant = len(requests_list)
        json_data = {
            "Количество запросов типа GET": get_req_quant
        }
        # Записываем найденные данные в json файл
        add_to_json(json_data)
        # Выводим в терминал данные о количестве GET запросов
        print('Количество запросов типа "GET": ', get_req_quant)
        return get_req_quant
    # Считаем общее количество выполненных POST запросов
    elif param == 'post_requests':
        regexp = r'POST'
        requests_list = re.findall(regexp, reader(path_to_filename))
        post_req_quant = len(requests_list)
        json_data = {
            "Количество запросов типа POST": post_req_quant
        }
        # Записываем найденные данные в json файл
        add_to_json(json_data)
        # Выводим в терминал данные о количестве POST запросов
        print('Количество запросов типа "POST": ', post_req_quant)
        return post_req_quant
    # Считаем общее количество выполненных HEAD запросов
    elif param == 'head_requests':
        regexp = r'HEAD'
        requests_list = re.findall(regexp, reader(path_to_filename))
        head_req_quant = len(requests_list)
        json_data = {
            "Количество запросов типа HEAD": head_req_quant
        }
        # Записываем найденные данные в json файл
        add_to_json(json_data)
        # Выводим в терминал данные о количестве GET запросов
        print('Количество запросов типа "HEAD": ', head_req_quant, "\n")
        return head_req_quant
    else:
        print('Enter valid searching value/parameter..', "\n")


# Ищем топ 3 IP адресов, с которых было сделано наибольшее количество запросов
def find_most_freq_requests(path_to_filename: str):
    data = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', reader(path_to_filename))
    counter = Counter(data)
    most_freq_list = counter.most_common(3)
    i = 0
    ips_list = []
    while i < len(most_freq_list):
        ips_list.append(most_freq_list[i][0])
        i += 1
    json_data = {
        "Топ 3 IP адресов, с которых были сделаны запросы": {
            "1 место": ips_list[0],
            "2 место": ips_list[1],
            "3 место": ips_list[2],
        }
    }
    # Записываем найденные данные в json файл
    add_to_json(json_data)
    # Выводим в терминал данные 3х IP, с которых было сделано наибольшее количество запросов
    print('Топ 3 IP адресов, с которых были сделаны запросы:')
    print('1 место: ', ips_list[0])
    print('2 место: ', ips_list[1])
    print('3 место: ', ips_list[2], "\n")
    return ips_list


# Ищем топ 3х самых долгих запросов
def find_slowest_requests(path_to_filename: str):
    time_regex = r'\" .\d{3,6}'
    data = re.findall(time_regex, reader(path_to_filename))
    counter = Counter(data)
    slowest_requests_list = counter.most_common(3)
    request_time = "".join(c for c in slowest_requests_list[0][0] if c.isdecimal())
    file_data = open(path_to_filename).readlines()
    count = 0
    requests_list = []
    for elem in iter(file_data):
        if request_time in elem:
            requests_list.append(elem)
        count += 1
    json_data = {
        "Топ 3х самых долгих запросов": {
            "1 место": requests_list[0],
            "2 место": requests_list[1],
            "3 место": requests_list[2],
        }
    }
    # Записываем найденные данные в json файл
    add_to_json(json_data)
    # Выводим в терминал данные топ 3х самых долгих запросов
    print('Топ 3х самых долгих запросов:')
    print('1 место: ', requests_list[0])
    print('2 место: ', requests_list[1])
    print('3 место: ', requests_list[2])
    return requests_list
