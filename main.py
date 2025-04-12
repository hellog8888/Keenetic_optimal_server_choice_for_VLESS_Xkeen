import os
import time
from ping3 import ping

#local files
import hosts, func, func_with_location

print("")
measurement_start_time = time.time()
print(f"Start: {func.current_date_and_time()}")

#Здесь задается параметр колличество ICMP запросов
total_count_ping_req = 10

result_pass_ping = {}
result_no_pass_ping = []

ip_country_dict = {}

print("-----------------------------------------------------")
print(f"1.  Словарь с IP")
print(f"1.1 ")

print("")

#Создаем словарь с IP адреса если их нет во внешнем локальном файла
for ip in hosts.hosts:
    country = func_with_location.get_country_by_ip(ip)
    ip_country_dict[ip] = country
    print(f"IP: {ip} : {country}")
    time.sleep(2)  # Пауза 1 секунда, чтобы не превысить лимит запросов API

print(f"1.2 Все ip присутствуют в локальном файле")
print("-----------------------------------------------------")

def base_station_get_from_export_romes(file_txt):
    with open(file_txt, 'r') as file_txt_r:
        return list(set([line[line.strip().find(':') + 1: line.strip().find('/')] for line in file_txt_r if
                         line.startswith('eNodeB') and line.strip().split(';')[13] != 11]))


print("-----------------------------------------------------")
print(f"2.  Проверка хостов по ICMP запросу.")
print(f"2.2 Каждый хост проходит проверку доступности на {total_count_ping_req} запросов")

for ip in hosts.hosts:
    print(f"IP: {ip}")

    total_time = 0
    count_error = 0
    temp_lst_for_med = []

    for attempt in range(1, total_count_ping_req + 1):
        response = ping(ip, timeout=1, unit='ms')
        
        if response is False or response is None:
            count_error += 1
            if count_error == 3:
                break
        else:
            temp_lst_for_med.append(response)

    if temp_lst_for_med and count_error < 3:
        result_pass_ping[ip] = func.find_median(temp_lst_for_med)
    else:
        result_no_pass_ping.append(ip)

print(f"Проверка хостов по ping(-у) завершена за: {time.time() - measurement_start_time:.2f} секунд")
print("")
print(f"IP не прошедших проверку: {0 if not result_no_pass_ping else [print(x) for x in result_no_pass_ping]}")
print("-----------------------------------------------------")



#Stage 2
sorted_dict_desc = dict(sorted(result_pass_ping.items(), key=lambda x: x[1]))
ip_list = list(sorted_dict_desc.keys())

count = 0
for key, value in sorted_dict_desc.items():
    if count < 3:
        print(f"{key}: {value}")
        time.sleep(1)
        count += 1
    else:
        break


#Stage 4
print("")
print(f"{ip_list[0]} : {ip_country_dict[ip_list[0]]}")
os.system(f"mtr -r -c 50 {list(sorted_dict_desc.keys())[0]}")
time.sleep(50)

print("")
print(f"{ip_list[1]} : {ip_country_dict[ip_list[1]]}")
os.system(f"mtr -w -c 50 {list(sorted_dict_desc.keys())[1]}")
time.sleep(50)

print("")
print(f"{ip_list[2]} : {ip_country_dict[ip_list[2]]}")
os.system(f"mtr -w -c 50 {list(sorted_dict_desc.keys())[2]}")


print(f"\nОбщее время выполнения: {time.time() - measurement_start_time:.2f} секунд")