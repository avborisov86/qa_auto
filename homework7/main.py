from homework7.parser import create_json
from homework7.parser import get_requests_quantity
from homework7.parser import find_most_freq_requests
from homework7.parser import find_slowest_requests

if __name__ == '__main__':
    # Создаем пустой файл parsing_results.json
    create_json()

    # Считаем общее количество выполненных запросов и дописываем в parsing_results.json
    get_requests_quantity('/Users/avboris/Desktop/access.log', 'all_requests')

    # Считаем количество выполненных запросов типа GET и дописываем в parsing_results.json
    get_requests_quantity('/Users/avboris/Desktop/access.log', 'get_requests')

    # Считаем количество выполненных запросов типа POST и дописываем в parsing_results.json
    get_requests_quantity('/Users/avboris/Desktop/access.log', 'post_requests')

    # Считаем количество выполненных запросов типа HEAD и дописываем в parsing_results.json
    get_requests_quantity('/Users/avboris/Desktop/access.log', 'head_requests')

    # Ищем топ 3 IP адресов, с которых было сделано наибольшее количество запросов, и дописываем в parsing_results.json
    find_most_freq_requests('/Users/avboris/Desktop/access.log')

    # Ищем топ 3х самых долгих запросов и дописываем в parsing_results.json
    find_slowest_requests('/Users/avboris/Desktop/access.log')
