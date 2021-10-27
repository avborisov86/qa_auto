from homework9.parser import get_ps_aux_data
from homework9.parser import get_unique_system_users
from homework9.parser import get_process_quantity
from homework9.parser import get_all_processes_per_users
from homework9.parser import get_all_memory_usage
from homework9.parser import get_cpu_usage
from homework9.parser import get_hardest_ram_process
from homework9.parser import get_hardest_cpu_process
from homework9.parser import save_report_to_txt
from homework9.parser import list_output
from homework9.parser import dict_output

if __name__ == '__main__':
    print("Отчет о состоянии системы:", "\n")

    aux_data = get_ps_aux_data()

    print("Пользователи системы:")
    list_output(get_unique_system_users(aux_data))

    print()
    print("Процессов запущено:", get_process_quantity(aux_data))

    print()
    print("Пользовательских процессов:")
    dict_output(get_all_processes_per_users(aux_data))

    print()
    print("Всего памяти используется:", get_all_memory_usage(aux_data), "%")

    print()
    print("Всего CPU используется:", get_cpu_usage(aux_data), "%")

    print()
    print("Больше всего памяти использует процесс:", get_hardest_ram_process(aux_data))

    print()
    print("Больше всего CPU использует процесс:", get_hardest_cpu_process(aux_data))

    save_report_to_txt(get_unique_system_users(aux_data), get_process_quantity(aux_data),
                       get_all_processes_per_users(aux_data), get_all_memory_usage(aux_data), get_cpu_usage(aux_data),
                       get_hardest_ram_process(aux_data), get_hardest_cpu_process(aux_data))
