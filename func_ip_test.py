from ping3 import ping
import func
import os
import nmap
impoer scapy


def ping_cheking(hosts, count_ping_req):

    result_pass_ping = {}
    result_pass_ping_no = []
    count_lst_ip = len(hosts)

    for i, ip in enumerate(hosts, start=1):
        print(f"IP: {ip} [{i} from {count_lst_ip}]")

        count_error = 0
        temp_lst_for_med = []

        for attempt in range(1, count_ping_req + 1):
            # Параметры проверки
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
            result_pass_ping_no.append(ip)

        result_pass_ping = dict(sorted(result_pass_ping.items(), key=lambda x: x[1]))

    return result_pass_ping, result_pass_ping_no
