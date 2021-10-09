import subprocess
import re
from datetime import datetime


# Осуществляем поиск пользователей системы, у которых есть процессы
def get_system_users():
    users = subprocess.run("dscl . -list /Users", shell=True, stdout=subprocess.PIPE, encoding="utf-8")
    users_list = users.stdout.split("\n")
    system_users_list = []
    for user in users_list:
        if '_' not in user:
            system_users_list.append(user)
    system_users_list = list(filter(None, system_users_list))
    return system_users_list


# Осуществляем поиск количества выполняемых процессов в системе
def get_process_quantity():
    process = subprocess.run("ps -eo pid,ppid,user", shell=True, stdout=subprocess.PIPE, encoding="utf-8")
    process_list = process.stdout.split("\n")
    quantity = len(process_list)
    return quantity


# Осуществляем поиск выполняемых процессов в зависимости от имени пользователя
def get_process_per_user():
    user_list = []
    quantity_list = []
    result_list = {}
    for user in get_system_users():
        user_list.append(user)
        process_per_user = subprocess.run(f"ps -U {user}", shell=True, stdout=subprocess.PIPE, encoding="utf-8")
        process_list = process_per_user.stdout.split("\n")
        quantity_list.append(len(process_list))
        for i in range(len(user_list)):
            result_list[user_list[i]] = quantity_list[i]
    return result_list


# Находим количество используемой памяти
def get_memory_usage():
    process = subprocess.run("top -l 1 -s 0 | grep PhysMem", shell=True, stdout=subprocess.PIPE, encoding="utf-8")
    memory_usage_list = process.stdout.split("\n")
    memory_usage_list = list(filter(None, memory_usage_list))
    regexp = r": \d{1,2}[A-Z]"
    for elem in memory_usage_list:
        matching = re.findall(regexp, elem)
        memory = ''.join(matching).replace(': ', '')
        return memory


# Находим процент использования памяти процессора
def get_cpu_usage():
    process = subprocess.run("top -l 1 -s 0 | grep CPU", shell=True, stdout=subprocess.PIPE, encoding="utf-8")
    cpu_usage_list = process.stdout.split("\n")
    cpu_list = cpu_usage_list[0].partition(':')[2]
    return cpu_list


# Находим процент использования памяти процессора самым тяжелым процессом
def get_hardest_cpu_process():
    process = subprocess.run("ps ahux", shell=True, stdout=subprocess.PIPE, encoding="utf-8")
    cpu_processes_list = process.stdout.split("\n")
    hardest_cpu_process_elems = cpu_processes_list[1].split()
    hardest_cpu_process = []
    hardest_cpu_process.append(hardest_cpu_process_elems[2])
    hardest_cpu_process.append(hardest_cpu_process_elems[-2])
    return hardest_cpu_process


# Построчный вывод значений словаря
def dict_output(data: dict):
    for key in data:
        print(key, ":", data[key])


# Построчный вывод значений списка
def list_output(data: list):
    for elem in data:
        print(elem)


# Запись отчета в файл с расширением *.txt
def save_report_to_txt(sys_users: list, process_quantity: int, process_per_user: dict, mem_usage: str, cpu_usage: str,
                       hard_process: list):
    date_time_str = datetime.now().strftime("%d-%m-%Y_%I-%M-%S_%p")
    with open(f"{date_time_str}-scan.txt", "w") as file:
        file.write("Отчет о состоянии системы:" + "\n" + "\n")
        file.write("Пользователи системы:" + "\n")
        for line in sys_users:
            file.write(line + "\n")
        file.write("\n")
        file.write("Процессов запущено: " + str(process_quantity) + "\n" + "\n")
        file.write("Пользовательских процессов:" + "\n")
        for line in process_per_user:
            file.write(line + "\n")
        file.write("\n" + "Всего памяти используется: " + mem_usage + "\n" + "\n")
        file.write("Всего CPU используется: " + cpu_usage + "\n" + "\n")
        file.write(
            "Больше всего CPU использует процесс: " + hard_process[1] + " - " + hard_process[
                0] + "%" + "\n")
