from homework9.parser import get_system_users
from homework9.parser import get_process_quantity
from homework9.parser import get_process_per_user
from homework9.parser import get_memory_usage
from homework9.parser import get_cpu_usage
from homework9.parser import get_hardest_cpu_process
from homework9.parser import save_report_to_txt
from homework9.parser import list_output
from homework9.parser import dict_output

if __name__ == '__main__':
    print("Отчет о состоянии системы:", "\n")

    print("Пользователи системы:")
    list_output(get_system_users())

    print()
    print("Процессов запущено:", get_process_quantity())

    print()
    print("Пользовательских процессов:")
    dict_output(get_process_per_user())

    print()
    print("Всего памяти используется:", get_memory_usage())

    print()
    print("Всего CPU используется:", get_cpu_usage())

    print()
    print("Больше всего CPU использует:", get_hardest_cpu_process()[1], "-", get_hardest_cpu_process()[0], "%")

    save_report_to_txt(get_system_users(), get_process_quantity(), get_process_per_user(), get_memory_usage(),
                       get_cpu_usage(), get_hardest_cpu_process())
