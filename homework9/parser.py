import subprocess
from datetime import datetime


# Получаем данные команды "ps aux" и осуществляем разбивку по столбцам
def get_ps_aux_data():
    process = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE, encoding="utf-8").communicate()[0]
    result = process.split('\n')
    nfields = len(result[0].split()) - 1
    aux_data = []
    for row in result[1:]:
        aux_data.append(row.split(None, nfields))
        aux_data = list(filter(None, aux_data))
    return aux_data


# Осуществляем поиск уникальных пользователей системы
def get_unique_system_users(aux_data: list):
    unique_users = []
    for element in aux_data:
        unique_users.append(element[0])
    return list(set(unique_users))


# Осуществляем поиск количества всех выполняемых процессов в системе
def get_process_quantity(aux_data: list):
    quantity = len(aux_data)
    return quantity


# Агрегируем данные всех процессов по именам пользователей в единый словарь
def get_all_processes_per_users(aux_data: list):
    users_processes = {}
    for user in get_unique_system_users(aux_data):
        filtered = filter(lambda c: user in c, aux_data)
        user_process = {user: len(list(filtered))}
        users_processes.update(user_process)
    return users_processes


# Находим количество используемой всеми процессами памяти
def get_all_memory_usage(aux_data: list):
    mem_usage_list = []
    mem_usage = 0
    for process in aux_data:
        mem_usage_list.append(process[3])
    for elem in mem_usage_list:
        mem_usage += float(elem)
    return round(mem_usage, 1)


# Находим процент использования памяти процессора
def get_cpu_usage(aux_data: list):
    cpu_usage_list = []
    cpu_usage = 0
    for process in aux_data:
        cpu_usage_list.append(process[2])
    for elem in cpu_usage_list:
        cpu_usage += float(elem)
    return round(cpu_usage, 1)


# Находим процесс, использующий больше всего RAM (памяти)
def get_hardest_ram_process(aux_data: list):
    ram_usage_list = []
    for process in aux_data:
        ram_usage_list.append(process[3])
    for hard_ram_process in aux_data:
        if ram_usage_list[0] in hard_ram_process:
            return hard_ram_process[-1][:20]


# Находим процесс, использующий больше всего CPU (процессора)
def get_hardest_cpu_process(aux_data: list):
    cpu_usage_list = []
    for process in aux_data:
        cpu_usage_list.append(process[2])
    max_element = max(cpu_usage_list, key=lambda i: float(i))
    for hard_cpu_process in aux_data:
        if max_element in hard_cpu_process[2]:
            return hard_cpu_process[-1][:20]


# Построчный вывод значений словаря
def dict_output(data: dict):
    for key in data:
        print(key, ":", data[key])


# Построчный вывод значений списка
def list_output(data: list):
    for elem in data:
        print(elem)


# Запись отчета в файл с расширением *.txt
def save_report_to_txt(sys_users: list, process_quantity: int, process_per_user: dict, mem_usage: float,
                       cpu_usage: float, hard_ram_process: str, hard_cpu_process: str):
    date_time_str = datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p")
    with open(f"{date_time_str}-scan.txt", "w") as file:
        file.write("Отчет о состоянии системы:" + "\n" + "\n")
        file.write("Пользователи системы:" + "\n")
        for line in sys_users:
            file.write(line + "\n")
        file.write("\n")
        file.write("Процессов запущено: " + str(process_quantity) + "\n" + "\n")
        file.write("Пользовательских процессов:" + "\n")
        for k, v in process_per_user.items():
            file.write(str(k) + ": " + str(v) + "\n")
        file.write("\n" + "Всего памяти используется: " + str(mem_usage) + " %" + "\n" + "\n")
        file.write("Всего CPU используется: " + str(cpu_usage) + " %" + "\n" + "\n")
        file.write(
            "Больше всего памяти использует процесс: " + hard_ram_process + "\n" + "\n")
        file.write(
            "Больше всего CPU использует процесс: " + hard_cpu_process + "\n")
