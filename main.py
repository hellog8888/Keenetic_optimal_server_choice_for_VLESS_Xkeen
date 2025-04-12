import os
import time

# local files
import func, func_ip_location, func_ip_test


if __name__ == "__main__":

    print("")
    measurement_start_time = time.time()
    print(f"Start: {func.current_date_and_time()}")

    # Колличество ICMP запросов на 1 IP
    count_ping_req = 200

    print("-----------------------------------------------------")
    print(f"1.  IP:Location")
    print(f"1.1 Чтение IP-адресов из локального файла hosts.txt")
    ip_country_dict_lst = func.get_lst_from_file('hosts.txt')
    # Создание словаря IP:Location из локального файла hosts.txt
    ip_country_dict = func_ip_location.ip_and_country_lst_to_dict('ip_and_country_lst.txt')
    print(f"1.2 Создание словаря IP:Location из локальных файлов ip_and_country_lst.txt + hosts.txt")
    ip_country_dict = func_ip_location.create_ip_country_dict(ip_country_dict_lst, ip_country_dict)
    print(f"Time execution #1: {time.time() - measurement_start_time:.4f} сек.")

    print("-----------------------------------------------------")
    print(f"2.  Ping")
    print(f"2.1 Поверка доступности. {count_ping_req} ICMP запросов на host")
    result_pass_ping, result_pass_ping_no = (func_ip_test.ping_cheking([*ip_country_dict], count_ping_req))
    print(f"2.2 IP не прошедших проверку: {0 if not result_pass_ping_no else [print(x) for x in result_no_pass_ping]}")
    [print(f"{key}: {value}") for key, value in result_pass_ping.items()]
    print(f"Time execution #2: {time.time() - measurement_start_time:.2f} сек.")

    # Stage 3

    # Stage 4

    # Запись ip_country_dict в файл ip_and_country_lst

    print(f"Total time execution: {time.time() - measurement_start_time:.4f} сек.")
