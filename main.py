import os
import time

# local files
import func, func_ip_location, func_ip_test


if __name__ == "__main__":

    print("")
    measurement_start_time = time.time()
    print(f"Start: {func.current_date_and_time()}")

    # Колличество ICMP запросов на 1 IP
    count_ping_req = 2

    print("-----------------------------------------------------")
    print(f"1.  IP:Location")
    print(f"1.1 Reading IP addresses from local hosts.txt file")
    ip_country_dict_lst = func.get_lst_from_file('hosts.txt')
    # Создание словаря IP:Location из локального файла hosts.txt
    ip_country_dict = func_ip_location.ip_and_country_lst_to_dict('ip_and_country_lst.txt')
    print(f"1.2 Creating an IP:Location dictionary from local hosts.txt + ip_and_country_lst.txt files")
    ip_country_dict = func_ip_location.create_ip_country_dict(ip_country_dict_lst, ip_country_dict)
    print(f"Time execution #1: {time.time() - measurement_start_time:.4f} sec.")

    print("-----------------------------------------------------")
    print(f"2.  Ping test")
    print(f"2.1 Availability check. {count_ping_req} ICMP requests to host")
    result_no_pass_ping = []
    result_pass_ping, result_pass_ping_no = func_ip_test.ping_cheking(ip_country_dict_lst, count_ping_req)
    print("")
    print(f"2.2 IP not verified: {0 if not result_pass_ping_no else [print(x) for x in result_no_pass_ping]}")
    print("")
    print(f"2.3 TOP 3 IP of successful candidates:")
    best_3_ip = list(result_pass_ping.items())[:3]
    [print(f"IP: {ip} - median latency {delay:.2f}") for ip, delay in best_3_ip]
    print("")
    print(f"Time execution #1 #2: {time.time() - measurement_start_time:.2f} sec.")

    print("-----------------------------------------------------")
    print(f"3.  Test Network Distance")
    
    print("2.3 TOP 3 IP of Network Distance:")
    

    # Stage 4


    # Запись ip_country_dict в файл ip_and_country_lst

    print(f"Total time execution: {time.time() - measurement_start_time:.4f} sec.")
